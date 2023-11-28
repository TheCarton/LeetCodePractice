use std::cmp::Ordering;

fn main() {
    println!("Hello, world!");
}
struct Solution;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut sums: Vec<Vec<i32>> = Vec::new();
        let mut nums = nums;
        nums.sort_unstable();
        for left_i in 0..nums.len() - 2 {
            if nums[left_i] > 0 {
                break;
            }
            if left_i > 0 && nums[left_i] == nums[left_i - 1] {
                continue;
            }
            let mut mid_i = left_i + 1;
            let mut right_i = nums.len() - 1;
            while mid_i < right_i {
                let current_sum = nums[left_i] + nums[mid_i] + nums[right_i];
                match current_sum.cmp(&0) {
                    Ordering::Less => {
                        mid_i += 1;
                    }
                    Ordering::Greater => {
                        right_i -= 1;
                    }
                    Ordering::Equal => {
                        sums.push(vec![nums[left_i], nums[mid_i], nums[right_i]]);
                        while mid_i < right_i && nums[mid_i] == nums[mid_i + 1] {
                            mid_i += 1;
                        }
                        while mid_i < right_i && nums[right_i] == nums[right_i - 1] {
                            right_i -= 1;
                        }
                        mid_i += 1;
                        right_i -= 1;
                    }
                }
            }
        }
        sums
    }
}
