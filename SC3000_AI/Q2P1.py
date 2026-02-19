import numpy as np
import pandas as pd
import json

from env import GridWorld
from value_iteration import ValueIteration
from policy_iteration import PolicyIteration

env = GridWorld()
vi_agent = ValueIteration(env)
pi_agent = PolicyIteration(env)

vi_agent.solve()

pi_agent.solve()
print("------- POLICY ITERATION -------")
print(pi_agent.V)
print(pi_agent.policy)
print("------- VALUE ITERATION -------")
print(vi_agent.V)
print(vi_agent.policy)