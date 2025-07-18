import request
import csv
from io import StringIO

def decode_secret_message(url):
    """
    Given a URL to a published Google Doc (as CSV), this function fetches the data,
    parses character positions, and prints a grid forming the secret message.
    """
    # Step 1: Download the CSV-formatted data from the published Google Doc
    response = requests.get(url)
    response.raise_for_status()  # Ensure we catch bad links or access issues

    # Step 2: Parse CSV data
    content = response.text
    reader = csv.reader(StringIO(content))
    
    # Skip header row
    next(reader)

    # Step 3: Collect character placements and find grid bounds
    cells = []
    max_x = 0
    max_y = 0

    for row in reader:
        try:
            x = int(row[0].strip())
            char = row[1].strip()
            y = int(row[2].strip())
        except (ValueError, IndexError):
            continue  # Skip invalid rows

        cells.append((x, char, y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Step 4: Create empty grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 5: Place characters at the specified coordinates
    for x, char, y in cells:
        grid[y][x] = char  # y is row index, x is column index

    # Step 6: Print the grid
    for row in grid:
        print(''.join(row))




