import requests
import csv
from io import StringIO

def decode_secret_message(url):
    """
    Downloads a published Google Doc (in CSV format) from the given URL,
    parses the list of Unicode characters and their coordinates,
    builds a 2D grid, and prints the resulting message.
    
    Parameters:
        url (str): Public URL to the Google Doc published as CSV.
    """

    # Step 1: Fetch the document content from the provided URL
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the document.")
        return

    # Step 2: Read the CSV data into a usable format
    csv_text = response.text
    csv_file = StringIO(csv_text)
    csv_reader = csv.reader(csv_file)

    # Step 3: Skip the header row
    next(csv_reader)

    # Step 4: Parse each row to collect character placement and track grid size
    character_positions = []
    max_x = 0
    max_y = 0

    for row in csv_reader:
        try:
            x = int(row[0].strip())
            char = row[1].strip()
            y = int(row[2].strip())
        except (IndexError, ValueError):
            continue

        character_positions.append((x, char, y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Step 5: Create a blank grid (filled with spaces)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 6: Place characters in the grid at the correct positions
    for x, char, y in character_positions:
        grid[y][x] = char

    # Step 7: Print the completed grid
    for row in grid:
        print(''.join(row))


# Example usage:
if __name__ == "__main__":
    # Replace this with the actual published CSV link
    url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub?output=csv"
    decode_secret_message(url)