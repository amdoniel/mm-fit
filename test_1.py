import pandas as pd

def decode_secret_message(csv_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Make sure column names are clean and lowercase
    df.columns = [col.strip().lower() for col in df.columns]

    # Find max x and y to determine grid size
    max_x = df['x-coordinate'].max()
    max_y = df['y-coordinate'].max()

    # Create an empty grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with characters at the correct positions
    for _, row in df.iterrows():
        x = int(row['x-coordinate'])
        y = int(row['y-coordinate'])
        char = str(row['character'])
        grid[y][x] = char

    # Print the final grid row by row
    for row in grid:
        print(''.join(row))

# Run the function with your CSV file path
decode_secret_message("mm-fit/data_code.csv")