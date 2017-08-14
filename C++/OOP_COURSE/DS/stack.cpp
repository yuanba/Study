#include"./stack.h"
#include<iostream>

using namespace std;

mystack::mystack()
{
	size = 0;
	data = new int[100000];
	volume = 100000;
	//cout<<"Succeed to create 100 data"<<endl<<"if you want to use more"<<endl<<"just do it ,we will dynamic to add 100 a time"<<endl;
}

mystack::~mystack()
{
	size = 0;
 	delete[] data;
	data = NULL;
	cout<<"Destory succeed!"<<endl;
}

void mystack::pop()
{
	try
	{
		if(get_size() == 0) throw emptyerror();
		else size -= 1;
	}
	catch(emptyerror e)
	{
		cout<<"try to pop the empty stack!"<<endl;
	}
}

void mystack::push(int x)
{
	try
	{
		if(size >= volume) throw fullerror();
		else data[++size] = x;
	}
	catch(fullerror e)
	{
		cout<<"try to push element into the full stack!"<<endl;
	}
}

int mystack::top()
{
	return data[get_size() - 1];	
}
