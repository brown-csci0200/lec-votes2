from votes import PollRecord

topic = "Favorite flavor?"
finished_polls = list()

def reset_poll(options: list[str]):
    curr_poll = PollRecord(topic, options)

curr_poll = PollRecord(topic, ["pumpkin", "chocolate", "vanilla"])
print(curr_poll)

curr_poll.cast_vote("chocolate")
curr_poll.cast_vote("vanilla")
curr_poll.cast_vote("chocolate")


reset_poll(["strawberry", "mint", "cookie dough"])
print(curr_poll)


