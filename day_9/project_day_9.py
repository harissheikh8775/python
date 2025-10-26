# -------------------------------
# 🏆 Secret Auction Program
# -------------------------------

# Import required modules
import os
from bidder_art import logo
from congrats_art import cong_logo


# Function to clear the screen (works on all OS)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Display logo and welcome message
print(logo)
print("Welcome to the Secret Auction Program!!!")

# Dictionary to store bidders and their bids
auctioners = {}

# Flag to control the bidding loop
continue_bid = True

# Loop for collecting bids
while continue_bid:
    # Get bidder's name and bid
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auctioners[name] = bid  # Store in dictionary

    # Ask if there are more bidders
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == "no":
        continue_bid = False  # Stop taking bids
    else:
        clear_screen()  # Clear screen for next bidder

# Find the highest bidder
max_bid = 0
max_bidder = ""

for bidder in auctioners:
    if auctioners[bidder] > max_bid:
        max_bid = auctioners[bidder]
        max_bidder = bidder

# Announce the winner
print(f"The winner is {max_bidder} with a bid of ${max_bid}!")
print(cong_logo)
