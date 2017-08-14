#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

class some
{
	private:
		double a,b,c;
		int size ;
	public:
		inline some()
		{
			size = 0;
			a = b = c = 1;
		}
		inline some(double x,double y,double z):a(x),b(y),c(z)
		{
			size = 0;
		}
		/*inline some(double x,double y,double z=1)
		{
			size = 0;
		}
		inline some(double x,double y=1,double z=1)
		{
			size = 0;
		}*/
		inline double* get_result()
		{
			double* result = new double(2);
			if(a == 0) 
			{
				size = 1;
				result[0] = -c/b;
				return result;
			}			
			double key = b*b - 4*a*c;
			if(key < 0) return NULL;
			else if(key == 0) size = 1,result[0] = -b/2/a;
			else 
			{
				size = 2;
				result[0] = (-b+sqrt(key))/2/a;
				result[1] = (-b-sqrt(key))/2/a;
			}
			return result;
		}
		inline void set(double a,double b,double c){this->a = a;this->b = b;this->c = c;}
		inline double get_a(){return a;}
		inline double get_b(){return b;}
		inline double get_c(){return c;}		
		inline int get_number_result()
		{
			return size;
		}
		some& add(some& a,some& bb)
		{
			double newa = this->a+a.get_a();
			double newb = this->b+a.get_b();
			double newc = this->c+a.get_c();
			bb.set(newa,newb,newc);
			return bb;
		}
};

int main()
{
	double x,y,z;
	scanf("%lf%lf%lf",&x,&y,&z);
	some a(x,y,z);
	//cout<<a.get_a()<<a.get_b()<<a.get_c()<<endl;	
	/*some b;
	some c(0,2,0);
	b = a.add(c,b);
	double* result = b.get_result();
	int answer = b.get_number_result();
	cout<<answer<<"#"<<endl;
	cout << b.get_a() << b.get_b() << b.get_c() <<endl;	
	for(int i=0;i<answer;i++)
	{
		cout<<result[i]<<endl;
	}*/
	double* result = a.get_result();
	int answer = a.get_number_result();
	for(int i=0;i<answer;i++)
	{
		cout<<result[i]<<endl;
	}
	return 0;
}
