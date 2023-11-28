use std::cmp;

fn main() {
    println!("Hello, world!");
}
struct Solution();

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = height.len() - 1;
        let mut area = 0;
        while i < j {
            area = cmp::max(area, (j - i) as i32 * cmp::min(height[i], height[j]));
            if height[i] < height[j] {
                i += 1;
            } else {
                j -= 1;
            }
        }
        area
    }
}

#[test]
fn one_two() {
    let bars = vec![1, 2];
    let correct = 1;
    let r = Solution::max_area(bars);
    assert_eq!(r, correct);
}
