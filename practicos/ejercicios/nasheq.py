import numpy as np
from itertools import product, combinations

def players(G) :
    return G.keys()

def actions(G, p) :
    nact = G[p][1].shape[0]
    acts = np.arange(0, nact)
    return acts

def BR(G, p, a_p, a_q) :
    return np.all(G[p][0][a_p, a_q] >= G[p][0][:, a_q])

def is_nash(G, p, a_p, q, a_q) :
    return BR(G, p, a_p, a_q) and BR(G, q, a_q, a_p)

def nash(G) :
    nash_eqs = []
    for p, q in combinations(players(G), r = 2) :
        for a_p, a_q in product(actions(G, p), actions(G, q)) :
            if is_nash(G, p, a_p, q, a_q) :
                nash_eqs.append(np.array([G[p][1][a_p], G[q][1][a_q]]))
    return nash_eqs