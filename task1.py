try:
    with open("sample.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Error: sample.txt not found.")
