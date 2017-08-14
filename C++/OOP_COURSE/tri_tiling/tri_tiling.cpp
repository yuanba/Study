#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

//define begin
int data[21];
//define end

void init()
{
	memset(data,0,sizeof(data));
	data[0] = 1;
	data[2] = 3;
	for(int i = 4;i <= 20;i += 2)
	{
		data[i] = 4 * data[i-2] - data[i-4];
	}
}

int main()
{
	int n;
	init();
	while(scanf("%d",&n) && n != -1)
	{
		printf("%d\n",data[n]);
	}
	return 0;
}
