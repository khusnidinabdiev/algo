#include <iostream>
using namespace std;
int main()
{
	double x,y;
	cin>>x>>y;
	if(y<=1 and y>=-1)
	{
		if(x>=0 and x<=1){
			if(1.00/3.00*x-1.00/3.00<=y and y<=0){
				cout<<"yes";}
			else{
				cout<<"no";}}
		if(x>=-1 and x<0){
			if(2*x+3>=y or -x>=y){
				cout<<"yes";}
			else{
				cout<<"no";}}
		if(x>=-2 and x<-1)
		{
			if(2*x+3>=y or 1.00/3.00*x-1.00/3.00<=y){
				cout<<"yes";}
			else
			{
				cout<<"no";
			}
		}
		else
		{
			cout<<"no";
		}
	}
	else
	{
		cout<<"no";
	}
}

