from main.utils.MDP import MDP


def createMDP():

    states = range(8)

    actions = {0: [],
               1: [2],
               2: [0, 4, 5],
               3: [5],
               4: [],
               5: [6],
               6: [],
               7: [5]}



    #todo not sure if should have for every pair or just between pairs that have actions
    #todo also, are there cases when it shouldn't sum up to 1 ?
    probabilities = ({(1, 2): 1,
                      (2, 0): 0.2,
                      (2, 4): 0.3,
                      (2, 5): 0.5,
                      (3, 5): 0.75,
                      (5, 6): 1,
                      (7,5):1})


    # not needed at this point
    rewards = {}
    discount = 0

    return MDP(states,actions,probabilities,rewards,discount)


def createReverseActionDictionary(actionsDict,states):
    """

    :param states: the list of all the existing states
    :param actionsDict:  dict(initialState -> list ( possibleFutureStates ) )
    :return:  dict( possibleFutureState -> list ( initialStates ) )
    """

    inverseDictionary = {key: [] for key in states}

    for initialState, possibleFutureStates in actionsDict.iteritems():

        for possibleFutureState in possibleFutureStates:

            inverseDictionary[possibleFutureState].append(initialState)


    return inverseDictionary
