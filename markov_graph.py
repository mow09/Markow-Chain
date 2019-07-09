#!/usr/bin/env python
# coding: utf-8

"""

    Can make a directed graph
    Can make it multiple times for a GIF

"""

#####
#
#   IMPORTS
#
import numpy as np
#import matplotlib.pyplot as plt
import networkx as nx
import os

#####
#
#   FUNCTIONS
#
def edges_weights_specified_state(probabilities, states, amount):
    """
        * probabilities is a Matrix P
        * states


        returns
        - the origin and the destiny node in edges
        - the weight for each edge
        - the new node names with the amount of starting s
    """
    edges = []
    weights = []
    qs = []
    for index, (j, state, a) in enumerate(zip(probabilities,states, amount)):
        #print(state)
        qs.append((state+' '+ str(round(a,3))))
        for index2, (i, state2) in enumerate(zip(j,states)):
            edges.append((qs[index],state2+' '+ str(round(amount[index2],3))))
            weights.append(i)
    return edges, weights, qs
#
#####
#
def save_graph_as_png(edges,weights,states, time, plot_it=False):
    """
        creates a png of the graph and saves it
    """
    G = nx.MultiDiGraph()
    G.add_nodes_from(states)
    for e,w in zip(edges,weights):
        G.add_edge(e[0], e[1], weight=w, label=w)

    nx.drawing.nx_pydot.write_dot(G, f'markov{time}.dot')

    os.system(f' dot -Tpng markov{time}.dot -o markov{time}.png')

    if plot_it: os.system(f' open markov{time}.png')


    os.system(f' rm markov{time}.dot')

#
#####
#
def markov_chain(s_0,time_steps, P):
    """
        returns the state transitions for n time_steps
        s_n = s_0 o P^n
    """
    res = []
    for i in range(0,time_steps):
        if i == 0:
            res.append(s_0)
        else:
            res.append(res[i-1].dot(P))
    return res
#
#####
#
def multi_graph_as_png(time,P,Q,s_0):
    """
        saves an image for every discret time step from Markov Chain
    """
    s_t = markov_chain(s_0,time, P)

    for s,t in zip(s_t,range(0,time)):
        ed, we, Qs = edges_weights_specified_state(P,Q,s)
        save_graph_as_png(ed, we, Qs, t)
#
#####
#

def why():
    """
        why doesnt it work?
    """
    len(Q)


    a = np.ones(len(Q))


    b = P.sum(axis=1)


    a


    b


    a==b


    np.all(a==b, axis=0)


    #assert np.all(P.sum(axis=1) == np.ones(len(Q)))





if __name__ == "__main__":
    Q = ['A','B','C', 'F']
    SNULL = np.array([10,10,10,10])
    #s_0 = SNULL
    TIMESTEPS = 30
    PROBABILITYMATRIX = np.array(np.mat('0.7 0.1 0.1 0.1; 0.005 0.89 0.1 0.005;\
                                        0.00 0.00 0.8 0.2; 0.01 0.03 0.3 0.66'))#, subok=True)

    e, w, s = edges_weights_specified_state(PROBABILITYMATRIX, Q, SNULL)
    save_graph_as_png(e,w,s, 32, plot_it=True)


    multi_graph_as_png(TIMESTEPS,PROBABILITYMATRIX,Q,SNULL)