fn main() {
    println!("Hello, world!");
}
struct Solution;
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

use std::collections::VecDeque;
impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut node = head.clone();
        let mut window: VecDeque<&mut Option<Box<ListNode>>> =
            VecDeque::with_capacity(n as usize + 1);
        let mut len = 0;
        while node.is_some() {
            len += 1;
            if len > n + 1 {
                window.pop_front();
            }
            let addr = &mut node;
            window.push_back(addr);
            let mut node = node.next;
        }
        // [a, b, c, d, e]
        // remove 2
        // [a, b, c, e]
        // index of d is 3 = 5 - 2

        return head;
    }
}
