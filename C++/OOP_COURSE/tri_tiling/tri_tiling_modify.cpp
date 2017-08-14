#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

class square
{
	public:
		int data[3][3];
		int x_size;
		int y_size;
		square(int a,int b):x_size(a),y_size(b)
	    {
			memset(data,0,sizeof(data));
			if(y_size == 1)
			{
				data[0][0] = 11;
				data[1][0] = 3;
				data[2][0] = 1;
			}
			else
			{
				data[0][0] = 4;   data[0][1] = -1;   data[0][2] = 0;
				data[1][0] = 1;   data[1][1] = 0;    data[1][2] = 0;
				data[2][0] = 0;   data[2][1] = 1;    data[2][2] = 0;
			}
		};
		square operator*(square a)
		{
			square res(3,3);
			for(int i = 0;i<3;i++)
			{
				for(int j = 0;j<3;j++)
				{
					res.data[i][j] = 0;
					for(int k = 0;k<3;k++)
					{
						res.data[i][j] += this->data[i][k] * a.data[k][j];
						res.data[i][j] = res.data[i][j] % 9973;
					}
				}
			}
			return res;
		}
		void set(square a)
		{
			for(int i = 0;i<3;i++)
			{
				for(int j = 0;j<3;j++)
				{
					this->data[i][j] = a.data[i][j];
				}
			}
		}
		void print()
		{
			cout<<"#############"<<endl;
			for(int i = 0;i<3;i++)
			{
				for(int j = 0;j<y_size;j++) cout << data[i][j] <<' ';
				cout << endl;
			}
		}
};

square fast_square(square source,int key)
{
	square cal(3,3);
	cal.data[0][0] = 1;    cal.data[0][1] = 0;    cal.data[0][2] = 0;
	cal.data[1][0] = 0;    cal.data[1][1] = 1;    cal.data[1][2] = 0;
	cal.data[2][0] = 0;    cal.data[2][1] = 0;    cal.data[2][2] = 1;
	while(key)
	{
		if(key & 1) cal.set(cal * source);
		key >>= 1;
		source.set(source * source);
	}
	return cal;
}

int main()
{
	int n;
	while(scanf("%d",&n) && n != -1)
	{
		if(n & 1) cout << 0 << endl;
		else if(n == 0) cout << 1 << endl;
		else if(n == 2) cout << 3 << endl;
		else if(n == 4) cout << 11 << endl;
		else
		{
			square base(3,1);
		//	base.print();
			square trans(3,3);
			//trans.print();
			int key = (n-4)/2;
			square result(3,1);
			square w = fast_square(trans,key);
			//w.print();
			//cout << "key: " << key << endl;
			result.set(w * base);
			//result.print();
                        if(result.data[0][0] < 0) cout << 9973 + result.data[0][0] << endl;
			else cout << result.data[0][0] << endl;
		}
	}
	return 0;
}
