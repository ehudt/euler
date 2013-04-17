/* problem 75  - bad solution*/
#include <iostream>
#include <math.h>
using namespace std;

#define limit 1500000

int tries[limit + 1] = {0};

int main(void) {
	for (int i = 1; i < limit / 3; ++i) {
		for (int j = i; j < limit / 3 + 1; ++j) {
			int kk = i*i + j*j;
			int k = sqrt(kk);
			if (kk == k*k && i+j+k <= limit) {
				tries[i+j+k]++;
			}
		}
	}
	int count = 0;
	for (int i = 0; i < limit + 1; ++i) {
		if (tries[i] == 1) count++;
	}
	cout << count << endl;
	return 0;
}

