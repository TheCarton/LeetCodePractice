fn main() {
    println!("Hello, world!");
}
struct Solution;
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let mut longest_start = 0;
        let mut longest_len = 1;
        let bytes = s.as_bytes();

        for i in 0..s.len() {
            let mut right = i;
            while right < s.len() && bytes[i] == bytes[right] {
                right += 1;
            }
            let mut left = i as i64 - 1;
            while left >= 0 && right < s.len() && bytes[left as usize] == bytes[right] {
                left -= 1;
                right += 1;
            }
            let new_len = (right as i64 - left - 1) as usize;
            if new_len > longest_len {
                longest_len = new_len;
                longest_start = (left + 1) as usize;
            }
        }
        s[longest_start..longest_start + longest_len].to_string()
    }
}
#[test]
fn happy() {
    let s = "babad";
    let correct = "bab";
    let r = Solution::longest_palindrome(s.to_string());
    assert_eq!(correct, r);
}

#[test]
fn all_palindrome() {
    let s = "bab";
    let correct = "bab";
    let r = Solution::longest_palindrome(s.to_string());
    assert_eq!(correct, r);
}
