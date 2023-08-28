#include <stdio.h>

int main() {
    int number;
    scanf("%d",&number);
    if(number<=1){
        exit(0);
    }
    printf("%d",2);
    for(int i=2;i<number+1;i++){
        for(int j=2;j<=i;j++){
            if(i%j == 0){
                break;
            }
            else{
                printf(" %d",i);
                break;
            }
        }
    }
    

    return 0;
}