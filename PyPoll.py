#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

#Add out dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load='Resources\election_results.csv'

#Assign a variable to save the file to a path
file_to_save='Analysis\election_analysis.txt'

#Open the election resuts and read the file
with open(file_to_load) as election_data:


    #To Do: read and analyze the data here
    file_reader=csv.reader(election_data)
    #print each row in the CSV file
    headers=next(file_reader)
    print(headers)




#Open the election analysis file
###outfile=open(file_to_save,"w")
#Using the with statement to open the file as a txt file
##with open(file_to_save,"w") as txt_file:

#Write three counties into the file
    ##txt_file.write("Counties in the election\n--------------------------\nArapahoe\nDenver\nJefferson")
#Close the file
##outfile.close
