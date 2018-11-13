/* https://projecteuler.net/problem=3

Largest prime factor
Problem 3


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

*/
#include <stdio.h>

/* int BiggerPrime(int n){  //This function is not what we want. This one gives the bigger Prime from 2 to (int n)
	int i = 2;

	while (n>0 && i<n){
		if(n%i==0){
			n--;
			i=2;
		}
		else {i++;}
	}
	return n;
} */




int Lprime (int n){        // This function gives the largest prime factor 
	int i=2;               // let's strar the (int i) as 2

	while (n>1 && i<n){    // while (int n) it's bigger than 1 and (int i) it's less than (n)
		if (n%i==0) {      // if (n%i) it's equal to 0
			n=n/i;         // (n) iquals n/i
		}
		else {i++;}        // or else increment (i)
	}
	return n;              // return (n)
}

/*Since i have this warning:

"warning: overflow in implicit constant conversion [-Woverflow]
  printf("\nThe largest prime is: %d\n", Lprime(600851475143));"

  I decided to try it on Matlab/Octave
*/

void main () {

	printf("\nThe largest prime is: %d\n", Lprime(600851475143)); //6857
}
