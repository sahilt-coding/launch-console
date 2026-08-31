name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")
    print("4) Fun Fact")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print("I'm a builder-in-training at Code2College.")
    elif choice == "2":
        print("My goal: ship my first real project this term.")
    elif choice == "3":
        print("Goodbye!")
        running = False
    elif choice == "4":
        print("Fun Fact: I love coding!")
    else:
        print("Please pick 1, 2, 3, or 4.")