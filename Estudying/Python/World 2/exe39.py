import datetime
year  = int(input("Enter a Year: "))
#age
actuallyYear = datetime.date.today().year
ageActually = actuallyYear - year
print(ageActually)

if ageActually < 18:
  
