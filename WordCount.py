#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  line_count = 0
  word_count = 0
  char_count = 0

  for line in textFile:
    print(line, end='')

    line_count +=1
    word_count += len(line.split())
    char_count += len(line)

  textFile.close()

  print("\n\nFile Stats:")
  print("\nLines: ", line_count)
  print("\nWords: ", word_count)
  print("\nCharacters: ", char_count)  
  

  

if __name__ == '__main__':
  main()
