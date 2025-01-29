import csv
import os

def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    data = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return data

def process_data(data):
    """
    Processes the data (e.g., filters, transforms, etc.).
    In this example, we'll just print the data.
    """
    for record in data:
        print(f"Name: {record['Name']}, Age: {record['Age']}, City: {record['City']}")

def main():
    # Define the path to the CSV file
    csv_file_path = os.path.join('..', 'data', 'input.csv')
    
    # Read the CSV file
    data = read_csv(csv_file_path)
    
    # Process the data
    if data:
        process_data(data)

if __name__ == "__main__":
    main()