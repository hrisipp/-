first = int(input(''))
second = int(input(''))
third = int(input(''))
if first == second and first == third and second == third:
    print(3)
elif first == second or third == second or third == first:
    print(2)
else:
    print(0)