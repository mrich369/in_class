# Instructions
# A group of friends is planning movie night and needs to organize votes. Write a program that:
# 1. Ask for the name of the person hosting (a string)
host = input("Host name: ")

# 5. Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
votes = []

# 2. Use a while loop to let the user add movie votes one at a time. After each vote, ask
# "Add another vote? (yes/no)". Stop when the user types "no".
add_more = "yes"
while add_more == "yes":
    # 3. For each vote, collect:
    # • Voter name (a string)
    # • Movie title (a string)
    # • Genre: "action", "comedy", "horror", or "drama" (a string)
    # 4. Clean each vote’s data before storing:
    # • Voter name should be converted to title case (e.g., "jane doe" → "Jane Doe")
    # • Movie title should be converted to title case
    # • Genre should be converted to lowercase and stripped of whitespace
    voter_name = input("Voter name: ").title()
    movie_title = input("Movie title: ").title()
    genre = input("Genre (action, comedy, horror, drama): ").lower().strip()

    # 5. Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
    vote_dict = {"voter": voter_name, "movie": movie_title, "genre": genre}
    votes.append(vote_dict)

    add_more = input("Add another vote? (yes/no): ").lower()
# 6. After voting closes, produce a report:
# • Total number of votes
# • Number of comedy votes and number of non-comedy votes (use an accumulator or
# counter)
# Example output:
# --- Movie Night Report (hosted by Alex) ---
# Total votes: 4
# Comedy votes: 3
# Other votes: 1

print(f"\n--- Movie Night Report (hosted by {host}) ---")

total_votes = len(votes)
comedy_votes = 0
for vote in votes:
    if vote["genre"] == "comedy":
        comedy_votes += 1
non_comedy_votes = total_votes - comedy_votes

print(f"Total Votes: {total_votes}")
print(f"Comedy Votes: {comedy_votes}")
print(f"Other Votes: {non_comedy_votes}")

# A numbered list of all votes showing voter, movie, and genre (use a for loop with the
# index)
# All Votes:
# 1. Jane Doe voted for The Hangover (comedy)
# 2. Bob Smith voted for Inception (action)
# 3. Carol Lee voted for Bridesmaids (comedy)
# 4. Dan Park voted for Superbad (comedy)

for i in range(len(votes)):
    print(f"{i+1}. {votes[i]["voter"]} voted for {votes[i]["movie"]} ({votes[i]["genre"]})")

# • If more than half the votes are for comedy, print: "Looks like a comedy night!"
# Looks like a comedy night!

if (comedy_votes / total_votes) > 0.5:
    print("Looks like a comedy night!")

# IS 303 Practice Midterm Builds 1–3
# Page 7
# Constraints
# • Must use a while loop (not a for loop with a fixed count)
# • Must use string methods to clean data (title case, lowercase, strip)
# • Must use a list of dictionaries
# • Must use an accumulator/counter for comedy vs. non-comedy counts
# • Must use a conditional for the comedy night message