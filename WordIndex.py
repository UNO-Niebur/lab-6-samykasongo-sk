#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary

  line_number = 0

  for line in textFile:
    line_number += 1

    clean_line = line.strip().lower()
    clean_line = clean_line.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    for word in clean_line.split():
      if word not in words:
        words[word] = [line_number]
      else:
        if line_number not in words[word]:
          words[word].append(line_number)

  textFile.close()          
  
  
  print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)


if __name__ == '__main__':
  main()
