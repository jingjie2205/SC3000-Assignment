import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

    def plot_gridworld(values, policy, title="RL Gridworld Results"):
        rows, cols = values.shape
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Create the basic grid lines
        ax.set_xticks(range(cols + 1))
        ax.set_yticks(range(rows + 1))
        ax.grid(True, color='black', linewidth=2)
        
        # Remove axis labels and ticks for a cleaner look
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        
        for r in range(rows):
            for c in range(cols):
                # Display Value (top-center of cell)
                val_text = f"{values[r, c]:.2f}"
                ax.text(c + 0.5, rows - r - 0.3, val_text, 
                        va='center', ha='center', fontsize=12)
                
                # Display Policy/Symbol (bottom-center of cell)
                symbol = policy[r, c]
                # Color coding symbols for better visibility without background colors
                color = 'red' if symbol in ['*', '■'] else 'blue'
                ax.text(c + 0.5, rows - r - 0.7, symbol, 
                        va='center', ha='center', fontsize=22, 
                        fontweight='bold', color=color)

        plt.title(title, pad=20, fontsize=15)
        
        # Adjust limits to show the full grid
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)
        plt.show()
