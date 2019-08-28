"""Test for Markov Graph."""

import os
import numpy as np
from markov_graph import (
    edges_weights_specified_state,
    save_graph_as_png,
    markov_chain,
    multi_graph_as_png,
)

FULL_PATH = './'
MARKET = ['Apple', 'Banana', 'Coconut']
SNULL = np.array([100, 100, 100])
TIMESTEPS = 30
PROBABILITYMATRIX = np.array(np.mat('0.7 0.1 0.2; \
                                      0.69 0.01 0.3;\
                                      0.2 0.7 0.1'))


def test_edges_and_weights():
    """
    Testing if the size fits the task.

    between each states are edges with weights.
    """
    edges, weights, state_value = edges_weights_specified_state(
        PROBABILITYMATRIX,
        MARKET,
        SNULL)
    assert len(edges) == len(weights) == (len(state_value)**2)


def test_multi_graph():
    """
    Testing the Multi-Graph.

    Testing that the amount of the creates images are
    the same as the amount of the timesteps.
    """
    multi_graph_as_png(TIMESTEPS, PROBABILITYMATRIX, MARKET, SNULL)
    counter = 0
    for f_name in os.listdir('./'):
        if f_name.endswith(".png"):
            counter += 1
            os.remove(f_name)
    assert counter == TIMESTEPS


def test_markov_chain():
    """Testing the changes between the timestemps."""
    amount = len(markov_chain(SNULL, TIMESTEPS, PROBABILITYMATRIX))
    assert TIMESTEPS == amount
