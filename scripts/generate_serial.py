import uuid
import datetime

def generate_serial():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4()).split('-')[0]
    serial_number = f"SERIAL-{timestamp}-{unique_id}"
    return serial_number

def main():
    serial = generate_serial()
    print(f"🎯 Generated Serial Number: {serial}")

    with open("artofcats.txt", "w") as f:
        f.write(f"{serial}\n")

    print("✅ Serial number saved to artofcats.txt")

if __name__ == "__main__":
    main()
