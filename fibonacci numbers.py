#python program to generate fibonacci series until 'n' value
n = int(input("enter the value of 'n':"))
a = 0
b = 1
sum = 0
count = 1
print("fibonacci series:", end =" ")
while(count <=n):
  print(sum, end =" ")
  count +=1
  a = b
  b = sum
  sum = a+b