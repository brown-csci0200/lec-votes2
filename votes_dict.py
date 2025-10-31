def cast_vote(poll, for_option: str):
    if for_option not in poll["options"]:
        raise ValueError("Wrong option " + for_option)
    poll["votes"].append(for_option)

def count_votes(poll):
    return len(poll["votes"])

def count_votes_for(poll, for_option: str):
    total = 0

    for v in poll["votes"]:
        if v == for_option:
            total += 1

    return total

# Example of use
some_poll = {
    "name": "Favorite color?",
    "options": ["red", "green", "blue"],
    "votes": [],
}

print(some_poll)
cast_vote(some_poll, "red")
cast_vote(some_poll, "green")
print(count_votes(some_poll))