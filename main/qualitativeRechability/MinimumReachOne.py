



def allChildrenAreInReachableStates(currentState, possibleChildStates, reachableStates, probabilitiesDict):

    # all the children from the current state belong to the reachable states
    if not set(reachableStates).issuperset(set(possibleChildStates)):
        return False

    # all the probabilities to the children are greater than 0

    for childState in possibleChildStates:
        if (currentState, childState) not in probabilitiesDict:
            return False

        if probabilitiesDict[(currentState, childState)] <= 0 :
            return False


    return True


def performMinimumReachabilityOne(mdp, minReachZeroStates):
    """

    :param mdp: the markov decision proces
    :param minReachZeroStates: the minimum reachability zero states associated with the target states
    :param targetState: the states we want to end up in
    :return: the states from which we are have a P = 100% to reach the target states
    """

    reachableStates = list(set(mdp.states) - set(minReachZeroStates))

    parentStateToChildStateDict = mdp.actions

    probabilitiesDict = mdp.probabilities

    #force entry in while
    statesToBeCut = [1]

    while statesToBeCut:

        statesToBeCut = []

        for currentState in reachableStates:
            possibleChildStates = parentStateToChildStateDict[currentState]


            if not allChildrenAreInReachableStates(currentState,possibleChildStates, reachableStates, probabilitiesDict):
                statesToBeCut.append(currentState)


        reachableStates = list(set(reachableStates) - set(statesToBeCut))


    #todo should left the state itself be in the final set ?
    return reachableStates
