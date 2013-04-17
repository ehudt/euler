// problem 125
// correct solution in 40m :(
#include <iostream>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <string>
using namespace std;

const int limit = 100000000;
const int sqrt_limit = 10000;

static int squares[sqrt_limit + 1] = {0};

bool check(int n);
bool is_palindrome(int n);
bool sum_consecutive_squares(int n);

int main(void) {
	for (int i = 0; i < sqrt_limit + 1; ++i) {
		squares[i] = i*i;
	}
	long long int sum = 0;
	for (int i = 0; i < limit; ++i) {
		//cout << i << endl;
		if (check(i)) {
			sum += i;
		}
	}
	cout << sum << endl;
	return 0;
}

bool sum_consecutive_squares(int n) {
	for (int biggest = sqrt(n) + 1; biggest > 1; --biggest) {
		for (int series = 2; series < biggest; ++series) {
			int series_sum = 0;
			for (int i = biggest - series; i < biggest; ++i) {
				series_sum += squares[i];
			}
			if (series_sum > n) break;
			if (series_sum == n) return true;
		}
	}
	return false;
}

bool is_palindrome(int n) {
	int m = n, r = 0;
	while (m) {
		r = r*10 + m%10;
		m /= 10;
	}
	return n == r;
}

bool check(int n) {
	return is_palindrome(n) && sum_consecutive_squares(n);
}