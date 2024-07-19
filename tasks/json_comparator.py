"""
This module provides a class `JsonComparator` to compare two JSON files 
and highlight the differences between them.
"""

import json
import sys


class JsonComparator:
    """
    This class provides methods to compare two JSON files and
    print the differences between them.
    """

    def compare_json(self, path_1: str, path_2: str) -> None:
        """
        This function compares two JSON files specified by their paths
        and prints any differences found in the data.

        Args:
            path_1 (str): Path to the first JSON file.
            path_2 (str): Path to the second JSON file.
        """
        # Load JSON data from both files
        try:
            with open(path_1, "r", encoding="utf-8") as f:
                data1 = json.load(f)
            with open(path_2, "r", encoding="utf-8") as f:
                data2 = json.load(f)
        except FileNotFoundError:
            print(f"Error: One or both files ({path_1}, {path_2}) not found!")
            return
        file_1 = path_1.split("/")[-1]
        file_2 = path_2.split("/")[-1]

        # Compare the data
        for key, value in data1.items():
            if key not in data2:
                print(f"Key '{key}' missing in file2")
            elif data2[key] != value:
                print(f"Difference in key '{key}':")
                print(f"    {file_1}: {value}")
                print(f"    {file_2}: {data2[key]}")

        # Check for keys present only in file2
        for key, value in data2.items():
            if key not in data1:
                print(f"Key '{key}' missing in {file_1}")


def main():
    """
    This function serves as the entry point for the script.
    It validates the number of arguments passed and calls the
    `compare_json` function of the `JsonComparator` class.
    """
    if len(sys.argv) != 3:
        raise TypeError("Passed-in more than two arguments!")
    else:
        comparator = JsonComparator()
        comparator.compare_json(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
