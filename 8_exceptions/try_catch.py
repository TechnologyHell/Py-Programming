try:
    a, b = map(int, input("Enter any two numbers: ").split())  
    print(a / b)

except ValueError:
    print("Invalid input! Please enter two integers separated by space.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except Exception as e:  
    print(f"An unexpected error occurred: {e}") 