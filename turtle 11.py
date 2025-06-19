name = input("Enter your name: ")

while(name != ""):
    for i in range(5):
        print(name, end = "\n")

    name = input("Enter your name ↩ to quit: ")

print("Thanks for playing! ")
