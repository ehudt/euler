// problem 187
#include <iostream>
using namespace std;

#define limit 100000000

int part(int n, int p) {
	int count = 0;
	int q = p;
	while (n % q == 0) {
		q *= p;
		count++;
	}
	return count;
}

static int factors[limit] = {0};

int main(void) {
	factors[1] = 1;
	int count = 0;
	for (int i = 2; i < limit; ++i) {
		if (factors[i] == 0) {
			for (int j = i; j < limit; j += i) {
				factors[j] += part(j, i);
			}
		}
		if (factors[i] == 2) count++;
	}
	cout << count << endl;
	return 0;
}
