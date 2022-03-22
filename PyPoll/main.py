import os
import csv

#------------------READ CSV-----------------------------   

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
analysispath = os.path.join('PyPoll', 'analysis', 'analysis_poll.txt') 

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

    analysis.write("\n Total Votes: " + str(len(id)))
    analysis.write("\n----------------------------")


# A complete list of candidates who received votes

    unique_candidates = []                 # do dict
    votes = []
    index = 0

    unique_candidates.append(candidates[0])
    votes.append(0)
    print(len(unique_candidates))
    print(votes)

    for candidate in candidates:
        find = False
        
        while not find or index < len(unique_candidates):
            
            if candidate == unique_candidates[index]:
                
                find = True
                votes[index] += 1 
            else:
                index+=1
        
        if not find:
            unique_candidates.append(candidate)
            votes[len(unique_candidates)-1] = 1
    
    analysis.write("\n candidates: {unique_candidates} and votes: {votes}")
            

# The percentage of votes each candidate won



# The total number of votes each candidate won




# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------


# The winner of the election based on popular vote.

# Winner: Diana DeGette
# -------------------------




    analysis.close()

#------------------FUNCTIONS-----------------------------   

def sum(nums):
    count= 0
    for i in nums:
        count=count+i
    return count

def average(nums):
    num = sum(nums)/len(nums) 
    return(round(num,2))
    

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


