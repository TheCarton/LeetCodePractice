impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        for (i, _) in haystack.chars().enumerate() {
            if i + needle.len() > haystack.len() {
                return -1;
            }
            if &haystack[i..i + needle.len()] == &needle[..] {
                return i.try_into().unwrap();
            }
        }
        return -1;
    }
}
struct Solution;

#[test]
fn substring_in_start() {
    let s1 = "hello";
    let s2 = "hell";
    let correct = 0;
    let r = Solution::str_str(s1.to_string(), s2.to_string());
    assert_eq!(r,correct);
}

#[test]
fn no_substring() {
    let s1 = "hello";
    let s2 = "xyz";
    let correct = -1;
    let r = Solution::str_str(s1.to_string(), s2.to_string());
    assert_eq!(r,correct);
}

#[test]
fn partial_match() {
    let s1 = "hello";
    let s2 = "help";
    let correct = -1;
    let r = Solution::str_str(s1.to_string(), s2.to_string());
    assert_eq!(r,correct);
}



#[test]
fn partial_match_then_match() {
    let s1 = "hellohelp";
    let s2 = "help";
    let correct = 5;
    let r = Solution::str_str(s1.to_string(), s2.to_string());
    assert_eq!(r,correct);
}
