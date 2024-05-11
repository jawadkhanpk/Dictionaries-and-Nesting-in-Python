# See flowchart in comment section of this commit
bids = {}
bidding_finished = False


def find_higest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is: {winner}, with a highest bid of: {highest_bid}")


while not bidding_finished:
    name = input("What is your name: ")
    price = int(input("What is your bid: $"))

    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        find_higest_bidder(bids)
        break
