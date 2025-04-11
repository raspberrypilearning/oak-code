# read the spellings from the CSV file
file = open("spellings.csv","r")
words = file.read()
file.close()

# assign the spellings to a list
words = words.split(",")
results = []

# check the spelling of each word and store results
for item in words:
    word = input("Enter word: ")
    if word == item:
        results.append("Correct")
    else:
        results.append("Incorrect")

# join the results to a single string
data = "\n" + ",".join(results)

# append the results to the spellings CSV file
file = open("spellings.csv","a")
file.write(data)
file.close()