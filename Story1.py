def is_palindrome(n):
    return str(n) == str(n)[::-1]

def has_repeated(n):
    s = str(n)
    return len(s) != len(set(s))

def cryptic_numbers(L, R):
    result = []
    for num in range( L, R+1):
        if num % 7 == 0 and num % 5 != 0:
            if not is_palindrome(num):
                if not has_repeated(num):
                    result.append(num)
    if len(result)==0:
        print(-1)
    else:
        print(*result)

L = int(input("Enter L:"))
R = int(input("Enter R:"))

print(cryptic_numbers(L, R))