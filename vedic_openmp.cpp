#include <iostream>
#include <omp.h>

using namespace std;

int main() {
	
	int num;
	int d, s, sum=0, ans, s1, s2;
	
	cout << "\nEnter a two digit no. to find square: ";		cin >> num;
	
	#pragma omp parallel num_threads(2)
	{
		if(omp_get_thread_num() == 0) {
			cout << "\nTotal threads created: " << omp_get_num_threads();
			cout << "\nThread " << omp_get_thread_num() << " is executing.";
		}
	
		#pragma omp taskwait
		{
			if(omp_get_thread_num() == 1) {
				cout << "\nThread 1 is executing.";
				
				d = num-10;
				s = d*d;
				sum = num+d;
			
				if(s/10 == 0) {
					ans = sum*10 + s;
				} else {
					s1 = s/10;
					sum = sum+s1;
					s2 = s%10;
					ans = sum*10 + s2;
				}
			}
		}
	}
	
	cout << "\nSquare of " << num << " is " << ans <<endl;
	return 0;
}
