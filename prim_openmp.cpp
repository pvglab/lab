#include <iostream>
#include <omp.h>

using namespace std;

void setvis(int d, int vis[]) {
	vis[d] = d;
	cout << d;
}

int chkvis(int d, int vis[]) {
	if(vis[d] == d)
		return 1;
	else
		return 0;
}

int main() {
	
	int v, a[10][10], vis[10];
	
	cout << "\nEnter no. of vertices: ";		cin >> v;
	
	for(int i=0; i<10; i++) {
		for(int j=0; j<10; j++) {
			a[i][j] = 99;
		}
		vis[i] = -1;
	}
	
	cout << "\nStart entering distances: \n";
	
	
	for(int i=0; i<v; i++) {
		for(int j=i+1; j<v; j++) {
			cout << "Enter cost b/w Node: " << i << " and Node: " << j << " : ";
			cin >> a[i][j];
			if(a[i][j] == 0) {
				a[i][j] = 99;
			}
			a[j][i] = a[i][j];
		}
	}
	
	cout << "\n\nEntered cost matrix is: ";
	for(int i=0; i<v; i++) {
		cout << endl;
		for(int j=0; j<v; j++)
			cout << a[i][j] << "\t";
	} 
	cout << endl;
	
	int min = 99, k, l;	
	for(int i=0; i<v; i++) {
		for(int j=0; j<v; j++) {
			if(a[i][j] < min) {
				min = a[i][j];
				k = i;
				l = j;
			}		
		}
	}
	cout << endl;
	setvis(k, vis);
	cout << "---";
	setvis(l, vis);
	cout << " : " << min << endl;
	
	
	int total = min;
	for(int m=0; m<v-2; m++) {
		min = 99;
		int tid;
		
		#pragma omp parallel private(tid) num_threads(v) 
		{
			tid = omp_get_thread_num();
			
			if(chkvis(tid, vis) == 1) {
				for(int j=0; j<v; j++) {
					if(chkvis(j, vis) == 0) {
						if(a[tid][j] < min) {
							min = a[tid][j];
							k = tid;
							l = j;
						}
					}
				}
			}
		}		
		setvis(k, vis);
		cout << "---";
		setvis(l, vis);
		cout << " : " << min << endl;
		total += min;
	}
	cout << "\nTotal: " << total << endl;	

	return 0;
}
