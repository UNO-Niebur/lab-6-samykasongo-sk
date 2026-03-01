#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  #find the sum total of the two dice
  #print statictics for dice rolls 
  
  nums_rolls = 10000

  for _ in range(nums_rolls):
    first_die = random.randint(1,6)
    second_die = random.randint(1,6)

    total = first_die + second_die

    rolls[total -2] += 1

  print("Dice rolls Stat ", nums_rolls, " rolls:\n")
  for i in range(11):
    sum_val = i+2
    count = rolls[i]
    percentage =   (count / nums_rolls) * 100
    print(f"Sum {sum_val}: {count} times ({percentage:.2f}%)")



if __name__ == '__main__':
  main()
