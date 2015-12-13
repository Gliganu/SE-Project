from main.utils import Utils
from main.qualitativeRechability.MinimumReachZero import *
from main.qualitativeRechability.MinimumReachOne import *

def runAlgorithm():

    mdp = Utils.createMDP()

    targetStates = [6]

    zeroReachabilityStates = performMinimumReachabilityZero(mdp, targetStates)

    oneReachabilityStates = performMinimumReachabilityOne(mdp,zeroReachabilityStates)

    print "Zero reach {}".format(zeroReachabilityStates)
    print "One reach {}".format(oneReachabilityStates)



runAlgorithm()