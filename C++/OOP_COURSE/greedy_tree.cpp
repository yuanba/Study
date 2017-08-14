#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

//define begin
int map[1505][1505];
int degree[1505];
int stack[1505];
int size = 0;
int number;
int result;
//define end

void init(int x)
{
	memset(map,0,sizeof(map));
	memset(degree,0,sizeof(degree));
	size = 0;
	result = 0;
}

int main()
{
	while(scanf("%d",&number) != EOF)
	{
		init(number);
		for(int i = 0;i < number;i++)
		{
			int x,y,nedge;
			scanf("%d:(%d)",&x,&nedge);
			degree[x] += nedge;
			while(nedge--)
			{
				scanf("%d",&y);
				map[x][y] = map[y][x] = 1;
				degree[y] ++;
			}
		}

		for(int i = 0;i < number;i++) if(degree[i] == 1) stack[++size] = i;

		while(size)
		{
			int now = stack[size];
			int father = 0;
			size --;
			if(degree[now] == 0) continue;
			for(int i = 0;i < number;i++)
			{
				if(map[now][i] == 1)
				{
					result ++;
					father = i;
					break;
				}
			}
			for(int i = 0;i < number;i++)
			{
				if(map[father][i] == 1)
				{
					degree[father] --;
					degree[i] --;
					map[father][i] = map[i][father] = 0;
					if(degree[i] == 1) stack[++size] = i;
				}
			}
		}

		cout << result << endl; 
	}
	return 0;
}
