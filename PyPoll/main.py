import os
import csv

#------------------READ CSV-----------------------------   

#Runned with GitBash 
csvpath = os.path.join('Resources', 'election_data.csv')
analysispath = os.path.join('analysis', 'analysis_poll.txt') 

# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
id = []
county = []
candidates = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csvheader = next(csvreader)
    #print(f"Header: {csvheader}")

    for row in csvreader:
        
        id.append(int(row[0]))  
        county.append(str(row[1]))
        candidates.append(str(row[2]))

poll_data = {}
poll_data["id"] = id
poll_data["county"] = county
poll_data["candidates"] = candidates

#------------------ANALYSIS-----------------------------   

def poll_analysis(filepath, id, county, candidates):      

    analysis = open(filepath, 'w') 

    analysis.write(" Election Results")
    analysis.write("\n----------------------------")


# The total number of votes cast

    total_votes = len(id)
    analysis.write("\n Total Votes: " + str(total_votes))
    analysis.write("\n----------------------------")


# A complete list of candidates who received votes,
# The total number of votes each candidate won and
# The percentage of votes each candidate won

    unique_candidates = {}

    for candidate in candidates:
        
        if candidate not in unique_candidates.keys():
            unique_candidates[candidate] = 1
        else:
            unique_candidates[candidate] +=1

    for candidate, votes in zip(unique_candidates.keys(), unique_candidates.values()):

        votes_percent = percent(total_votes,votes,3)
    
        analysis.write("\n " + candidate + ": " + str(votes_percent) + "% (" + str(votes) + ")")
            
    analysis.write("\n----------------------------")


# The winner of the election based on popular vote.

    max_votes = max(unique_candidates.values())

    winner = [key for key, value in unique_candidates.items() if value == max_votes]
    
    
    analysis.write("\n Winner: " + winner[0])

    analysis.write("\n----------------------------")

    analysis.close()


#------------------FUNCTIONS-----------------------------   

def percent(total,partial,decimals):
    result = (partial * 100) / total
    return round(result,decimals)
    

#------------------RESULT-----------------------------   
 
poll_analysis(analysispath, id, county, candidates) 

#------------------PRINT RESULT-----------------------  

results = open(analysispath, "r")
print(results.read())


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

