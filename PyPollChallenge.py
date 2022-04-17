
#Add dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load='Resources\election_results.csv'
#Assign a variable to save the file to a path
file_to_save='Analysis\election_results.txt'

#Intitialize a total voter count.
total_votes=0

#Create list and dictionary for candidate options and candidate votes
candidate_options=[]
candidate_votes={}

#1. Creat a county list and county votes dictionary
county_list=[]
county_votes={}

#track the winning candidate, vote count, and percentage
winning_candidate=""
winning_count=0
winning_percentage=0

#2 Track the largest county and county voter turnout
largest_county=""
voter_turnout_count=0
voter_turnout_percentage=0

#Read the csv and convert it to a list of dictionaries
with open(file_to_load) as election_data:
    reader=csv.reader(election_data)

    #read the header
    header=next(reader)

    #for each row in the CSV file.
    for row in reader:
        #Add to the total vote count
        total_votes +=1

        #Get the candidate name from each row.
        candidate_name=row[2]

        #3 Extract the county name from each row.
        county_name=row[1]

        #If the candidate does not match any existing cadidate add it to the candidate list
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #And begin tracking that candidate's voter count.
            candidate_votes[candidate_name]=0
        
        #Add a vote to that candidate's voter count
        candidate_votes[candidate_name]+=1

        #4a Write an if statement to check that the county does not match any existing in the list
        if county_name not in county_list:
            #4b Add the county name to the county list
            county_list.append(county_name)
            #4c Begin tracking the county's vote count
            county_votes[county_name]=0
        #5 Add a vote to that county's vote count.
        county_votes[county_name]+=1

#Save the results to our text file.
with open(file_to_save,"w") as txt_file:

    #Print the final vote count (to terminal)
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    #Add final vote count to text file
    txt_file.write(election_results) 

    #6a Write a for loop to get the county from the county dictionary
    for county_name in county_list:
        #6b Retrieve the county vote count
        votes=county_votes[county_name]
        #6c Calculate the percentage of votes for the county
        voter_turnout_percentage=float(votes)/float(total_votes)*100
        #6d print the county results to the terminal
        county_results=(f"{county_name}: {voter_turnout_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        #6e save the county results to a text file
        txt_file.write(county_results)
        #6f Write an if statement to dtermine the winning county and get its vote count
        if(votes>voter_turnout_count):
            voter_turnout_count=votes
            largest_county=county_name
    #7 Print the county with the largest turnout to terminal
    print(f"{largest_county} is the county with the most voter turnout.")
    #8 Save county with largest turnout to the text file
    txt_file.write(f"{largest_county} is the county with the most voter turnout.\n\n")
    
    #Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
        #Retrieve vote count and percentage
        votes=candidate_votes.get(candidate_name)
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
        #Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        #Save the candidat results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count, winning percentage, and cadidate.
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_candidate=candidate_name
            winning_percentage=vote_percentage

    #Print the winning candidate to terminal
    winning_candidate_summary=(
        f"------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
        









        





