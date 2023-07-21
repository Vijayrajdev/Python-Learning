# Formatted strings

First = "vijay"
Last = "Raj"

msg = f'{First} [{Last}] is a coder'

print(msg)

# String methods

string = "This is the example for string operations"

print(len(string))
print(string.upper())
print(string.lower())

print(string.find('s'))
print(string.find('for'))
print(string.replace('the', 'a'))


weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
converted_unit = unit.upper()

if converted_unit == "L":
    print(f"Your weight is {weight * 0.45}")

else:
    print(f"Your weight is {weight / 0.45}")
