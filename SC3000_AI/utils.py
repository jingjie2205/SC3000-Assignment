import matplotlib.pyplot as plt

def plot_rl_comparison(vi_v, vi_p, pi_v, pi_p):
    # Create a figure with 1 row and 2 columns of subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    def draw_single_grid(ax, values, policy, title):
        rows, cols = values.shape
        # Setup grid lines
        ax.set_xticks(range(cols + 1))
        ax.set_yticks(range(rows + 1))
        ax.grid(True, color='black', linewidth=1.5)
        
        # Hide standard axis labels
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_title(title, fontsize=16, pad=15)

        for r in range(rows):
            for c in range(cols):
                # Place Value (V) in the top half of the cell
                ax.text(c + 0.5, rows - r - 0.3, f"{values[r, c]:.2f}", 
                        va='center', ha='center', fontsize=11)
                
                # Place Policy Arrow in the bottom half
                symbol = policy[r, c]
                color = 'red' if symbol in ['*', '■'] else 'blue'
                ax.text(c + 0.5, rows - r - 0.7, symbol, 
                        va='center', ha='center', fontsize=20, 
                        fontweight='bold', color=color)
        
        ax.set_xlim(0, cols)
        ax.set_ylim(0, rows)

    # Draw both plots
    draw_single_grid(ax1, vi_v, vi_p, "Value Iteration Result")
    draw_single_grid(ax2, pi_v, pi_p, "Policy Iteration Result")
    
    plt.tight_layout() # Ensures titles and labels don't overlap
    plt.show()