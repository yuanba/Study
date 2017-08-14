#include<iostream>
#include"stack.h"

using namespace std;

int main()
{
	mystack test;
	for(int i = 1;i <= 20;i++)
	{
		test.push(i);
	}
	cout<<test.top()<<endl;
	cout<<test.get_size()<<endl;
	for(int i = 1;i <= 30;i++)
	{
		test.pop();
	}
	cout<<test.get_size()<<endl;
	return 0;
}
