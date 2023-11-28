use std::cmp::max;
struct Solution;
fn main() {
    println!("hello world!");
}
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut max_len = 0;
        let mut substring_start = 0;
        let mut ascii_table: [Option<usize>; 128] = [None; 128];
        for (i, &c) in s.as_bytes().iter().enumerate() {
            let repeat_char_in_substring =
                ascii_table[c as usize].is_some_and(|j| j >= substring_start);
            if repeat_char_in_substring {
                substring_start = ascii_table[c as usize].unwrap() + 1;
            }
            let substring_len = i - substring_start + 1;
            max_len = max(substring_len, max_len);
            ascii_table[c as usize] = Some(i);
        }
        max_len as i32
    }
}

#[test]
fn longest_is_in_start() {
    let s = "abcabcbb";
    let correct = 3;
    let r = Solution::length_of_longest_substring(s.to_string());
    assert_eq!(r, correct);
}

#[test]
fn longest_is_in_middle() {
    let s = "bbb12345bbbb";
    let correct = 6;
    let r = Solution::length_of_longest_substring(s.to_string());
    assert_eq!(r, correct);
}

#[test]
fn abba() {
    let s = "abba";
    let correct = 2;
    let r = Solution::length_of_longest_substring(s.to_string());
    assert_eq!(r, correct);
}

#[test]
fn empty() {
    let s = "";
    let correct = 0;
    let r = Solution::length_of_longest_substring(s.to_string());
    assert_eq!(r, correct);
}

#[test]
fn blank() {
    let s = " ";
    let correct = 1;
    let r = Solution::length_of_longest_substring(s.to_string());
    assert_eq!(r, correct);
}
