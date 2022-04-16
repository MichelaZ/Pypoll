# 1 Open the data file.
# 1.1.1 Add dependencies
import csv
import os
# 1.1.2 Assign a variable to load file from path.
file_to_load = os.path.join("..","Resources","election_results.csv")

# 1.1.3 Assign a variable to save file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#1.2.1  Open the election results and read the file.
with open(file_to_load) as election_data:
    #read & analyze data:
    #1.2.2 Read the file w/reader function.
    file_reader = csv.reader(election_data)
    # 1.2.3 read & print the header row
    headers = next(file_reader)
    print(headers)
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
# Close file
