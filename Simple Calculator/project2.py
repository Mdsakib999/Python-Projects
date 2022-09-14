#How to make a simple calculator  using python???



def add(x, y):
    return x + y
def subtract(x , y):
    return x - y
def multiply(x, y):
    return x*y
def divided(x, y):
    return x / y

print("Select what do you want to do :")
print("1. sum")
print("2. subtract")
print("3. Multiply")
print("4. Divided")

#take inpute from user
choice = input("enter choice(1/2/3/4): ")
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divided(num1, num2))
else:
    print("not valid")