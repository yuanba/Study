#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

class pusherror
{};

class dynamic_str
{
	private:
		vector<char> data;
	public:
		dynamic_str();
		dynamic_str(char*);
		dynamic_str& append(char);
		dynamic_str* append(const char*);
		int size();
		void clear();
		void insert(int , char);
		inline void print()
		{
			for(vector<char>::iterator iter = data.begin();iter != data.end();iter++) cout << *iter ;
			cout << endl;
		}
};

dynamic_str::dynamic_str()
{
	data.clear();
	cout << "Create succeed!" << endl;
}

dynamic_str::dynamic_str(char* something)
{
	for(int i = 0;i <= strlen(something);i++) data.push_back(something[i]);
	cout << "Create succeed!" << endl;
}

dynamic_str& dynamic_str::append(char s)
{
	data.push_back(s);
	return *this;
}

dynamic_str* dynamic_str::append(const char* something)
{
	for(int i = 0;i <= strlen(something);i++) data.push_back(something[i]);
	return this;
}

void dynamic_str::clear()
{
	data.clear();
}

int dynamic_str::size()
{
	return data.size();
}

void dynamic_str::insert(int position , char s)
{
	try
	{
		if(position >= data.size()) throw pusherror();
		else data.insert(data.begin() + position,s);
	}
	catch(pusherror e)
	{
		cout << "Try to insert a wrong position!" << endl;
	}
}

int main()
{
	dynamic_str test_one;
	dynamic_str test_two("lantian");
	for(int i = 1;i <= 5;i++) test_one.append('s');
	for(int i = 1;i <= 1;i++) test_two.append("GMFTBY");
	cout << test_one.size() << endl;
	test_one.clear();
	cout << test_one.size() << endl;
	test_two.print();
	test_two.insert(2,'?');
	test_two.print();
	cout << test_two.size() << endl;
	dynamic_str& a = test_one.append('a');
	a.print();
	return 0;
}
