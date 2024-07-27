import time
from datetime import datetime, timedelta

class EpochHandler:

    def extend_epoch(self, days: int = None, date: str = None) -> int:
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
