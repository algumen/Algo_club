
class TheaterSquare(object):
    def square_calc(self, n,m,a):

        if n//a==n/a:
            length  = n//a
        else: length  = n//a+1

        if m//a==m/a:
            width  = m//a
        else: width  = m//a+1

        quantity = length * width
        return quantity

n = int(input('Input n  '))
m = int(input('Input m  '))
a = int(input('Input a  '))
c = TheaterSquare()
print(c.square_calc(n,m,a))