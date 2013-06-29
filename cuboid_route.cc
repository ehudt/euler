// Problem 86

#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
  int M = 1817;
  double epsilon = 1e-9;
  int count = 0;
  for (int j = 1; j <= M; ++j) {
    for (int k = j; k <= M; ++k) {
      for (int l = k; l <= M; ++l) {
        double path = sqrt((j+k)*(j+k) + l*l);
        if (path - int(path) < epsilon) {
          count++;
        }
      }
    }
  }
  cout << count << endl;
  return 0;
}