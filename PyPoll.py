#Add out dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load='Resources\election_results.csv'
#Assign a variable to save the file to a path
file_to_save='Analysis\election_analysis.txt'

#1 Initiate total vote counter
total_votes=0
#2 Declare variable for candidate name
candidate_options=[]
#3 and 4 Create dictionary to store # of votes per candidate
candidate_votes={}
#5 Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0


#Open the election resuts and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #read the header row.
    headers=next(file_reader)

    #Print each row in the CSV file w/out Header
    for row in file_reader:
        #1 Add to the total vote count
        total_votes +=1

        #2 Get list of candidates
        candidate_name=row[2]
        
        #2 If the candidate doesn't match any existing candidates
        if candidate_name not in candidate_options:
            #2 Add it to the list of candidates
            candidate_options.append(candidate_name)
            #4 Begin tracking candidate's vote count
            candidate_votes[candidate_name]=0
            #4 Incrementally increase candidate votes by 1 for each row
        candidate_votes[candidate_name]+=1

#Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    #After opening the file, print the final vote count to terminal
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #After printin, write the final vote count in text file
    txt_file.write(election_results)

#3 Determine percent vote for each candidate
# Iterate through the cadidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results=(
            f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

        #print each candidates voter count and percent to terminal
        print(candidate_results)
        #save candidate results to text tile
        txt_file.write(candidate_results)

        #5 Determing winning vote and percentage
        #Determine if the votes is greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            #If true, set winning count= votes and winning percent = vote percent
            winning_count=votes
            winning_percentage=vote_percentage
            #Winning candidate is equal to candidate name
            winning_candidate=candidate_name
    winning_candidate_summary=(
        f"------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)

    #save winning candidate results to text file
    txt_file.write(winning_candidate_summary)





