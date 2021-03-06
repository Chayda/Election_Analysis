# Dependencies
import csv
import os

# Variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
counties = []
county_votes = {}


# Track the winning candidate, vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
winning_county = ""
county_turnout = 0
w_county_percentage = 0


# Read the csv and convert it into a list of dictionaries.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header.
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count.
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:
            
            # Add the existing county to the list of counties.
            counties.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal).
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Get the county from the county dictionary.
    for county_name in county_votes:
        # Retrieve the county vote count.
        votes = county_votes[county_name]
        # Calculate the percentage of votes for the county.
        county_percentage = float(votes / float(total_votes) * 100)

         # Print the county results (to terminal).
        print(county_votes)
         # Save the county votes to a text file.
        txt_file.write(str(county_votes))
         # Write an if statement to determine the winning county and get its vote count.
        if (votes > county_turnout) and (county_percentage > w_county_percentage):
            county_turnout = votes
            w_county_percentage = county_percentage
            winning_county = county_name

    # Print the county with the largest turnout (to terminal).
        county_turnout_summary = (
            f"-------------------------\n"
            f"Winning County: {winning_county}\n"
            f"Largest County Vote Count: {county_turnout:,}\n"
            f"Winning County Percentage: {w_county_percentage:.1f}%\n"
            f"-------------------------\n"
            )
            
        print(county_turnout_summary)

    # Save the county with the largest turnout to a text file.
        txt_file.write(county_turnout_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage (to terminal).
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal).
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
