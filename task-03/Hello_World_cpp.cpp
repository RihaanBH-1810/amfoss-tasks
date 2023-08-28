#include<iostream>
using namespace std;

int number;
int main(){
    cin>>number;
    if(number <=1 ){
        exit(0);
    }
    cout<<2<<" ";
    for(int i=2;i<number+1;i++){
        for(int j=2;j<=i;j++){
            if(i%j == 0){
                break;
                }
            cout<<i<<" ";
            break;
                }
            }
        
    return 0;
    }