numerator = int(input())
denominator = int(input())

# Find the integer part, and subtract the integer from the original fraction
integer = numerator // denominator
numerator -= integer * denominator

for i in range(2,numerator+1):           # Determines the simplest form
    if numerator % i == 0 and denominator % i == 0:
        numerator //= i
        denominator //= i

if numerator == 0:           # output data when there is no fraction
    print(integer)
elif integer == 0:           # output data when there is no integer
    print("%d/%d" % (numerator,denominator))
else:                        # output data when there are both fraction and integer
    print(integer,"%d/%d" % (numerator,denominator))
