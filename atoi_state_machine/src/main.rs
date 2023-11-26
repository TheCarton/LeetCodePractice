fn main() {
    println!("Hello, world!");
}
struct Solution;

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        enum Phase {
            Whitespace,
            Sign,
            Digit,
        }
        let mut phase = Phase::Whitespace;
        let mut num: i64 = 0;
        let mut sign = 1;

        let mut chars = s.chars().peekable();
        while let Some(c) = chars.peek() {
            match phase {
                Phase::Whitespace => {
                    if *c == ' ' {
                        chars.next();
                        continue;
                    }
                    phase = Phase::Sign;
                }
                Phase::Sign => {
                    phase = Phase::Digit;
                    match c {
                        '-' => {
                            sign = -1;
                            chars.next();
                        }
                        '+' => {
                            chars.next();
                        }
                        _ => {}
                    }
                }
                Phase::Digit => {
                    if !c.is_ascii_digit() || num > i32::MAX.into() {
                        break;
                    }
                    num = num * 10 + (*c as i64) - ('0' as i64);
                    chars.next();
                }
            }
        }
        (sign * num).clamp(i32::MIN.into(), i32::MAX.into()) as i32
    }
}
