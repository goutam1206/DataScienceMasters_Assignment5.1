# The below function has the exception handling. On error, it returns the error string else, a number
def divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Divide by Zero Exception")
        return "Divide by Zero Exception"
        

        
# Below code calls the function which handles the exception of Zero Division
while True:
    try:
        numerator=int(input("Enter the numerator value: "))
        denominator=int(input("Enter the denominator value: "))
        break;
    except ValueError:
        print ("Please enter a valid integer value")

result = divide(numerator,denominator)
print ("Result: ",result)
    