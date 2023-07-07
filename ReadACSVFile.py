import csv


def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) == 4:
                # This is a print-out of the box label.
                print(f"{row[0].strip()} Box {row[1].strip()} \n {row[2].strip()} - {row[3].strip()}\n")


# This is the path to my Comic Book CSV file
csv_file_path = 'D:\Documents\comic boxes.csv'

# Call the function to read and print the contents of the CSV file
read_csv_file(csv_file_path)
