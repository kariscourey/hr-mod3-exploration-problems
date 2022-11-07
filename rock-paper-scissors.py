class Node:

    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

    def __str__(self):

        return ("Node { value: '" + str(self.value)
                + "', link: " + str(self.link) + " }")


p = Node("paper")
r = Node("rock")
s = Node("scissors")

p.link = r

# place your code below
r.link = s
