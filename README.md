# Election_Analysis

## Project Overview
The goal of this project was to complete an audit for a recent congressional election. To complete the audit it is necessary to understand the following:
  1. The total number of votes cast
  2. A complete list of candidates that received votes
  3. The total number of votes each candidate received
  4. The percentage of votes each candidate won
  5. Which candidate won the election by popular vote

## Resources
Data source: election_results.csv
Software: Python 3.7, VS Code 

## Election Audit Results
A total of 369,711 votes were cast in the election

Candidates with votes were:
-Charles Casper Stockham
-Diana Degette
-Raymon Anthony Doane

Counties represented in this election were:
-Jefferson
-Denver
-Arapahoe

Voter statistics by county:
-Jefferson voters made up 10.5% of the voter base with 38,855 voters total.
-Denver voters made up 82,8% of the voter base with 306,055 voters total.
-Arapahoe voters made up 6.7% ofthe voter base with 24,801 voters total.

Denver voters made up the majority of voters in this election

Results by candidate were:
-Charles Casper Stockham received 23% of the votes with a total of 85,213 votes.
-Diana Degette received 73.8% fo the votes with a total of 272,892 votes.
-Raymon Anthony Doan received 3.1% of the votes with a toal of 11,606 votes.

The winner of the election was: 
-Diana Degette won the election with 73.8% of the votes with a total of 272,892 votes.

## Election Audit Summary

The script written to audit this election can be used to audit results of other elections where Voter ID, County, and Candidate values are provided. Should the raw data provide a candidate ID number rather than a name, you can generate a dictionary with the ID as the key and name as a value, then cross refernce the ID to the names continue to use this script. If data provides zip code rather than county information, you can substitue the county values for zip code values and continue to run this script.
