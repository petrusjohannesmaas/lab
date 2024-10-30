from cryptography.fernet import Fernet


def generate_key():
    # Generate a key
    key = Fernet.generate_key()

    # Display the key
    print(f"Your encryption key: {key.decode()}")
    print(
        "Write this key down somewhere safe. You'll need it to encrypt and decrypt your data."
    )


if __name__ == "__main__":
    generate_key()
