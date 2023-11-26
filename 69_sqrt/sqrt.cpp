class Solution {
public:
  int mySqrt(int x) {
    if (x <= 1) {
      return x;
    }
    int low = 1;
    int high = x / 2;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      // mid * mid = x
      // mid = x / mid
      if (mid < x / mid) {
        low = mid + 1;
      } else if (mid > x / mid) {
        high = mid - 1;
      } else {
        return mid;
      }
    }
    return high;
  }
};
