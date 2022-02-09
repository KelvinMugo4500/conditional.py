#Decision making
salary = int(input("Enter salary:"))
years = int(input("Enter years of service:"))
if years > 10:
  print("Net bonus is", 0.01*salary)
elif years >=6 and years <=10:
    print("Net bonus is", 0.08*salary)
else :
    print("Net bonus is", 0.05*salary)
