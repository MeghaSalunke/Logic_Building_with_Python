'''Given a purchase amount, apply a tiered discount and print the final amount rounded to 2 decimal places.

Amount Range	Discount
Amount < 1000	5%
1000 ≤ Amount < 5000	10%
Amount ≥ 5000	15%
Input → Output
800  → 760.00
3000 → 2700.00
6000 → 5100.00
Formula
final = amount - (amount × discount)
rounded to 2 decimals
'''
n = float(input("Enter the Amount:"))

d = 0.05 if n < 1000 else 0.10 if n < 5000 else 0.15
final = n -( n * d)
print(f"{final:.2f}")

