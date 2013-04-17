/* priblem 75 - bad solution */

#include <stdio.h>
#include <assert.h>
#include <math.h>

#define max(a,b)	((a) > (b) ? (a) : (b))

int count_triangles(int n) {
	int i, j, count = 0;
	if (n < 3) return 0;
	for (i = max(1, (-1+sqrt(1+4*n))/2); i < n / 3; ++i) {
		int t = n - i;
		int ii = i*i;
		int k = ( ii + t*t ) / (2 * t);
		//printf("n = %d, i = %d, d = %lf\n", n, i, d);
		//if (f != truncf(f)) continue;
		//int k = (int) f;
		int j = t - k;
		if (ii + j*j == k*k) count++;
	}
	return count;
}

int main(void) {
	int l, count = 0;
	for (l = 4; l <= 50; l += 2) {
		if (count_triangles(l) == 1) {
			count++;
			//printf("%d\n", l);
		}
	}
	/*for (l = 4; l <= 120; l += 2) {
		printf("%d cm : %d triangles\n", l, count_triangles(l));
	}*/
	printf("%d\n", count);
	return 0;
}
