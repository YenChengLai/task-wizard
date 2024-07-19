import random
import string
import sys

class APIKeyGenerator:

    def __init__(self, key_length=16):
        self.key_length = key_length

    def gen_api_key(self) -> str:
        random_key = "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(self.key_length)
        )
        return "AU" + random_key


def main():
    # Allow specifying key length as an argument (optional)
    if len(sys.argv) > 1:
        try:
            key_length = int(sys.argv[1])
            generator = APIKeyGenerator(key_length)
        except ValueError:
            print("Invalid argument. Please provide an integer for key length.")
            exit(1)
    else:
        generator = APIKeyGenerator()
    print(f"Generated API keys: {generator.gen_api_key()}")


if __name__ == "__main__":
    main()
