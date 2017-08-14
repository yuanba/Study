#include <cstring>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

class Group
{
    protected:
        string name;
        double Baseline;
        double Baseheight;
    public:
        Group(string n,double x,double y):name(n),Baseline(x),Baseheight(y)
        {
            cout << "Create Succeed!" << endl;
        }
        Group(){};
        virtual inline void print()
        {
            cout << name << endl;
        }
        virtual double area() = 0;
};

class T:public Group
{
    protected:
        double a,b,c;
    public:
        T()
        {
            cout << "Three edges of the T!" << endl;
            cin >> a >> b >> c ;
        };
        void print()
        {
            cout << "T!" << endl;
        }
        double area()
        {
            double p = (a + b + c)/2;
            return sqrt(p * (p-a) * (p-b) * (p-c));
        }
};

int main()
{
    Group* a = NULL;// = new Group();
    //a->area();
    a = new T();
    cout << a->area() << endl;
    return 0;
}
