import numpy as np

def players(G) :
    return G.keys()

def actions(G, p) :
    nact = G[p][1].shape[0]
    acts = np.arange(0, nact)
    return acts

def superior(u, v, strict = False) :
    if strict :
        return np.all(np.greater(u, v))
    else :
        all_ge = np.all(np.greater_equal(u, v))
        one_gt = np.any(np.greater(u, v))
        return all_ge and one_gt
