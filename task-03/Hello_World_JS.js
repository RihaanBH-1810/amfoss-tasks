var number = prompt();
if(number > 1){
    console.log(2);
    for (var i = 2; i <= number; i++) {
        for (var j = 2; j < i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
            console.log(i);
            break;
        }
    }
}
