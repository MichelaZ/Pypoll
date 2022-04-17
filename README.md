# Pypoll: Analyzing election results with python
##### Module 3 | Assignment - PyPoll

## Purpose:
A Colorado election committee is looking for an easy way to audit their election results. To provide the client with an analysis of results from a congressional election I created a code to take data from a large csv file and save a report that summarizes the data to a text file. The values the client is most interested in are the votes and percentage of votes per candidate as well as the votes and percentage of votes per county. Summarizing these values gave me the winner of the election and which county had the most voter turnout.

## Getting the Results for the Candidates:
1. The first thing I had to do was load the election data. To do this I used a relative path so I had to import the CSV and OS dependencies. Then I assigned the file path to a variable.
```
import csv
import os
file_to_load = os.path.join("..","Resources","election_results.csv")
```
2. I assigned the file path for the text file I am saving the report to a variable.
```
file_to_save = os.path.join("analysis","election_analysis.txt")
```
3. I initialized a variable to store the total number of votes.
```
total_votes = 0
```
4. I declared a list to store the candidate names and a dictionary to store how many votes they got.
```
candidate_options = []
candidate_votes = {}
```
5. I declared variables to store the name, number of votes and percent of the total vote for the winner.
```
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```
6. I used the with function to open the election results from the csv file.
```
with open(file_to_load) as election_data:
``` 
7. I used the reader function to create a variable called file reader that reads the election data.
```
    file_reader = csv.reader(election_data)
```
8. I used the next function to skip the headers.
```    
headers = next(file_reader)
```    
9. I created a for loop to loop through the data rows and add a vote to the total votes for each row of data. 
```
    for row in file_reader:
        #add tot the total vote count
        total_votes += 1
  ```       
10. I defined a variable to find the names of the candidates. Then I used an if statement to store unique values to the candidate_options list, and to initialized the candidate_votes dictionary to have a value of zero for each candidate.
```
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
```    
11. I added a vote the to the candidate’s count for each row their name was voted for.
```
        candidate_votes[candidate_name] += 1
```
12. I saved the result to the text file by using the with function to open the file. Then I formatted the results and had them print to the text file
```
    with open(file_to_save,"w") as txt_file:
        election_results = (f"Election Results:\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)
```
13. I created a for loop to go through each candidate’s name in the candidate_votes dictionary. It sets a variable called votes as equal to the number of votes for that candidate. Then I calculated the candidate’s vote percentage by defining the votes/total_votes as floats, dividing the number of votes the candidate got by the total votes and multiplying it by 100.
```
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/float(total_votes) * 100
``` 
14.  To find the number of votes, percent of the vote and the name of the candidate that won I created an if statement. If the number of votes the candidate received and the percentage of votes were higher for that candidate than the previous candidate, the loop will set the wining variables I created in step 5 equal to the data for the current candidate. If it is lower, it does not.
``` 
           if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
 ```          
15.  I defined variable that formats candidate information. Then I saved the results to the text file the report is being generated in.
``` 
           candidate_results = (f"{candidate_name}: {vote_percentage :.1f}% ({votes:,})\n")
            # Print candidate results in the file_to_save
            print(candidate_results, end="")
            txt_file.write(candidate_results)
```         
16. I defined variable that formats the winning candidate information. Then I saved the results to the text file the report is being generated in.
```   
     winning_candidate_summary = (
            f"---------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------\n")        
        # Write the winning candidate information in the file_to_save
        print(winning_candidate_summary, end="")
        txt_file.write(winning_candidate_summary)
```
Here is the output when I run the file:

