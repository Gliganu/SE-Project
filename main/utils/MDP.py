

# states -> list(int)
# actions -> dict(state -> list ( possibleFutureStates ) )
#
# probabilities -> dict( (state,futureState) -> probability )
#
# rewards -> dict( (state,futureState) -> reward )
#
# discount -> integer

class MDP:
    def __init__(self, states, actions, probabilities, rewards, discount):
        self.states = states
        self.actions = actions
        self.probabilities = probabilities
        self.rewards = rewards
        self.discount = discount


    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y
