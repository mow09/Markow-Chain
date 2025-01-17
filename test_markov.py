"""Test for Markov Graph."""

import numpy as np
from markow_graph import (
    edges_weights_specified_state,
    markow_chain,
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


def test_markow_chain():
    """Testing the changes between the timestemps."""
    amount = len(markow_chain(SNULL, TIMESTEPS, PROBABILITYMATRIX))
    assert TIMESTEPS == amount
