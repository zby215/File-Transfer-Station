def area(r):
    a = 3.142 * r * r
    return a


radius = int(input('What is the radius of your circle?'))

circle_area = area(radius)
print('The area of your circle is', circle_area)
