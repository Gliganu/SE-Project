from main.utils import Utils


def allActionsLeadToOrphanStates(parentForCurrentState, orphanStates, probabilitiesDict):


    for orphanState in orphanStates:
        if (parentForCurrentState, orphanState) not in probabilitiesDict:
            return False

        if probabilitiesDict[(parentForCurrentState, orphanState)] <= 0 :
            return False


    return True

def performMinimumReachabilityZero(mdp, targetStates):
    """

    :param mdp: Markov Decision Process which will be used
    :param targetStates:  the list of states in which we would want to end up it
    :return: the set of all states S such the Prob(S->T) = 0
    """

    reachableStates = targetStates
    orphanStates = targetStates

    childStateToParentStatesDict = Utils.createReverseActionDictionary(mdp.actions, mdp.states)

    probabilitiesDict = mdp.probabilities

    # random value to force enter in while loop
    parentStates = [1]

    # while list not empty
    while parentStates:

        parentStates = []

        for currentState in orphanStates:
            parentsForCurrentState = childStateToParentStatesDict[currentState]

            for parentForCurrentState in parentsForCurrentState:

                if allActionsLeadToOrphanStates(parentForCurrentState, orphanStates, probabilitiesDict):
                    parentStates.append(parentForCurrentState)



        # the found parents will be next iterations's orphan child states
        orphanStates = parentStates

        # add every node found to the final list
        reachableStates += parentStates


    allStates = mdp.states

    # the zero reachability nodes are the ones which do not belong
    # in the node list found going up the tree from the target states
    # todo maybe return as a tuple with target states ?
    return list(set(allStates) - set(reachableStates))



