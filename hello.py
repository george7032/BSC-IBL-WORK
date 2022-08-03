#prompt the user
name=input("What is your name? ")

#for removing white spaces
name=name.strip()

#capitalize online the first letter in a sentence
name=name.capitalize()

#capitalize all titles eg. George Kimani(G and K are in capital letters)
name=name.title() 

print(name)

print("Hello," + name)


print("Hello,", name)

#format string
print("Hello, {}". format(name))

print(f"Hello, {name}")





("Hello, world")
