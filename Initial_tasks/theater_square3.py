str = input()
input_data = str.split(' ')
n = int(input_data[0])
m = int(input_data[1])
a = int(input_data[2])

if n // a == n / a:
    length = n // a
else:
    length = n // a + 1

if m // a == m / a:
    width = m // a
else:
    width = m // a + 1
print(length * width)