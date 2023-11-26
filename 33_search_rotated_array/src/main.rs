fn main() {
    let _a = vec![1, 2, 4, 6, 54];
}
struct Solution;
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left < right {
            let mid = (left + right) / 2;
            if nums[mid] > nums[right] {
                // 5, 6, 7, 8, 1, 2, 3
                left = mid + 1;
            } else {
                // 10, 11, 1, 2, 3
                right = mid;
            }
        }
        let start = left;
        left = 0;
        right = nums.len() - 1;

        if target >= nums[left] && target <= nums[right] {
            left = start;
        } else {
            right = start;
        }

        while left <= right {
            let mid = (left + right) / 2;
            println!("left = {}, right = {}, mid = {}", left, right, mid);
            match nums[mid].cmp(&target) {
                std::cmp::Ordering::Equal => return mid as i32,
                std::cmp::Ordering::Less => left = mid + 1,
                std::cmp::Ordering::Greater => right = mid - 1,
            }
        }

        -1
    }
}

#[test]
fn example_1() {
    let a = vec![4, 5, 6, 7, 0, 1, 2];
    let r = Solution::search(a, 1);
    assert_eq!(r, 5);
}
