/* problem 145 */

#include <stdio.h>

#define false	(0)
#define true	(!false)

const int limit = 1000000000;

int reverse(int n) {
	int m = 0;
	while(n) {
		m = m*10 + n%10;
		n /= 10;
	}
	return m;
}

bool odd_digits(int n) {
	while (n) {
		if (n % 2 == 0) return false;
		n /= 10;
	}
	return true;
}


int main(void) {
	int i = 0;
	int count = 0;
	for (i = 0; i < limit; ++i) {
		if (i%10 == 0) continue;
		if (odd_digits(i + reverse(i))) count++;
	}
	printf("%d\n", count);
	return 0;
}