# Open the data file to import data and create file for data output
# Add dependencies
import csv
import os
# Assign a variable to load file from path.
file_to_load = os.path.join("..","Resources","election_results.csv")
# Assign a variable to save file to a path.
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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #read & analyze data:
    # Read the file w/reader function.
    file_reader = csv.reader(election_data)
    # read & print the header row
    headers = next(file_reader)
    # print data rows
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

    # Save the result to txt file
    with open(file_to_save,"w") as txt_file:
        # Format the title and total votes and print them into the file_to_save
        election_results = (f"Election Results:\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)

        # Find the total votes per candidate and percent of the total vote those votes equal
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/float(total_votes) * 100
            # Determine winning count, vote percent and candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
            # Define variable that formats candidate information
            candidate_results = (f"{candidate_name}: {vote_percentage :.1f}% ({votes:,})\n")
            # Print candidate results in the file_to_save
            print(candidate_results, end="")
            txt_file.write(candidate_results)
            
        # Define variable that formats the winner data
        winning_candidate_summary = (
            f"---------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------\n")        
        # Write the winning candidate information in the file_to_save
        print(winning_candidate_summary, end="")
        txt_file.write(winning_candidate_summary)
 