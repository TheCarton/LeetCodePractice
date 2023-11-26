use std::collections::BTreeMap;
fn main() {
    println!("Hello, world!");
}
struct Solution();

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut sums: Vec<Vec<i32>> = Vec::new();
        let mut tree: BTreeMap<i32, usize> = BTreeMap::new();
        for x in nums.iter() {
            if let Some(e) = tree.get_mut(x) {
                *e += 1;
            } else {
                tree.insert(*x, 1);
            }
        }
        for (i, x) in nums.iter().enumerate() {
            for (j, y) in nums.iter().enumerate() {
                if i == j {
                    continue;
                }
                let complement = -(*x + *y);
                if let Some(num_comp) = tree.get(&complement) {
                    if !Self::check_duplicates(complement, *num_comp, *x, *y) {
                        continue;
                    }
                    let mut three_sum = vec![*x, *y, complement];
                    three_sum.sort_unstable();
                    if Self::unique_three_sum(&three_sum, &sums) {
                        sums.push(three_sum);
                    }
                }
            }
        }
        sums
    }

    fn check_duplicates(comp: i32, num_comp: usize, a: i32, b: i32) -> bool {
        if comp == a && a == b {
            return num_comp >= 3;
        }
        if num_comp == 1 {
            return comp != a && comp != b;
        }
        true
    }

    fn unique_three_sum(three_sum: &[i32], sums: &[Vec<i32>]) -> bool {
        let mut unique = true;
        for sum in sums.iter() {
            unique &=
                (three_sum[0] != sum[0]) || (three_sum[1] != sum[1]) || (three_sum[2] != sum[2]);
            if !unique {
                println!("{:?} == {:?}", sum, three_sum);
                return false;
            }
        }
        true
    }
}

fn three_sums_eq(a_sums: &[Vec<i32>], b_sums: &[Vec<i32>]) -> bool {
    if a_sums.len() != b_sums.len() {
        return false;
    }
    let mut same = true;
    for a_sum in a_sums.iter() {
        for b_sum in b_sums.iter() {
            for (a, b) in a_sum.iter().zip(b_sum.iter()) {
                same &= a == b;
            }
        }
    }
    same
}

#[test]
fn happy() {
    let nums = vec![-1, 0, 1, 2, -1, -4];
    let correct = vec![vec![-1, -1, 2], vec![-1, 0, 1]];
    let r = Solution::three_sum(nums);
    assert!(
        three_sums_eq(&r, &correct),
        "vectors are not equal. Expected {:?}, got {:?}",
        r,
        correct
    );
}
