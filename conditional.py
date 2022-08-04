"""condiitons
< less than
> greater than
<=less than or equal to
>=greater than or equal to
!= not equal to
== equal to
"""

first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))

if first_number > second_number:
    print("First number must be greater than the second number.")
elif first_number < second_number:
    print("Second number is greater than the second number")
elif first_number == second_number:
    print("first number is equal to the second number")
     