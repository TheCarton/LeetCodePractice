fn main() {
    println!("Hello, world!");
}
// multiply a number and keep track of the digits in a vector
struct Solution;
impl Solution {
    const MAX_DIGITS: u32 = 9;
    pub fn reverse(x: i32) -> i32 {
        let x_abs = x.checked_abs();
        if x_abs.is_none() {
            return 0;
        }
        let m = x_abs.unwrap();
        let sign = if x.is_negative() { -1 } else { 1 };
        let log = m.ilog10();
        if log == Self::MAX_DIGITS {
            return Self::checked_reverse(m, sign);
        }
        let mut num = m;
        let mut rev = 0;
        for i in 0..=log {
            let exp = log - i;
            let y = 10_i32.pow(exp);
            let cur_digit = num % 10;
            rev += cur_digit * y;
            num = (num - cur_digit) / 10;
        }
        return sign * rev;
    }
    fn checked_reverse(x: i32, sign: i32) -> i32 {
        let mut num = x;
        let mut rev: i32 = 0;
        for i in 0..=Self::MAX_DIGITS {
            let exp = Self::MAX_DIGITS - i;
            let cur_digit = num % 10;
            if let Some(y) = 10_i32.checked_pow(exp) {
                if let Some(m) = cur_digit.checked_mul(y) {
                    if let Some(p) = rev.checked_add(m) {
                        rev = p;
                        num = (num - cur_digit) / 10;
                        continue;
                    }
                }
            }
            return 0;
        }
        return sign * rev;
    }
}

#[test]
fn happy() {
    let forward = 134;
    let backward = 431;
    let r = Solution::reverse(forward);
    assert_eq!(backward, r);
}

#[test]
fn use_all_digits() {
    // 2147483647
    let forward = 2111111111;
    let backward = 1111111112;
    let r = Solution::reverse(forward);
    assert_eq!(backward, r);
}


#[test]
fn negative() {
    let forward = -134;
    let backward = -431;
    let r = Solution::reverse(forward);
    assert_eq!(backward, r);
}

#[test]
fn overflow() {
    // 2147483647
    let forward = 2111111117;
    let r = Solution::reverse(forward);
    assert_eq!(0, r);
}

