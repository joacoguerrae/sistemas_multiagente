import numpy as np
from itertools import permutations

def players(G) :
    return G.keys()

def num_actions(G, p) :
    return G[p][1].shape[0]

def actions(G, p) :
    nact = num_actions(G, p)
    acts = np.arange(0, nact)
    return acts

def R(G, p) :
    return G[p][0]

def FP(G, niter = 1, initial = {}, verbose = False) :
    np.random.seed(117)
    
    # inicializar count 
    count = initial
    if count == {} : 
        count = dict([(p, None) for p in players(G)])
        for p, q in permutations(players(G), r = 2) :
            count[p] = np.round(np.random.random(num_actions(G, q)) * 10 + 1)      
    
    # inicializar freq, V y br
    freq = dict([(p, None) for p in players(G)])     
    V = dict([(p, 0) for p in players(G)])
    br = dict([(p, 0) for p in players(G)])

    # fictitious play
    for t in range(niter) :
        if verbose :
            print('iter: ' + str(t))
            print('  count: ', count)
        for p in players(G) :
            freq[p] = count[p] / np.sum(count[p])
            # calcular valor
            V[p] = np.matmul(R(G, p), freq[p])
            # calcular best response
            br[p] = np.argmax(V[p])
        if verbose:
            print('  freq:  ', freq)
            print('  valor: ', V)
            print('  BR:    ', list(map(lambda p : G[p][1][br[p]], players(G))))
        # actualizar count
        for p, q in permutations(players(G), r = 2) :
            count[p] = count[p] + np.array([1 if br[q] == u else 0 for u in actions(G, q)])

    # devolver estrategia
    policy = {}
    for p, q in permutations(players(G), r = 2) :
        policy[p] = freq[q]
    return policy
    