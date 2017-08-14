#include<iostream>
#include"test.cpp"

using namespace std;

int main()
{
	test<float> a;
	a.set(3.1);
	cout<<a.get()<<endl;
	return 0;
}
