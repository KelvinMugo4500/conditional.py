#Conditional statements
a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
c= int(input("Enter a number:"))
if  a>b and a>c:
  print("Return the largest number",a)
if  b>a and b>c:
  print("Return the largest number",b)
if  c>a and c>b:
  print("Return the largest number",c)