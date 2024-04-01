class PollRecord:
    # We can include these type annotations, but Python doesn't enforce them
    # It will still allow us to pass in a "name" that isn't a str
    def __init__(self, name: str, options: list[str]):
        self.name = name
        self.options = options
        self.votes = list()

    def cast_vote(self, for_option: str):
        if for_option in self.options:
            self.votes.append(for_option)
        else:
            raise RuntimeError("unknown")
        
    def count_votes(self) -> int:
        return len(self.votes)
        
    def count_votes_for(self, for_option: str) -> int:
        total = 0
        for v in self.votes:
            if v == for_option:
                total += 1
        return total
    
    # This is equivalent to Java's toString() method
    # The double underscores at the beginning and end tell us that
    # "__str__" is a method name that Python has reserved for very specific functionality

    # In this case, this is the method name that tells Python how to represent PollRecord objects as strings,
    # which is used when we call print(). Otherwise by default, the output of print(p) would look like:
    # <__main__.PollRecord object at 0x7fd48865bfd0>
    def __str__(self) -> str:
        return "Poll for question " + self.name + ", choices: " + str(self.options)
        
        # We can write these string operations quicker with f-strings
        # return f"Poll for question {self.name}, choices: {self.options}"

option_list = ["red", "green", "blue"]
p = PollRecord("Favorite color?", option_list)
print(p)
p.cast_vote("red")
p.cast_vote("green")

print("Green has " + str(p.count_votes_for("green")) + " votes")

p2 = PollRecord(5, ["red", "green"])
# Python allows us to make PollRecords with the wrong type inputs,
# and only breaks below when we go to use them

# print(p2) # Should fail
