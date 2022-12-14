// c++

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
	z=sqrt(y*y+exp(x)+sqrt(exp(x)+a/(x*x+2))+pow(cos(x),2)/sin(x*x))+pow(cos(x),3);
	cout<<fixed<<setprecision(2)<<z;
}