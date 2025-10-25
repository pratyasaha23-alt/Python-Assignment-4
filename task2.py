data = input("Enter text to write: ")
with open("output.txt", "w") as f:
    f.write(data + "\n")

append_data = input("Enter text to append: ")
with open("output.txt", "a") as f:
    f.write(append_data + "\n")

with open("output.txt", "r") as f:
    print("\nFinal file content:")
    print(f.read())
