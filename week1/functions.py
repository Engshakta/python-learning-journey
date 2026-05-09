hours = float(input("Enter hours worked: "))
rate= float(input("Enter rate per hour worked: "))

def computepay(hours, rate):
    if hours > 40 :
     over_time = hours - 40
     gross_salary = (40 * rate) + (over_time * rate *1.5)
     
    else:
     gross_salary = hours * rate

    return gross_salary
   
    
print("Pay" , computepay(hours, rate))