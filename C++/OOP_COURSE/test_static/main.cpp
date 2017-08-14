#include<iostream>
#include"test.h"

using namespace std;

int main()
{
	test* pa = NULL;
 	pa = new test[100];
	cout<<pa->get()<<endl;
	//cout<<pa->number<<endl;
	cout<<test::number<<endl;  
	return 0;
}
