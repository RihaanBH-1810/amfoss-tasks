import java.util.*;
class Main{
    public static void main(String[] args) {
       int num;
       Scanner sc = new Scanner(System.in);
       num = sc.nextInt();
       if(num <=1){
        System.exit(0);
       }
       System.out.print(2 + " ");
       for(int i = 2;i < num+1;i++){
        for(int j = 2;j < i;j++){
            if(i%j == 0){
                break;
            }else{
                System.out.print(i + " ");
                break;
            }

        }
       }
    }
}