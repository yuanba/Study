#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

class complexe
{
    private:
        int a,b;
    public:
        complexe()
        {
            a = b = 0;
        }
        complexe(int x,int y):a(x),b(y){}
        void operator=(complexe k)
        {
            this->a = k.a;
            this->b = k.b;
        }
        complexe& operator++()
        {
            this->a++;
            return *this;
        }
        complexe operator++(int x)
        {
            complexe k(this->a,this->b);
            this->a++;
            return k;
        }
        complexe& operator+(complexe k)
        {
            this->a += k.a;
            this->b += k.b;
            return *this;
        }
        friend istream& operator>>(istream& in,complexe& k)
        {
            in >> k.a >> k.b;
            return in;
        }
        friend ostream& operator<<(ostream& out,complexe& k)
        {
            out << k.a << " + " << k.b << "*i" <<endl;
            return out;
        }
};

int main()
{
    complexe x;
    complexe y;
    cin >> x >> y;
    cout << x << y;
    complexe w;
    w = x++;
    cout << w <<endl;
    w = ++x;
    cout << w <<endl;
    w = x + y;
    cout << w<< endl;
    //cout << ++x <<endl;
    //cout << x+y <<endl;
    return 0;
}
