#include <iostream>
using namespace std;

#define target 100000
#define modulus 1000000

static int sums[target + 1] = {0};

int main(void) {
	sums[0] = 1;
	for (int i = 1; i < target; ++i) {
		for (int j = i; j < target + 1; ++j) {
			sums[j] = (sums[j] + sums[j-i]) % modulus;
		}
	}
	for (int i = 0; i < target + 1; ++i) {
		if (sums[i] == 0) {
			cout << "n = " << i << ", p(n) = " << sums[i] << endl;
			break;
		}
	}
	return 0;
}

