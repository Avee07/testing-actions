import argparse

def main():
    parser = argparse.ArgumentParser(description="Greet the user with details.")
    parser.add_argument('--name', required=True, help='Name of the user')
    parser.add_argument('--age', required=True, help='Age of the user')
    parser.add_argument('--place', required=True, help='Place where the user lives')

    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    print(f"You are {args.age} years old and live in {args.place}.")

if __name__ == "__main__":
    main()
