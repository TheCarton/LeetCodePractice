fn main() {
    println!("Hello, world!");
}
struct Solution;

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut chars = s.trim().chars().peekable();
        let mut sign: i32 = 1;
        if let Some(c) = chars.peek() {
            sign = match c {
                '+' => {
                    chars.next();
                    1
                }
                '-' => {
                    chars.next();
                    -1
                }
                _ => 1,
            };
        }
        let mut number: i32 = 0;
        for char in chars.skip_while(|char| *char == '0') {
            if !char.is_ascii_digit() {
                break;
            }
            if let Some(n) = number
                .checked_mul(10)
                .and_then(|number| number.checked_add((char as i32) - ('0' as i32)))
            {
                number = n
            } else if sign.is_positive() {
                return i32::MAX;
            } else {
                return i32::MIN;
            }
        }
        sign * number
    }
}
