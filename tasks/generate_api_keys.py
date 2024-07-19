import random
import string

class APIKeyGenerator:

    def gen_api_key(self) -> str:
        random_key = "".join(random.choice(string.ascii_letters + string.digits) for x in range(16))
        return "AU" + random_key

def main():
    generator = APIKeyGenerator()
    print(f"Generated API keys: {generator.gen_api_key()}")


if __name__ == "__main__":
    main()
