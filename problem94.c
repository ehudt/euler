#include <stdio.h>

const long long limit = 1000000000ll;

int main(void) {
  long long sum = 0;
  long long x, y;
  for (x = 1; x <= limit; ++x) {
    for (y = x - 1; y <= x + 1; y += 2) {
      const long long perimeter = x + x + y;
      if (perimeter > limit) {
        x = limit + 1;
        break;
      }
      const long long h2 = x * x - y * y / 4;
      if (y % 2 == 0 || h2 % 4 == 0) {
        sum += perimeter;
      }
    }
  }
  
  printf("%lld\n", sum);
  return 0;
}