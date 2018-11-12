/* https://projecteuler.net/problem=1

Multiples of 3 and 5
Problem 1 



If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <stdio.h>

int m35(int n){                 

int s=0, i=0;                   // (int s) will be the sum of the multiples of 3 & 5. For now, let's initialize at 0. (int i) will be and index number

	while(i<n){                 // while (int i) it's less than (int n), in this case 1000
		if (i%3==0 || i%5==0){  // if (i) is multiple of 3 or (i) is multiple of 5...
			s=s+i;              // ... (int s) will be the sum of the previous (s) with (i)
			i++;                // ... increment (int i)
		}
		else { i++;}            // if (i) isn't multiple of 3 or 5, increment (i)
	}
	return s;                   // after the cicle 'while', return (int s), the sum of all the multiples of 3 or 5 below 1000
}

void main () {
	printf("The sum of all the multiples of 3 or 5 below 1000 is: %d\n", m35(1000));
}
