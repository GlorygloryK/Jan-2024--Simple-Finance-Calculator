import math

#POINT 3: Investment function

def investment_simple():
        number_of_years=input("Enter the number of years you plan on investing")
        number_of_years=int(number_of_years)
        interest_rate=input("What is your interest rate (%)?- Enter here:")
        interest_rate=float(interest_rate)/100
        money_deposited= (input("Enter the money you will be depositing"))
        money_deposited=float(money_deposited)
        simple_answer= money_deposited*(1+ interest_rate*number_of_years)
        print(f"The total amount of interest will be  £ {simple_answer}")

def investment_compound(): 
        number_of_years=int(input("Enter the number of years you plan on investing"))
        interest_rate=input("What is your interest rate (%)?- Entere here:")
        interest_rate=float(interest_rate)/100
        money_deposited= float(input("Enter the money you will be depositing"))
        compound_answer=money_deposited*math.pow((1+interest_rate),number_of_years)
        print(f"The total amount of interest will be £{compound_answer}")


# POINT 4: Bond function
def bond():
    house_value=input("Enter the value of the house here(£):")
    house_value=float(house_value)

    interest_rate_house=input("Enter the interest rate for your house here(£):")
    interest_rate_house=float(interest_rate_house)
    monthly_interest_rate=float((interest_rate_house/100)/12)
    
    number_of_months=input("Enter the no. of months you plan to repay the bond here(£):")
    number_of_months=int( number_of_months)

    repayment= (monthly_interest_rate*house_value)/(1-(1+monthly_interest_rate)**(-number_of_months))
    print(f"Repayment will cost £{repayment}")

# investment - to calculate the amount of interest you'll earn on your investment
# bond- to calculate the amount you'll have to pay on home loan

user_input= input("Either enter 'investment' or 'bond' from the menu above to proceed:")
if user_input == 'investment':
    interest_type = input("What is your interest type? 'simple' or 'compound'?- Type here:")
    if interest_type=='simple':
        investment_simple()
    elif interest_type=='compound':
        investment_compound()
elif user_input=='bond':
    bond()
print("Thank you for using the calculator!")


