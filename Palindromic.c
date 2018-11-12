/* https://projecteuler.net/problem=4

Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

*/
#include <stdio.h>


int reverseNumber (int n) {         // Function to know thw reverse of a number
	int reverse = 0, i=1;           // Let's initialize (int reverse) as 0 and (int i) as 1
	int nl = n;                     // (int nl) will work as an helper to find (int i) 

	while (nl>10) {                 // while (int nl) it's bigger than 10
		i=i*10;                     // (int i) it's equal to (int i) * 10
		nl=nl/10;                   //  and (nl) it's equal to (nl)/10         
									// ... So, in this case, (int i) it's now 100  
	}

	while(i>0){                          // While (int i) it's bigger than 0
		reverse = reverse + (i*(n%10));  // (reverse) it's equal at reverse plus (int i) times (n%10)
		n=n/10;                          // (n) it's equal to (n)/10
    	i=i/10;                          // (i) it's equal to (i)/10
	}                                    
	return reverse;                      // ... and that's how we discover the reverse
}


int palindromic(int n){                      // Function to find the largest palindrome made from the product of two 3-digit numbers 
	int p=0;                                 // let's initialize (int p) as 0

	for(n; n>99; n--){                       // Now, let's initialize a cicle 'for' that takes (int n '999'), and will decrement till n>99
		for(int m=n; m>99; m--){             // (int m) it's equal to (int n) and we will do the same thing
			if((m*n)==reverseNumber(m*n)){   // If the product of m&n it's equal to the reverse number of n&m...
				if((m*n)>p){                 // ... and if the producto of n&m it's bigger than (int p)...
					p=(m*n);                 // (int p) it's now (m*n)
				}
			}
		}
	}
	return p;                                // After the two cicles 'for', return the value of p 
}


void main () {
	printf("This is the largest palindrome made from the product of two 3-digit numbers: %d\n", palindromic(999)); 

}
