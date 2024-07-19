import random
import string
import sys


class APIKeyGenerator:

    key: str | None = None

    def __init__(self, key_length=16):
        if key_length < 1:
            raise ValueError("Key length must be at least 1")
        self.key_length = key_length

    def gen_api_key(self) -> None:
        """
        Generates random api keys with specified length

        Returns:
            generated API key
        """
        random_key = "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(self.key_length)
        )
        self.key = "AU" + random_key

    def gen_mongo_check_cmd(self) -> str:
        """
        Generates a MongoDB find command to check for the provided API key.

        Args:
            api_key: The API key to check for.

        Returns:
            A string representing the MongoDB find command.
        """
        return f"db.account.find({{ api_key: /^{self.key}/ }})"


def main():
    # Allow specifying key length as an argument (optional)
    if len(sys.argv) > 1:
        try:
            key_length = int(sys.argv[1])
            generator = APIKeyGenerator(key_length)
        except ValueError as e:
            print(e.args[0])
            exit(1)
    else:
        generator = APIKeyGenerator()
    generator.gen_api_key()
    print(f"Generated API keys: {generator.key}")
    print("Please run this command in MongoDB to check if duplicate exists:")
    print(generator.gen_mongo_check_cmd())


if __name__ == "__main__":
    main()
