#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;
int main()
{
	int x;
	double y,z,f;
	cin>>x;
	cin>>y>>z;
	f=pow(2,-x)*sqrt(x+pow(fabs(y)+2,1./4.))*pow(exp(x-1)/sin(z+2)+2,1./3.);
	cout<<fixed<<setprecision(2)<<f;
}
