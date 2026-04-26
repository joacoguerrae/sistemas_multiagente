# Eliminación de estrategias estricta y débilmente dominadas

import numpy as np

def players(G) :
    return G.keys()

def actions(G, p) :
    nact = G[p][1].shape[0]
    acts = np.arange(0, nact)
    return acts

def dominates(u, v, strict = False) :
    if strict :
        return np.all(np.greater(u, v))
    else :
        all_ge = np.all(np.greater_equal(u, v))
        one_gt = np.any(np.greater(u, v))
        return all_ge and one_gt

def equivalent(u, v) :
    return np.all(np.equal(u, v))

def weakdominates_or_eq(u, v) :
    return dominates(u, v) or equivalent(u, v)

def dominant(G, p, i, strict = False) :
    acts = actions(G, p)
    acts = acts[acts != i]
    if strict :
        return np.all([dominates(G[p][0][i], G[p][0][j], strict) for j in acts])
    else :
        return np.all([weakdominates_or_eq(G[p][0][i], G[p][0][j]) for j in acts])

def player_dominant(G, p, strict = False) : 
    acts = actions(G, p)
    is_dominant = list(map(lambda i : dominant(G, p, i, strict), acts))
    return acts[is_dominant]

def game_dominant(G, strict = False) :
    return dict(map(lambda p : (p, player_dominant(G, p, strict)), players(G)))

def dominated(G, p, i, strict = False) :
    acts = actions(G, p)
    acts = acts[acts != i]
    return np.any([dominates(G[p][0][j], G[p][0][i], strict) for j in acts])    

def player_dominated(G, p, strict = False) : 
    acts = actions(G, p)
    is_dominated = list(map(lambda i : dominated(G, p, i, strict), acts))
    return acts[is_dominated]

def update_game(G, p, dominated_acts) :  
    for q in players(G) :
        if q == p :
            _actions = np.delete(G[q][1], dominated_acts)
            axis = 0
        else :
            _actions = G[q][1]
            axis = 1
        _rewards = np.delete(G[q][0], dominated_acts, axis = axis)
        G[q] = (_rewards, _actions)
    return G

def delete_strict_dominated(G, p) : # in place
    dominated_acts = player_dominated(G, p, strict = True)
    to_delete = dominated_acts.size != 0
    if to_delete :
        G = update_game(G, p, dominated_acts)
    return to_delete

def IDSDS(G0, verbose = False) :
    G = G0.copy()
    it = 1
    while True :
        cont = np.any(list(map(lambda p : delete_strict_dominated(G, p), players(G))))
        if verbose :
            print('-- ' + str(it) + '\n', G)
        if not cont :
            break
        it += 1
    return G

def delete_weakly_dominated(G) : # in place
    dominated_acts = list(map(lambda p : player_dominated(G, p, strict = False), players(G)))
    to_delete = False
    for i, p in enumerate(players(G)) :
        if dominated_acts[i].size != 0 :
            to_delete = True
            G = update_game(G, p, dominated_acts[i])
    return to_delete

def IDWDS(G0, verbose = False) :
    G = G0.copy()
    it = 1
    while True :
        cont = delete_weakly_dominated(G)
        if verbose :
            print('-- ' + str(it) + '\n', G)
        if not cont :
            break
        it += 1
    return G
