def circle_info(r):
    a = 3.142 * r * r
    c = 2 * 3.142 * r
    return a,c

radius = int(input('What is the radius od your circle?'))

area, circumf = circle_info(radius)

print('The area of your circle is', area)
print('The circumference of your circle is',circumf)