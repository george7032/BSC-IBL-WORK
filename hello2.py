name=input("Enter your name: ")
first_name, last_name=name.strip().title().split()
print("hi, {}". format(first_name))



first_name, last_name=input("What is your name? ").strip().title().split()
print(f"{first_name} {last_name}")