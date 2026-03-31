'''
Given N transactions (Sender, Receiver, Timestamp, Amount), validate them against fraud and duplication rules.

📐 Rules
Same Sender + Receiver seen before → error duplication transaction
Consecutive timestamp difference > 60 seconds → fraud detected
All valid → all transaction are valid
🧪 Test Cases
Input
2
A B 100 500
A B 110 600
Output
error duplication transaction
Input
2
A B 100 500
C D 200 300
Output
fraud detected
'''


n = int(input())

seen = set()
prev_time = None

for i in range(n):
    sender, receiver, time, amount = input().split()
    time = int(time)

    # Rule 1: Duplicate check
    if (sender, receiver) in seen:
        print("error duplication transaction")
        break
    seen.add((sender, receiver))

    # Rule 2: Fraud check
    if prev_time is not None and (time - prev_time) > 60:
        print("fraud detected")
        break

    prev_time = time

else:
    print("all transaction are valid")