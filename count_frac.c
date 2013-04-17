#include <stdio.h>
#define limit 1000000
int main(void) {
	long long int count = 0;
	int phi[limit + 1];
	int i = 0, j = 0;
	for (i = 0; i < limit + 1; ++i) {
		phi[i] = i;
	}
	for (i = 2; i < limit + 1; ++i) {
		if (phi[i] == i) {
			for (j = i; j < limit + 1; j += i) {
				phi[j] = phi[j] / i * (i - 1);
			}
		}
		count += phi[i];
	}
	printf("%lld\n", count);
}
