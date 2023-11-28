fn main() {}
struct Solution;
impl Solution {
    const MAX_DIGITS: usize = 10;
    const MAX_ARRAY: [i32; 10] = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7];
    pub fn reverse(x: i32) -> i32 {
        let x_abs = x.checked_abs();
        if x_abs.is_none() {
            return 0;
        };
        let mut x_copy = x_abs.unwrap();
        let mut len_digits = 0;
        let mut could_overflow: Option<bool> = None;
        let mut rev = 0;
        println!("\n forward = {}", x);
        while x_copy > 0 {
            let d = x_copy % 10;
            println!("\nd = {}", d);
            println!("len digit = {}", len_digits);
            println!("max digit = {}", Self::MAX_ARRAY[len_digits]);
            println!("rev = {}", rev);
            if d > Self::MAX_ARRAY[len_digits] && could_overflow.is_none() {
                println!("could overflow.");
                could_overflow = Some(true);
            }
            if d < Self::MAX_ARRAY[len_digits] && could_overflow.is_none() {
                could_overflow = Some(false);
            }
            len_digits += 1;
            if len_digits == Self::MAX_DIGITS && could_overflow.unwrap_or(false) {
                println!("\n return 0");
                return 0;
            }
            rev = rev * 10 + d;
            x_copy /= 10;
        }
        if x.is_positive() {
            rev
        } else {
            -rev
        }
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

    let forward = -2147483412;
    let backward = -2143847412;
    let r = Solution::reverse(forward);
    assert_eq!(backward, r);
}

#[test]
fn overflow() {
    // 2147483647
    let forward = 2111111117;
    let r = Solution::reverse(forward);
    assert_eq!(0, r);

    let forward = 2147483647;
    let r = Solution::reverse(forward);
    assert_eq!(0, r);

    let forward = 1563847412;
    let r = Solution::reverse(forward);
    assert_eq!(0, r);
}
