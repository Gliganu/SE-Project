# states -> list(int)
# actions -> list(int)
# deltas -> dict( (state, action, futureState) -> probability )

class MDPFull:
    def __init__(self, states, actions, deltas):
        self.states = states
        self.actions = actions
        self.deltas = deltas
        
# helper function:
# sums all transition probabilities given
# markov decision process mdp, from chosen
# state s and action act with estimated 
# intermediate probabilities pEst        
def sumTrans(mdp, s, act, pEst):
    return sum(map(lambda sPrime: mdp.deltas(s, act, sPrime) * pEst[sPrime], mdp.states))

# main function computing value iteration on PrMin
def valIterQuantReachMin(mdp, S0min, S1min, epislon):
    # initialise first guess probabilities
    # in articles this is denoted as 'xs'
    p = { s: 0 for s in mdp.states } # all zero
    for s in S1min:
        p[s] = 1
    
    #init done, now start value iteration
    leastChange = epsilon + 1 # first ensure we enter the iteration
    
    unknowns = [s in mdp.states if (s not in S1min and s not in S0min) ]
    while leastChange > epsilon:
        # first compute real updates    
        pUpdate = {}
        for s in unknowns:
            pUpdate[s] = min(map(mdp.actions,  lambda act: sumTrans(mdp, s, act, p)))
            
        # now test for stop criterion
        leastDelta = min([abs(p[s] - pUpdate[s]) for s in unknowns ])
        
        # also update our probabilities
        for s in unknowns:
            p[s] = pUpdate[s]
    
    # iteration done, return resulted probs
    return p
    
# main function computing value iteration on PrMax
def valIterQuantReachMax(mdp, S0max, S1max, epislon):
    # initialise first guess probabilities
    # in articles this is denoted as 'xs'
    p = { s: 0 for s in mdp.states } # all zero
    for s in S1max:
        p[s] = 1
    
    #init done, now start value iteration
    leastChange = epsilon + 1 # first ensure we enter the iteration
    
    unknowns = [s in mdp.states if (s not in S1max and s not in S0max) ]
    while leastChange > epsilon:
        # first compute real updates    
        pUpdate = {}
        for s in unknowns:
            pUpdate[s] = max(map(mdp.actions,  lambda act: sumTrans(mdp, s, act, p)))
            
        # now test for stop criterion
        leastDelta = min([abs(p[s] - pUpdate[s]) for s in unknowns ])
        
        # also update our probabilities
        for s in unknowns:
            p[s] = pUpdate[s]
    
    # iteration done, return resulted probs
    return p
    
def example6():
    stateLabels = { 0: "init", 1: "run", 2: "succ", 3: "fail" }
    states = { v: k for k, v in stateLabels.items() }
    
    actionLabels = { 0: "go", 1: "safe", 2: "risk", 3: "stop", 4: "finish" }
    actions = { v: k for k, v in actionLabels.items() }
    
    # init all combinations to zero
    deltas = { (s, a, sprime): 0 for s in states for a in actions for sprime in states }
    
    # state 0 transitions
    deltas[(states["init"], actions["go"], states["run"])] = 1 
    
    # state 1, action 1 transitions
    deltas[(states["run"], actions["safe"], states["init"])] = 0.6
    deltas[(states["run"], actions["safe"], states["succ"])] = 0.3
    deltas[(states["run"], actions["safe"], states["fail"])] = 0.1
    
    # state 1, action 2 transitions
    deltas[(states["run"], actions["risk"], states["fail"])] = 0.5
    deltas[(states["run"], actions["risk"], states["succ"])] = 0.5    
    
    # state 2, action 4 transition 
    deltas[(states["succ"], actions["finish"], states["succ"])] = 1.0    
   
    # state 3, action 3 transition 
    deltas[(states["fail"], actions["stop"], states["fail"])] = 1.0
    
    mdp = MDPFull([s for name, s in states], [a for name, a in actions], deltas)
    
    S0max = [states["fail"]]
    S1max = [states["succ"]]

    epsilon = 0.01
    
    probs = valIterQuantReachMax(mdp, S0max, S1max, epislon)
    
    print(probs)
    
    
    
    
    
    
    