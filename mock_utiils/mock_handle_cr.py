import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--state', required=True)
parser.add_argument('--close_code', required=False)
args = parser.parse_args()

state = args.state
close_code = args.close_code

print(f"[INFO] Executing CR step: {state}")

if state == "create":
    print("Creating change request...")
    with open("mock_CHANGE_NUMBER.txt", "w") as f:
        f.write("CR-0001\n")

elif state == "implement":
    print("Implementing the change request...")
    with open("mock_CHANGE_NUMBER.txt", "r") as f:
        print(f"Change Number: {f.read()}")

elif state == "close":
    print("Closing the change request with code:", close_code)
else:
    print("[ERROR] Unknown state")
    exit(1)
