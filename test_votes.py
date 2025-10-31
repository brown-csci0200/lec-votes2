from votes import PollRecord

def test_votes_class():
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


# Here is the original Java code for reference:
"""
public static void main(String[] args) {
       String[] colors = {"red", "green", "blue"};
       PollRecord p = new PollRecord("What is your favorite color?", colors);
       System.out.println(e);
       p.castVote("green");
       p.castVote("red");
       p.castVote("green");
       System.out.println(p);
       System.out.println("green has " + p.countVotesFor("green") + " votes");
   }
"""