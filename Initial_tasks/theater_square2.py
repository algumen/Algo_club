n = int(input())
m = int(input())
a = int(input())
if n // a == n / a:
    length = n // a
else:
    length = n // a + 1

if m // a == m / a:
    width = m // a
else:
    width = m // a + 1
    
print(length * width)