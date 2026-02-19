import numpy as np

class ValueIteration:
    def __init__ (self, env):
        self.env = env
        self.gamma = 0.9
        self.V = np.zeros((env.height , env.width))
        # Converge threshold
        self.theta = 0.004
        # Policy of gridworld in terms of "↑", "↓", "←", "→"
        self.policy = np.full((self.env.height, self.env.width), ' ', dtype=object)

    def solve(self):
        for _ in range(1000):
        # while True:
            delta = 0
            v_new = self.V.copy()

            # Loop through all states
            for s in self.env.get_states():
                # Skip if state is terminal or block
                if s == self.env.goal: 
                    self.policy[s] = '*'
                    continue    
                elif s in self.env.blocks:
                    self.policy[s] = '■'
                    continue

                # Store Q value (up, down, left ,right) for state s
                q_value = []
                # Store old V value for delta calculation
                v_old = self.V[s[0], s[1]]

                # Loop through all possible actions in state s
                for a in self.env.actions:
                    # calculate Q value for action a
                    # Get reward and next state after taking action a in state s
                    reward, next_s = self.env.transition(s, a)
                    
                    # Deterministic action value
                    action_value = reward + (self.gamma * self.V[next_s[0]][next_s[1]])
                    # Store action value 
                    q_value.append(action_value)

                    if q_value:
                        v_new[s[0], s[1]] = max(q_value)

                    # Update V to the best action value in state s
                    delta = v_old - v_new[s[0], s[1]]
                # Convert highest action value to "↑", "↓", "←", "→"
                best_action_idx = np.argmax(q_value)
                
                # Update policy
                self.policy[s] = self.env.action_names[best_action_idx]


            self.V = v_new
            # if delta < self.theta:
            #     break
