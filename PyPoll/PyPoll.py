import csv
import os


election_data = os.path.join("..","Challenge3","Starter_Code","Starter_Code","PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..","Challenge3","Starter_Code","Starter_Code","PyPoll","Resources","electionResults.txt")  # Output file path

totalVotes=0 #Variable that will help us calculate the total amount of votes
candidates=[] #All values of the column Candidate will be stored here
candidateVotes=[] #The total voltes per candidatw will be stored here.
candidatePercent=[] #All the percetage of votes per each candidate will be stored here
UniqueCandidates=[] #Unique values foun in the list candidates will be stored here
candidate_count=0 #The counter of votes that will help us iterate the list candidates and will help us calculate the total votes per candidate
averageVotes=0 #the variable that will help us calculate the average votes


with open(election_data) as ElectionCsv: #Open file
    ElectionReader = csv.reader(ElectionCsv) #Read file and file type
    header = next(ElectionReader) #skip and Save the header ['Ballot ID', 'County', 'Candidate'] 

    for row in ElectionReader: #Row gives back each row in a list form ["Date","234343"]
        totalVotes=totalVotes+1 #Cout all votes
        candidates.append(row[2]) 


    UniqueCandidates.append(candidates[0]) #Start Unique values. Without it, any different values in the first row vs sencond row would be missed
    for i in range(len(candidates)-1): #Look for unique values within the list Candiadates
        if (candidates[i] != candidates[i+1]) and (candidates[i+1] not in UniqueCandidates):
            UniqueCandidates.append(candidates[i+1])
    
    for i in UniqueCandidates: #Count the votes per candidates and calculate their average votes
        candidate_count=0
        for x in candidates:
            if i == x:
                candidate_count=candidate_count+1
        averageVotes=round((candidate_count/totalVotes)*100,2)
        
        candidateVotes.append(candidate_count)
        candidatePercent.append(averageVotes)


summary=list(zip(UniqueCandidates,candidatePercent,candidateVotes)) #build a summary of the information


with open(file_to_output, "w") as txt_file: #Save the information in a Txt

    print("ElectionResults")
    txt_file.write("ElectionResults \n")

    print("---------------------")
    txt_file.write("--------------------- \n")
    
    print(f"Total Votes: {totalVotes}")
    txt_file.write(f"Total Votes: {totalVotes} \n")

    print("----------------------")
    txt_file.write("--------------------- \n")
    
    for i in range(len(summary)): #iterate through the summary to print all the candidate's information
        print(f"{summary[i][0]} {summary[i][1]}% ({summary[i][2]})")
        txt_file.write(f"{summary[i][0]} {summary[i][1]}% ({summary[i][2]}) \n")

    print("----------------------")
    txt_file.write("---------------------- \n")

    
    winner=UniqueCandidates[candidateVotes.index(max(candidateVotes))] #look for the max in list candidateVotes to determine the winner
    print(f"Winner: {winner}")
    txt_file.write(f"Winner: {winner} \n")


