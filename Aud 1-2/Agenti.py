class Agent:
    def __init__(self, x=0):
        self.x = x

    def move(self):
        pass

    def __repr__(self):
        return f"Agent: {self.x}"


class LeftAgent(Agent):
    def __init__(self, x=0):
        super().__init__(x)

    def move(self):
        self.x -= 1


class RightAgent(Agent):
    def __init__(self, x=0):
        super().__init__(x)

    def move(self):
        self.x += 1


if __name__ == '__main__':
    left_agent = LeftAgent(5)
    right_agent = RightAgent(8)
    print("Pred dvizenje: ")
    print(left_agent.__repr__() + " " + right_agent.__repr__())
    for i in range(10):
        left_agent.move()
        right_agent.move()
    print("Posle dvizenje: ")
    print(left_agent.__repr__() + " " + right_agent.__repr__())
