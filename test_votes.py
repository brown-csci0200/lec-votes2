from votes import PollRecord

def test_votes1():
    # create poll with options
    colors = ["red", "green", "blue"]
    p = PollRecord("What is your favorite color?", colors)

    # cast some votes
    p.cast_vote("green")
    p.cast_vote("red")
    p.cast_vote("green")

    # simple string representation (not strictly required for the test)
    print(p)

    # assertions
    assert p.count_votes_for("green") == 2
    assert p.count_votes() == 3

