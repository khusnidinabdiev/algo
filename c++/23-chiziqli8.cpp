#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
	int a,b,c,d;
	float x,f;
	cin>>a>>b>>c>>d;
	cin>>x;
	f=(a*x*x+b*x+c)/(x*a*a*a+a*a+pow(a,b-c))+cos(fabs((a*x+b)/(x*c+d+pow(2,c))));
	cout<<fixed<<setprecision(2)<<f;
}
