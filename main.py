import json  # Importing the JSON library for handling JSON data.
import re  # Importing the regular expression library for pattern matching.

# A function to verify the data.
def verify_data(data):
    # Iterating over each item in the data.
    for obj in data:
        # Check if each object has "Name", "age", and "birthyear" keys.
        if "Name" not in obj or "age" not in obj or "birthyear" not in obj:
            return False

        # Check if "Name" is a string.
        if not isinstance(obj["Name"], str):
            return False

        # Check if "age" is a non-negative integer.
        if not isinstance(obj["age"], int) or obj["age"] < 0:
            return False

        # Check if "birthyear" is a four-digit integer.
        if not isinstance(obj["birthyear"], int) or not re.fullmatch(r'\d{4}', str(obj["birthyear"])):
            return False

    # If all verifications pass, return True.
    return True

# Entry point for the script.
if __name__ == '__main__':
    try:
        # Open the input JSON file and load the data.
        with open('input.json', 'r') as f:
            data = json.load(f)

        # Verify the loaded data.
        if not verify_data(data):
            # If data is not valid, raise an error.
            raise ValueError("Invalid data")

        # Create the CSV header by joining the keys of the first dictionary in the list with commas.
        output = ','.join([*data[0]])

        # Iterate over each object in the data and append the values to the output string in CSV format.
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        # Open the output CSV file in write mode and write the output string to the file.
        with open('output.csv', 'w') as f:
            f.write(output)

    # Catch any exceptions that occur during the execution of the script.
    except Exception as ex:
        # Print an error message if an exception is caught.
        print(f'Error: {str(ex)}')

