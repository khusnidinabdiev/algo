#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
	int a;
	double x,s;
	cin>>a;
	cin>>x;
	s=x*sin(x/2+x/3+x/4)+(log(x*x-2)/log(10)+pow(3,a))/(cos(x+3)*sin(x+3)+8);
	cout<<fixed<<setprecision(2)<<s;
}
