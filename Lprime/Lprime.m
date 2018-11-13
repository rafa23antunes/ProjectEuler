
i=2;
n=600851475143;

while (n>1 && i<n) 
  if (mod(n,i)==0)
    n=n/i;
  else
    i=i+1;
  endif
end
n

