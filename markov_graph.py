#!/usr/bin/env python
# coding: utf-8
"""
Directed Graph for Markov Chain.

Can make a directed graph.
Can make it multiple times for a GIF
"""

#####
#
#   IMPORTS
#
import os
import numpy as np
import networkx as nx


def edges_weights_specified_state(probabilities, states, amount):
    """
    Edges for a specific states are made.

    * probabilities is a Matrix P
    * states
    returns
    - the origin and the destiny node in edges
    - the weight for each edge
    - the new node names with the amount of starting s
    """
    edges = []
    weights = []
    state_value = []
    for index, (j, state, a) in enumerate(zip(probabilities, states, amount)):
        state_value.append((state+' ' + str(round(a, 3))))
        for index2, (i, state2) in enumerate(zip(j, states)):
            edges.append((state_value[index], state2 + ' ' + str(
                round(amount[index2], 3))))
            weights.append(i)
    return edges, weights, state_value


def save_graph_as_png(edges, weights, states, time, plot_it=False):
    """Markov Chain for each state will be saved as an PNG."""
    graph = nx.MultiDiGraph()
    graph.add_nodes_from(states)
    for e, w in zip(edges, weights):
        graph.add_edge(e[0], e[1], weight=w, label=w)

    nx.drawing.nx_pydot.write_dot(graph, f'markov{time+100}.dot')

    os.system(f' dot -Tpng markov{time+100}.dot -o markov{time+100}.png')

    if plot_it:
        os.system(f' open markov{time+100}.png')

    os.system(f' rm markov{time+100}.dot')


def markov_chain(s_0, time_steps, P):
    """Calculate the Property-Matrix."""
    check_size_Q_P(s_0, P)
    res = []
    for i in range(0, time_steps):
        if i == 0:
            res.append(s_0)
        else:
            res.append(res[i-1].dot(P))
    return res
#
#####
#


def multi_graph_as_png(time: int, P, Q, s_0):
    """Save an image for every discret time step from Markov Chain."""
    s_t = markov_chain(s_0, time, P)

    for s, t in zip(s_t, range(0, time)):
        ed, we, Qs = edges_weights_specified_state(P, Q, s)
        save_graph_as_png(ed, we, Qs, t)


def check_size_Q_P(Q, P):
    """Check if the size of Q and P is the same."""
    a = np.ones(len(Q))
    b = P.sum(axis=1)
    a = a.round(3)
    b = b.round(3)
    assert np.all(a == b, axis=0)


def ask_for_delete():
    """Delete or not delete is the Question."""
    try:
        ans = int(input('Wanna delete all PNGs in this Folder?\
                               \n\tPress 1 for Yes\n\tPress 0 for No: '))

        if ans == 1:
            for f_name in os.listdir('./'):
                if f_name.endswith(".png"):
                    os.remove(f_name)
            print('All PNGs deleted.')
        elif ans == 0:
            print('Kept all PNGs.')
        else:
            print('\nNot any number!\n')
            ask_for_delete()

    except ValueError:
        print('\nThe answere should be a 1 or a 0.\n')
        ask_for_delete()


if __name__ == "__main__":
    FULL_PATH = './'
    MARKET = ['Apple', 'Banana', 'Coconut']
    SNULL = np.array([100, 100, 100])
    TIMESTEPS = 30
    PROBABILITYMATRIX = np.array(np.mat('0.7 0.1 0.2; \
                                         0.69 0.01 0.3;\
                                         0.2 0.7 0.1'))

    multi_graph_as_png(TIMESTEPS, PROBABILITYMATRIX, MARKET, SNULL)
    # Delete all PNGs
    ask_for_delete()
