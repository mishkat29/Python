"""
Little Shino and Common factors-
Little Shino loves maths. Today her teacher gave her two intergers.
Shino is now wondering how many integers can divide both the numbers.
She is busy with her assignments. Help her to solve the problem.
Print the number of common factors of a and b.
"""

def fact(m):
    return [x for x in range(1, m+1) if m % x == 0]

def common_fact(first,sec):
    a_f = fact(first)
    b_f = fact(sec)
    i = 0
    j = 0
    count = 0
    for i in a_f:
        for j in b_f:
            if i == j:
                count = count + 1
    return count

def checker(a,b):
    if a > 0:
        if b > 0:
            return common_fact(a,b)
        else:
            return "Invalid"
    else:
        return "Invalid"
            
while True:
    try:
        a = int(input("Please enter a: "))
        b = int(input("Please enter b: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print(checker(a,b))