![Terminal output for candidate information](https://github.com/MichelaZ/Pypoll/blob/main/Resources/practice_terminal_output.png)

## Getting the Results for Voter Turnout:
1.The starter code begins similarly to how my practice code above started, but after creating the list and dictionary for the candidates I created a county list to store the county names and counties dictionary to contain the number of votes for each county.
```
import csv
from distutils import text_file
import os
file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

county = []
counties = {}
```
2. After the variables for the winner information I created variables to store the name, vote count and percentage of the total vote for the county with the largest voter turnout.
```
winning_candidate = ""
winning_count = 0
winning_percentage = 0

largest_county = ""
county_highest_count = 0
county_highest_percent = 0
```
3. After the line of code that gets the candidate name from each row I crated a variable called county_name that gets the county name from each line of code. 
```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
```
4. I used an if statement to store unique values to the county list, and initialized the counties dictionary to have a value of zero for each county. In the for loop I added a vote the to the county’s count for each row the value was present in.
```
        if county_name not in county:
            county.append(county_name)
            counties[county_name] = 0
        counties[county_name] += 1
```            
5. After the segment of code that saves the total vote count to the text file I created a for loop to go through each county’s name in the counties dictionary. It them sets a variable called county_votes as equal to the number of votes that took place in that county. Then I calculated the percentage of the vote that took place in that county by defining the county_votes/total_votes as floats, dividing the number of votes per county by the total votes and multiplying it by 100. I created a variable to format the results and save the data to the text file.
```
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

for county in counties:
        county_votes = counties.get(county)
        county_vote_percentage = float(county_votes) / float(total_votes) * 100
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_votes:,})")
        print(county_results)
        txt_file.write(county_results)
```
*formatting the county_results variable like this makes the terminal output match the brief, but if I were actually doing it for the client I would format it so that each county result would appear in the text file as an new line as below:
```
county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
```
__How text appears when formatting matches brief:__

![County results output 1](https://github.com/MichelaZ/Pypoll/blob/main/Resources/county_votes1.png)

__How text appears with each result on a new line:__

![County results output 2](https://github.com/MichelaZ/Pypoll/blob/main/Resources/county_votes2.png)

6. I create an if statement to find the county with the largest voter turnout. If the number of votes in the county and the percentage of voters that voted in that county were than the previous, the loop has gone through it will make the variables I created in step 2 equal to the data for that county. If it is lower, it does not. Then I created a variable to format the name of the county with the highest voter turnout and saved it to the text file.
```
        if (county_votes > county_highest_count) and (county_vote_percentage > county_highest_percent):
            county_highest_count = county_votes
            largest_county = county
            county_highest_percent = county_vote_percentage

    largest_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)    
    txt_file.write(largest_county_summary)   

    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
```
## Election-Audit Results:

![Terminal output for election results](https://github.com/MichelaZ/Pypoll/blob/main/Resources/election_results_Terminal.png)
![Text output for election results](https://github.com/MichelaZ/Pypoll/blob/main/Resources/election_results_Text.png)
- In this election a total of 369,711 votes were cast from this precinct.
- The winner of the election was Diana DeGette with 272,892 votes which made up 73.8% of the total votes.
- Charles Casper Stockham got 85,213 votes which was 23.0% of the total vote giving them second most votes.
- Raymon Anthony Doane came in last with 11,606 votes or 3.1% percent of the total vote.
- __Voter Turnout:__
	- Denver county had the highest voter turnout, 306,055 votes, which made up 82.8% of votes in the precinct. 
	- Jefferson county had the second most votes with 38,855 votes making up 10.5% of total precinct votes. 
	- Arapahoe had the lowest voter turnout in the precinct. Only 24,801 voters, 6.7% of the total precinct votes, vote in this election.

##### Looking Further into Voter Turnout:
I did some research, because I wanted to know what percent of the population of each county voted. I used the 2019 population data from the US Census Bureau to calculate the number of percent of the population that voted. It is probably not the same year this data was from. It also isn’t a great measure of voter turnout because it should be a measure of the percent of eligible voters. This points out a potential issue with the data: the eligible voting population may be influencing the turnout percent, but this analysis doesn’t do anything to control for that.  Regardless the order of the largest to smallest turnout stayed the same when compared to county population.
- The population of Denver County: 705,576  which makes the percent of the population that voted 43.4%.
- The population Arapahoe County 656,590  which makes the percent of the population that voted 3.8%.
- The population of Jefferson County is 582,881 which makes the percent of the population that voted 6.7%.
Even though this isn’t a very accurate measure of turnout I was surprised by how little of the population voted in this election, because Colorado is known to have one of the highest voter turnouts. This leads me to believe this is probably from an off year election, which tend to have a lower voter turnout.
_Reference:_ https://www.census.gov/

## Election-Audit Summary:
This code could easily be used to audit data from similar elections. It can be used on elections involving more voters, candidates, and counties without changing anything other than the file path. Ideas to improve functionality:
- would add some code to tell what percentage of votes for each candidate came from which counties.
- To make the turnout more accurate I would want to find a way to import the eligible voter population and then add the calculations to the election result summary. 
- To make this useful for elections from local to state to national elections I would add some additional columns of data and use code to determine what type of election it is. Then the output could be customized to show the results based on the election type.

__Author’s Notes:__ 
- You can view the commented version of this code in the txt files I’ve provide of the code I removed comments from the code excerpts to remove redundancy. 
- After finding the candidate info in the module I started the finding the candidate info in the starter code, so that my results will most closely resemble the example.
- When I was testing the code, I didn’t take any screen shots of my outputs, but when I was testing, I used the print function instead of saving the data to the text file to see if the code worked.
