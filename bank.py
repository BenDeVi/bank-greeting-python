words = input("Greeting:").strip().lower()


if words.startswith("hello"):
    print("$0")
elif words.startswith("h"):
    print("$20")

else:
    print("$100")
