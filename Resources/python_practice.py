# 1. Open the data file to import data and create file for data output
# 1.1.1 Add dependencies
import csv
import os
# 1.1.2 Assign a variable to load file from path.
file_to_load = os.path.join("..","Resources","election_results.csv")

# 1.1.3 Assign a variable to save file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# initialize total vote counter
total_votes = 0

#Declare Candidate options & Votes
candidate_options = []
candidate_votes = {}
#Declare winner variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#1.2.1  Open the election results and read the file.
with open(file_to_load) as election_data:
    #read & analyze data:
    #1.2.2 Read the file w/reader function.
    file_reader = csv.reader(election_data)
    # 1.2.3 read & print the header row
    headers = next(file_reader)
    # 1.2.4 print data rows
    for row in file_reader:
        #add tot the total vote count
        total_votes += 1
        
        #print candidate name from each row
        candidate_name = row[2]
        #Calculate candiate votes
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            #initialize candidate votes
            candidate_votes[candidate_name] = 0
        #Add vote to candidate count
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage :.1f}% ({votes:,})")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n"
    )        
    print(winning_candidate_summary)

