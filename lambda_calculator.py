add = lambda a, b: a + b
subtract = lambda c, d: c - d
multiply = lambda e, f: e*f
divide = lambda g, h: g/h

if __name__ == "__main__":
    result1 = add(5, 3)
    result2 = subtract(5, 3)
    result3 = multiply(5, 3)
    result4 = divide(5, 3)

    print("The sum of 5 and 3 is:", result1)
    print("The difference of 5 and 3 is:", result2)
    print("The product of 5 and 3 is:", result3)
    print("The quotient of 5 and 3 is:", result4)
