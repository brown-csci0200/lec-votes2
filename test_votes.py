# The file name for any testing file must begin with "test_"

# To run tests, we must import "pytest"
import pytest

import votes

# All test functions must begin with "test_"
def test_example():
    assert 2 == 1 + 1

def test_votes():
    p = votes.PollRecord("Do you like testing?",
                         ["yes", "of course"])
    p.cast_vote("yes")
    p.cast_vote("of course")
    assert 2 == p.count_votes()

    # Nothing in Python is "private", so all of the below also works.
    # That's not always a good thing, it needs we need to be more careful
    p.votes = ["no", "no"]
    assert 2 == len(p.votes)