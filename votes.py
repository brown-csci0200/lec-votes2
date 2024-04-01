class PollRecord:
    def __init__(self, name: str, options: list[str]):
        self.name = name
        self.options = options
        self.votes = list()

    def cast_vote(self, for_option: str):
        if for_option in self.options:
            self.votes.append(for_option)
        else:
            raise RuntimeError("unknown")
        
    def count_votes(self):
        return len(self.votes)
        
    def count_votes_for(self, for_option: str):
        total = 0
        for v in self.votes:
            if v == for_option:
                total += 1
        return total
    
    def __str__(self) -> str:
        return "Poll for question " + self.name + ", choices: " + str(self.options)

option_list = ["red", "green", "blue"]
p = PollRecord("Favorite color?", option_list)
print(p)
p.cast_vote("red")
p.cast_vote("green")

print("Green has " + str(p.count_votes_for("green")) + " votes")
