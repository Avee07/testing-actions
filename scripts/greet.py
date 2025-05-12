import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--age', required=True)
    parser.add_argument('--place', required=True)
    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    print(f"You are {args.age} years old and live in {args.place}.")

if __name__ == "__main__":
    main()
s