"""
This module provides functionalities for extending epochs based on either a specified number of days or a specific date.

**Epoch:**

An epoch is a timestamp representing a specific point in time. It's often used to represent the start of a period for calculations or comparisons.

**Extending Epochs:**

This class allows extending epochs by adding a specified number of days or setting the epoch to a specific date.  

**Example Usage:**

```python
from epoch_handler import EpochHandler

# Extend the epoch by 7 days
epoch_handler = EpochHandler()
extended_epoch = epoch_handler.extend_epoch(days=7)
print(f"Extended epoch (after 7 days): {extended_epoch}")

# Extend the epoch to a specific date (2024-08-10)
epoch_handler = EpochHandler()
extended_epoch = epoch_handler.extend_epoch(date="2024-08-10")
print(f"Extended epoch (to 2024-08-10): {extended_epoch}")
"""

import time
from datetime import datetime, timedelta

class EpochHandler:
    """
    Provides methods for extending epochs based on days or a specific date.

    **Methods:**

    - extend_epoch(self, days: int = None, date: str = None) -> int:
        Extends the current epoch by a specified number of days or sets it to a specific date.

    **Raises:**

    - ValueError: If the provided date format is invalid.

    **Example Usage:**

    ```python
    from epoch_handler import EpochHandler

    epoch_handler = EpochHandler()
    extended_epoch = epoch_handler.extend_epoch(days=7)
    print(f"Extended epoch (after 7 days): {extended_epoch}")
    ```
    """
    def extend_epoch(self, days: int = None, date: str = None) -> int:
        """
        Extends the current epoch by a specified number of days or sets it to a specific date.

        **Args:**

        - days (int, optional): The number of days to extend the epoch by. Defaults to None.
        - date (str, optional): The date in YYYY-MM-DD format to set the epoch to. Defaults to None.

        **Returns:**

        int: The extended epoch timestamp in milliseconds.

        **Raises:**

        - ValueError: If neither days nor a valid date format is provided.
        """
        current_time = datetime.fromtimestamp(time.time())

        if days:
            next_day = current_time + timedelta(days=days + 1)
            next_day = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
            extended_epoch = int((next_day.timestamp()) * 1000)
        elif date:
            try:
                input_date = datetime.strptime(date, "%Y-%m-%d")
                extended_epoch = int((input_date.timestamp()) * 1000)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
                return None
        else:
            print("Please provide either days or a date.")
            return None

        return extended_epoch

def main():
    """
    The main function provides a user-friendly interface for extending epochs.

    Prompts the user to enter the number of days or a specific date for epoch extension.
    Creates an EpochHandler instance and calls the extend_epoch method.
    Prints the extended epoch value.
    """
    epoch_handler = EpochHandler()
    user_input = input("Please enter expected days for extension (integer) or a specific date (YYYY-MM-DD): ")

    if str.isdigit(user_input):
        extended_epoch = epoch_handler.extend_epoch(days=int(user_input))
    else:
        extended_epoch = epoch_handler.extend_epoch(date=user_input)

    if extended_epoch:
        print(f"Extended epoch: {extended_epoch}")

if __name__ == "__main__":
    main()
