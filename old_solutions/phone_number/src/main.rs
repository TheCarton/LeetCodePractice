fn main() {
    println!("Hello, world!");
}
struct Solution;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return Vec::new();
        }
        let table: [String; 10] = [
            "".to_owned(),
            "".to_owned(),
            "abc".to_owned(),
            "def".to_owned(),
            "ghi".to_owned(),
            "jkl".to_owned(),
            "mno".to_owned(),
            "pqrs".to_owned(),
            "tuv".to_owned(),
            "wxyz".to_owned(),
        ];
        let size: usize = digits
            .as_bytes()
            .iter()
            .map(|c| table[*c as usize - '0' as usize].len())
            .product();
        let mut repeat = size;
        let mut combos = vec!["".to_owned(); size];
        for &c in digits.as_bytes().iter() {
            let mut letters = table[c as usize - '0' as usize].as_bytes().iter().cycle();
            repeat /= table[c as usize - '0' as usize].len();
            let mut i = repeat;
            let mut letter = *letters.next().unwrap() as char;
            for combo in combos.iter_mut() {
                combo.push(letter);
                i -= 1;
                if i == 0 {
                    letter = *letters.next().unwrap() as char;
                    i = repeat;
                }
            }
        }
        combos
    }
}
