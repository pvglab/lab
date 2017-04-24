#include <iostream>
#include <omp.h>

using namespace std;

int main() {

	int size, arr[20], sep[20], n, key, tid, tid1;
	int left, right, t_left, t_right, interval, index, flag = 0, b_flag = 0, repeat;

	cout << "\nEnter no. of elements: ";		cin >> size;
	cout << "\nEnter elements:\n";
	for(int i=0; i<size; i++)
		cin >> arr[i];
	
	for(int i=0; i<20; i++)
		sep[i] = 0;
		
	cout << "\nEnter element to search: ";		cin >> key;
	cout << "\nEnter no.of threads to create(n): ";	cin >> n;
	
	left = t_left = 0;
	right = t_right = size-1;
	
	if((key>=arr[left]) && (key<=arr[right])) {
		while(t_left <= t_right) {
			
			repeat = 0;
			left = t_left;
			right = t_right;
			interval = (right-left+1)/n;
			
			if(interval == 0) {
				#pragma omp parallel shared(left) private(tid1) num_threads(right-left+1)
				{
					tid1 = omp_get_thread_num();
					if(arr[left+tid1] == key)
						flag = 1;
					b_flag = 1;
				}
			}
			
			else {
				#pragma omp parallel for schedule(static,1) num_threads(n)
				for(int i=0; i<n; i++) {
					if((left+interval*i) > size)
						sep[i] = size-1;
					sep[i] = left+interval*i;
				}
				sep[n] = right+1;
				
				#pragma omp parallel shared(key) private(left,right,tid,index) num_threads(n)
				{
					tid = omp_get_thread_num();
					left = sep[tid];
					right = sep[tid+1]-1;
					index = (left+right)/2;
					
					if(arr[index] == key) {
						cout << "\nElement found by ThreadID: " << tid << " at position: " << index;
					}
					if((key >= arr[left]) && (key <= arr[right])) {
						cout << "\nElement may be between " << left+1 << " and " << right+1;
						t_left = left;
						t_right = right;
						b_flag = 0;
					}
					else {
						repeat++;
					}
				}
			}
			if(repeat == n || b_flag == 1) {
				break;
			}
		}	// while loop ends here
		
		if(flag == 0) {
			cout << "\nElement not present";
		}
	} 
	else {
		cout << "\nElement not found !!!";
	}

	return 0;
}
