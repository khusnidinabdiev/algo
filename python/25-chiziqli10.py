//c++


#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
	int a;
	double x,t;
	cin>>a;
	cin>>x;
	t=(sqrt(x-1)+sqrt(x+2)+log(x*sqrt(a)+2)/log(10))/sqrt(sqrt(x+2)+sqrt(x+24)+pow(x,5));
	cout<<fixed<<setprecision(2)<<t;
}