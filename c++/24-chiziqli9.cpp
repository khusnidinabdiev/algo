#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main()
{
	int a,b,c;
	double x,w;
	cin>>a>>b>>c;
	cin>>x;
	w=0.75+(8.2*x*x+sqrt(fabs(x*x*x+3*x)+cos(x-2)))/(a/4.+b/3.+c/2.+1);
	cout<<fixed<<setprecision(2)<<w;
}
