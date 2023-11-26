fn main() {
    println!("wat");
}

struct Solution;

impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        if dividend == divisor {
            return 1;
        }
        let is_positive = dividend.signum() == divisor.signum();
        let mut dividend_abs = dividend.unsigned_abs();
        let divisor_abs = divisor.unsigned_abs();
        let mut quotient = 0;
        while dividend_abs >= divisor_abs {
            let mut q = 0;
            while dividend_abs > divisor_abs << (q + 1) {
                q += 1;
            }
            quotient += 1 << q;
            dividend_abs -= divisor_abs << q;
        }
        if is_positive && quotient >= i32::MAX as u32 {
            return i32::MAX;
        }
        if is_positive {
            quotient as i32
        } else if let Some(q) = (quotient as i32).checked_neg() {
            q
        } else {
            i32::MIN
        }
    }
}

#[test]
fn both_positive() {
    let r = Solution::divide(4, 2);
    assert_eq!(r, 2);
}

#[test]
fn negative_divisor() {
    let r = Solution::divide(4, -2);
    assert_eq!(r, -2);
}

#[test]
fn negative_dividend() {
    let r = Solution::divide(-4, 2);
    assert_eq!(r, -2);
}

#[test]
fn both_negative() {
    let r = Solution::divide(-4, -2);
    assert_eq!(r, 2);
}

#[test]
fn min_dividend() {
    let r = Solution::divide(i32::MIN, 1);
    assert_eq!(r, i32::MIN);
}
