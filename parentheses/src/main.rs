fn main() {
    println!("{:?}", Solution::generate_parenthesis(3));
    println!("{:?}", Solution::generate_parenthesis(1));
}

struct Solution;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut parens = vec![];
        Self::dfs(0, 0, "".to_string(), &mut parens, n);
        parens
    }
    fn dfs(left: usize, right: usize, s: String, parens: &mut Vec<String>, n: i32) {
        if s.len() == (n * 2) as usize {
            parens.push(s.to_owned());
        }

        if left < n as usize {
            let mut new_s = s.clone();
            new_s.push('(');
            Self::dfs(left + 1, right, new_s, parens, n);
        }
        if right < left {
            let mut new_s = s;
            new_s.push(')');
            Self::dfs(left, right + 1, new_s, parens, n);
        }
    }
}
