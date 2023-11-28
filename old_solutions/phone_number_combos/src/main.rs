fn main() {
    println!("{:?}", Solution::letter_combinations(String::from("23")));
}
struct Solution;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return vec![];
        }
        let table: [String; 8] = [
            String::from("abc"),
            String::from("def"),
            String::from("ghi"),
            String::from("jkl"),
            String::from("mno"),
            String::from("pqrs"),
            String::from("tuv"),
            String::from("wxyz"),
        ];
        let mut combos = vec![];
        for ch in digits.chars() {
            let new_word = &table[ch as usize - '2' as usize];
            combos = Self::combine(new_word, &combos);
        }
        return combos;
    }
    // abc + [] -> [a, b, c]
    // def + [a, b, c] -> [ad, ae, af, bd, be, bf, cd, ce, cf]

    fn combine(word: &str, list: &Vec<String>) -> Vec<String> {
        if list.is_empty() {
            let mut new_list: Vec<String> = Vec::with_capacity(word.len());
            for ch in word.chars() {
                new_list.push(ch.to_string());
            }
            return new_list;
        }
        let mut new_list: Vec<String> = Vec::with_capacity(list.len() * word.len());
        for combo in list.iter() {
            for ch in word.chars() {
                let mut new_combo = combo.clone();
                new_combo.push(ch);
                new_list.push(new_combo);
            }
        }
        return new_list;
    }
}
