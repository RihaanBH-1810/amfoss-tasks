package main

import("fmt")

func main(){
	var num,i,j int 

	fmt.Scanln(&num)
	fmt.Print(2)
	for i = 2; i<num+1; i++{
		for j = 2 ; j<=i; j++{
			if i%j == 0 {
				break
			}else{
				fmt.Print(" ",i)
				break
			}
		}
	}
}



