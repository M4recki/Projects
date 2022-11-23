from replit import clear
Dictionary = {}


def AddNewPerson(name, bid):
    Dictionary[name] = bid


while True:
    Name = input("What is your name?: ")
    Bid = int(input("What is your bid?: $"))
    AddNewPerson(name=Name, bid=Bid)
    Users = input(
        "Are there any other bidders? Type 'y' or 'n' (y-yes, n-no) ")
    if Users == "y":
        AddNewPerson(name=Name, bid=Bid)
        clear()
        continue
    elif Users == "n":
        break
    else:
        print("Invalid input. Please try again.")
        continue

HighestBid1 = max(Dictionary, key=Dictionary.get) #Bidder winner
HighestBid2 = max(Dictionary.values()) #Highest bid

#Or

# def FindHighestBidder (BidRecord):
#HighestBid = 0
#Winner = ""
#for Bidder in BidRecord:
    #BidAmount = BidRecord[Bidder]
    #if BidAmount > HighestBid:
    #HighestBid = BidAmount
    #Winner = Bidder

print(f"The winner is {HighestBid1} with a bid of ${HighestBid2}.")