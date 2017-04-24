#include <stdio.h> 
#include <omp.h> 
int sharedMemory=0; 

void readMemory(int threadID) 
{ 
	printf("THREAD: %d \t SHARED MEMORY: %d\n",threadID,sharedMemory); 
} 

void writeMemory(int threadID) 
{ 
	//int tid2;
	readMemory(threadID);
	#pragma omp critical 
	{ 
		//tid2=omp_get_thread_num();
		printf("\nCritical section updated by %d\n",threadID);
		sharedMemory++; 
	}  
	readMemory(threadID); 
} 


void writeMemoryLocks(int threadID) 
{ 
	
	static omp_lock_t lock; 
	readMemory(threadID); 
	omp_init_lock(&lock);
	int tid3;
	tid3=omp_get_thread_num();
	omp_set_lock(&lock);	
	sharedMemory++; 
	printf("\nCritical section updated by %d\n",threadID);
	omp_unset_lock(&lock);
	omp_destroy_lock(&lock); 
	readMemory(threadID); 
}
 
int main() 
{ 
	int choice;
	printf("\nMENU\n1. CRITICAL DIRECTIVE\n2. LOCKS\nENTER YOUR CHOICE ===> "); 
	scanf("%d",&choice); 
	omp_set_num_threads(8); 
	#pragma omp parallel shared(sharedMemory) 
	{ 
		if((omp_get_thread_num()%2) == 0) 
		{ 
			//even threads reader threads 
			readMemory(omp_get_thread_num()); 
		} 
		else 
		{ 
			//odd threads writer threads 
			if(choice == 1) 
				writeMemory(omp_get_thread_num()); 
			if(choice == 2) 
			writeMemoryLocks(omp_get_thread_num()); 
		} 
	} 
	return 0; 
}

/*
OUTPUT:
admin@admin-Lenovo-Z51-70:~/Music$ g++ -fopenmp h1.cpp
admin@admin-Lenovo-Z51-70:~/Music$ ./a.out

MENU
1. CRITICAL DIRECTIVE
2. LOCKS
ENTER YOUR CHOICE ===> 1
THREAD: 1 	 SHARED MEMORY: 0

Critical section updated by 1
THREAD: 1 	 SHARED MEMORY: 1
THREAD: 3 	 SHARED MEMORY: 0

Critical section updated by 3
THREAD: 3 	 SHARED MEMORY: 2
THREAD: 4 	 SHARED MEMORY: 0
THREAD: 5 	 SHARED MEMORY: 0

Critical section updated by 5
THREAD: 5 	 SHARED MEMORY: 3
THREAD: 6 	 SHARED MEMORY: 0
THREAD: 7 	 SHARED MEMORY: 0
Critical section updated by 7
THREAD: 7 	 SHARED MEMORY: 4
THREAD: 0 	 SHARED MEMORY: 0
THREAD: 2 	 SHARED MEMORY: 0
admin@admin-Lenovo-Z51-70:~/Music$ ./a.out

MENU
1. CRITICAL DIRECTIVE
2. LOCKS
ENTER YOUR CHOICE ===> 2
THREAD: 2 	 SHARED MEMORY: 0
THREAD: 0 	 SHARED MEMORY: 0
THREAD: 1 	 SHARED MEMORY: 0
THREAD: 5 	 SHARED MEMORY: 0

Critical section updated by 5
THREAD: 3 	 SHARED MEMORY: 0

Critical section updated by 3
THREAD: 3 	 SHARED MEMORY: 3

Critical section updated by 1
THREAD: 1 	 SHARED MEMORY: 3
THREAD: 5 	 SHARED MEMORY: 2
THREAD: 4 	 SHARED MEMORY: 0
THREAD: 7 	 SHARED MEMORY: 0

Critical section updated by 7
THREAD: 7 	 SHARED MEMORY: 4
THREAD: 6 	 SHARED MEMORY: 0
admin@admin-Lenovo-Z51-70:~/Music$ 

*/
