# Election_Analysis
An analysis of county elections for Colorado using Python.
## Overview of the Election Audit
### The purpose of this analysis is to capture the vote count by candidate and county, to determine the winning candidate as well as to see how many votes were cast per county in the election.

## Election-Audit Results:
### 
•	There were 369,711 votes cast in the election.

•	The counties were:
  - Jefferson
  - Denver
  - Arapahoe
 
•	The election results per county were:
  - Jefferson County  received 10.5% of the vote and 38,855 number of votes.
  - Denver County received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe County received 6.7% of the vote and 24,801 number of votes.
 
•	The county with the largest number of votes was Denver, which received 82.8% of the vote and 306,055 number of votes.

•	The candidates were:
  - Charles Casper Stockham
  - Diana Degette
  - Raymon Anthony Doane

•	The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana Degette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes. 

##	The winner of the election was:
  - Diana Degette received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary:
### This code can be used for elections in other counties, and modified to glean useful information about election campaigns in the following ways:

1)	Modify the code to see which candidate is the winner for each county; this can help to advise on how to assign a campaign budget for each county in future campaigns. Use a vote percentage for each county and assign it to the related candidate and print the results using an if-elif-else statement that would print the appropriate candidate name, county name, and vote percent for that county; or print for the other candidates for the same county. Would have to use the candidate_votes and county_votes dictionaries.

2)	Further, we can modify the code to compare the amount spent on individual campaigns for each candidate which may lead to insights on a successful election. We would require data on how much was spent by each candidate during the campaign, and merge it to the csv file used in the analysis. A dictionary added to the script that shows the campaign dollars spent in each county (key: candidate name & value: dollars spent). We can loop through the code to find how much each candidate spent in each county.

