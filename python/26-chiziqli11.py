//c++


#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;
int main()
{
	int a;
	double x,y,z;
	cin>>a;
	cin>>x>>y;
	z=sqrt(exp(x*y)-x*sin(a*x)-(x*x+2)/(fabs(x)+5))+sqrt(log(x*x+2)/log(exp(1))+5);
	cout<<fixed<<setprecision(2)<<z;
}