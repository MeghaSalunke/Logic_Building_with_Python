'''
A gym offers membership plans based on the number of months a customer enrolls. Write a program that prints the total membership cost or an appropriate message for edge cases.Software

📐 Pricing Rules
Duration	Cost (₹)
1 month	        ₹2,000
2 or 3 months	₹5,000
4 to 6 months	₹9,000
9 months	    ₹12,000
12 months	    ₹15,000
Input < 0	invalid input
Input = 0	0
Any other value	Error
🧪 Test Cases
Input
3
Output
5000
Input
-1
Output
invalid input
'''



n = int(input("Enter the Nober of Months you want to enrolls:"))

if n < 0:
    print("Invalid Input")
elif n ==0:
    print("0")
elif n == 2 or n == 3:
    print("5000")
elif n<= 6:
    print("9000")
elif n == 9:
    print("12,000")
elif n==12:
    print("15,000")
else:
    print('Error')