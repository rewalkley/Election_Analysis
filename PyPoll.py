# The data we need to retrieve
# 1. The total number of voted cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of vote each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open results and read file

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# To do: read and analyze the data here
# Read the file with the reader function
# Print each row in the CSV file
#    for row in file_reader:
#        print(row)
# Print the Header Row
    headers = next(file_reader)
    print(headers)




