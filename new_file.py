"""
Chalange: Write a Chrun Simulator:
=================================

- start with a single customer in a random initial state (A, B, C)
    * What data type to use for the customer state?
- Change the state randomly using a transition probability matrix PendingDeprecationWarning
    * That values to use for the probability matrix?
    * What data type to use for the probability matrix?
- Simulate N times stepy in the same way
- write the sequence of states to an output file
    * What is the overall structure of the program?

---------------------------------

- Do the same but for M customers
- Add new customers to the system at every time step

---------------------------------

OPTIONAL:

- Price the products, estimate customer lifetime value (CLV )
- Plot the number of customers in each state
- Try to find a steady state

- idealisiert OR wo gehen sie wirklich hin () - customer lifetime value

"""
from numpy import array, mat

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

if __name__ == "__main__":
    Q = ['A','B','C', 'F']
    SNULL = array([10,10,10,10])
    #s_0 = SNULL
    TIMESTEPS = 10
    PROBABILITYMATRIX = array(mat('0.7 0.1 0.1 0.1; 0.005 0.89 0.1 0.005;\
                                        0.00 0.00 0.8 0.2; 0.01 0.03 0.3 0.66'))#, subok=True)

    result = markov_chain(SNULL, TIMESTEPS, PROBABILITYMATRIX)
    print(result)
