import art
import tarun
from replit import clear

bids = {}
more_users_flag = "y"

while more_users_flag == "y":
  print(art.logo)
  name = input("What's your name?\n")
  bid = int(input("What's your bid amount?\n$"))
  bids[name] = bid

  more_users_flag = input("Are there more users? Enter 'y' for yes.\n").lower()
  clear()



winner = tarun.find_winning_bidder(bids)
print(f"Highest bid is: ${winner[1]} and the highest bidder is: {winner[0]}.")




