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
import imageio

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

    nx.drawing.nx_pydot.write_dot(G, f'markov{time+100}.dot')

    os.system(f' dot -Tpng markov{time+100}.dot -o markov{time+100}.png')

    if plot_it: os.system(f' open markov{time+100}.png')

    os.system(f' rm markov{time+100}.dot')

#
#####
#
def markov_chain(s_0,time_steps, P):
    """
        returns the state transitions for n time_steps
        s_n = s_0 o P^n
    """
    check_size_Q_P(s_0,P)
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
def gif_maker(file_path, gif_name='result007',frames=3, kill=False):
    """
        GIF MAKER for PNG in current directory
    """
    images = []
    file_names = []
    for fn  in os.listdir(file_path):
        #not needed, because they are now in a seperated directory
        if fn.endswith(".png"):
            file_names.append(fn)
        else:
            continue
    file_names.sort()

    for name in file_names:
        image = imageio.imread(file_path+name)
        images.append(image)

    imageio.mimsave(f'{gif_name}.gif', images, fps=frames)
    if kill:
        os.system('rm *.png')

def check_size_Q_P(Q,P):
    """
        why doesnt it work?
        -> float is not perfect on binary !!
    """

    a = np.ones(len(Q))
    b = P.sum(axis=1)
    a = a.round(3)
    b = b.round(3)
    assert np.all(a==b, axis=0)




if __name__ == "__main__":
    FULL_PATH = './'
    Q = ['Ananas','Banana','Coconut', 'Paneapple', 'Chicken']
    SNULL = np.array([100,100,100,100, 100])
    #s_0 = SNULL
    TIMESTEPS = 120
    PROBABILITYMATRIX = np.array(np.mat('0.7 0.1 0.1 0.1 0.0; 0.105 0.69 0.05 0.15 0.005;\
                                        0.075 0.125 0.7 0.05 0.05; 0.01 0.055 0.825 0.05 0.06; 0.1 0.4 0.4 0.1 0.0'))#, subok=True)

    #e, w, s = edges_weights_specified_state(PROBABILITYMATRIX, Q, SNULL)
    #save_graph_as_png(e,w,s, 32, plot_it=True)


    multi_graph_as_png(TIMESTEPS,PROBABILITYMATRIX,Q,SNULL)
    gif_maker(FULL_PATH, kill=True)
