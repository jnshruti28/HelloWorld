number = int(input("Write a Number = "))
c=0
for i in range (1,number+1):
  if(number%i==0):
    c = c+1
if(c==2):
  print("The number is PRIME")
else:
  print("The number is COMPOSITE ") 
