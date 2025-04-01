import random
import string

def generate_key():
    characters = string.ascii_uppercase + string.digits
    groups = [''.join(random.choices(characters, k=5)) for _ in range(5)]
    return '-'.join(groups)

def main():
    num_keys = 450
    keys = [generate_key() for _ in range(num_keys)]
    with open("valid_keys.txt", "w") as file:
        for key in keys:
            file.write(key + "\n")
    print(f"EaglerHost | {num_keys} generated.")

if __name__ == "__main__":
    main()
