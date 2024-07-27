"""
This module provides functionalities for generating random API keys and creating
MongoDB find commands to check for their existence.

**Example usage:**

```python
from api_key_generator import APIKeyGenerator

# Generate an API key with a default length of 16 characters
generator = APIKeyGenerator()
api_key = generator.gen_api_key()
print(f"Generated API key: {api_key}")

# Generate an API key with a specific length (20 characters)
generator = APIKeyGenerator(key_length=20)
api_key = generator.gen_api_key()
print(f"Generated API key with 20 characters: {api_key}")

# Generate a MongoDB find command to check for an API key
mongo_cmd = generator.gen_mongo_check_cmd(api_key)
print(f"\nMongoDB check command: {mongo_cmd}")
"""

import random
import string
import sys


class APIKeyGenerator:
    """
    Generates random API keys with a specified length and provides a function
    to create a MongoDB find command for checking their existence.

    **Attributes:**

    - key (str | None): Stores the most recently generated API key.

    **Raises:**

    - ValueError: If the provided key length is less than 1 character.

    **Example usage:**

    ```python
    generator = APIKeyGenerator()
    api_key = generator.gen_api_key()
    print(f"Generated API key: {api_key}")

    mongo_cmd = generator.gen_mongo_check_cmd(api_key)
    print(f"\nMongoDB check command: {mongo_cmd}")
    ```

    Example Usage in cmd:
    python tasks/generate_api_keys.py
    """

    key: str | None = None

    def __init__(self, key_length=16):
        if key_length < 1:
            raise ValueError("Key length must be at least 1")
        self.key_length = key_length

    def gen_api_key(self) -> None:
        """
        Generates a random API key with the specified length prepended with "AU".

        The generated key is stored in the `key` attribute of the object.

        **Returns:**

        None
        """
        random_key = "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(self.key_length)
        )
        self.key = "AU" + random_key

    def gen_mongo_check_cmd(self) -> str:
        """
        Generates a MongoDB find command to check for the provided API key.

        **Returns:**

        A string representing the MongoDB find command.
        """
        return f"db.account.find({{ api_key: /^{self.key}/ }})"

    def get_mongo_upsert_cmd(self) -> str:
        """
        Generates a MongoDB updateOne command with upsert functionality.

        Args:
            mongo_id: The MongoDB document _id to update or insert.
            api_key: The API key to set in the document.

        Returns:
            A string representing the MongoDB updateOne command.
        """
        return f"db.account.updateOne({{\"_id\": ObjectId('REAL_ACCOUNT_ID')}}, {{ $set: {{ \"api_key\": \"{self.key}\" }}}})"


def main():
    """
    The main function takes an optional argument for specifying the API key length.

    **Args:**

    - sys.argv: List containing command-line arguments.

    **Returns:**

    None
    """
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
    print("Once checked, run the upset command to insert the value:")
    print(generator.get_mongo_upsert_cmd())


if __name__ == "__main__":
    main()
