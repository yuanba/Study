#include<iostream>
#include"test.h"

using namespace std;

template<typename T>
T test<T>::get()
{
	return number;
}

template<typename T>
void test<T>::set(T a)
{
	number = a;
}
