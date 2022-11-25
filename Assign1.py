#Name: Het Patel
#Program: Inflation rate calculation 
#Date: October 5th, 2022
#Program Descripiton: This program simply inputs certain expenses listed by the user, and outputs the inflation rate while showing the type 

sumCurrentYear=0
sumPreviousYear=0
count=0

# The line inputs the year the user wnats to calculate the personal intrest 
year=int(input("Please enter the year that you want to calculate the personal interest: "))
# The line inputs the number of expenses (categories) the user wants to use for calculating the inflation rate  
numCategories=int(input("Please enter the number of expenditure categories: "))

# This countCategories while loop simply increments and sums the number of categories from the previous year and current year. Depending on the number of categories the user types, the sum will respectively add.  
while count<numCategories:
  expensesPreviousYear=float(input("Please enter expenses for previous year: "))       
  expensesCurrentYear=float(input("Please enter expenses for year of interest: "))
  sumCurrentYear+=expensesCurrentYear
  sumPreviousYear+=expensesPreviousYear
  count = count+1

# The variable inflationRate simply stores the inflation rate formula. It will be later used for compaaring the inflation rate value with the inflation rate types 
inflationRate=((sumCurrentYear-sumPreviousYear)/sumPreviousYear)*100
print("Personal inflation rate for ", year, " is ", inflationRate, "%")

# The following conditions idenitifes the type of inflation rate depending on the caculation
# line 29 (inflationRate<3) checks if the inflation rate caculation is less than 3. If it is true the value will be recognized as a low inflation rate type
if inflationRate<3:
  print("Type of inflation: Low")
# line 32 (inflationRate>=3 and inflationRate<5)  checks if the inflation rate caculation is greater than equal to 3 and inflationRate is less than 5, the value will be recognized as a moderate inflation type 
elif inflationRate>=3 and inflationRate<5:
  print("Type of inflation: Moderate")
# line 35 (inflationRate>=5 and inflationRate<10)  checks if the inflation rate caculation is greater than equal to 5 and inflationRate is less than 10, the value will be recognized as a high inflation type 
elif inflationRate>=5 and inflationRate <10:
  print("Type of inflation: High")
#line 38, the else statement prints out the type of inflation rate to be hyper if the inflation rate does not sastify any of the conditions 
else:
  print("Type of inflation: Hyper")
