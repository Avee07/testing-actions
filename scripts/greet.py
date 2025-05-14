import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--age', required=True)
    parser.add_argument('--place', required=True)
    args = parser.parse_args()

    print(f"Hello, {args.name}!")
    print(f"You are {args.age} years old and live in {args.place}.")
    
    # Get GitHub actor from environment variable
    actor = os.getenv("GITHUB_ACTORS", "unknown")
    actor = actor.split('_')[0]

    print(f"🚀 This workflow was triggered by: {actor}")

if __name__ == "__main__":
    main()
