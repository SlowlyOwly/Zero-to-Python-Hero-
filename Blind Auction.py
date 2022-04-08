from replit import clear

from art import logo
print(logo)
print("Welcome to the secret auction program.")

auctioners = {}

auction = True

while auction:
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  auctioners[name] = bid
  end = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  clear()
  high_bid = 0
  for bidder in auctioners:
    if int(auctioners[bidder]) > high_bid:
      high_bid = int(auctioners[bidder])
      winner = bidder
  
  if end == "no":
    auction = False
    print(f"The winner is {winner} with a bid of ${high_bid}")