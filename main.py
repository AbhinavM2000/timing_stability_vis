import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Data for the graph
num_runs = np.array([1, 2, 3,4,5])
wns = np.array([-0.042, -0.035, -0.01,0.01,-0.01])  # WNS values
tns = np.array([-10.568, -2.186, -0.01,0.01,-0.01])  # TNS values

# Calculate percentage changes
wns_percent_change = np.diff(wns) / wns[:-1] * 100  # Percentage change for WNS
tns_percent_change = np.diff(tns) / tns[:-1] * 100  # Percentage change for TNS

# Plotting the data
plt.figure(figsize=(8, 6))

# Plot WNS and TNS with increased line width
plt.plot(num_runs, wns, label='WNS', color='lightcoral', linestyle='-', marker='o', linewidth=2)
plt.plot(num_runs, tns, label='TNS', color='skyblue', linestyle='-', marker='o', linewidth=2)

# Add percentage change labels with offsets
wns_offset = +0.15  # Vertical offset for WNS labels
tns_offset = -0.55  # Vertical offset for TNS labels

for i in range(len(num_runs)):
    # Determine color for WNS
    if i > 0:
        wns_color = 'green' if wns[i] > wns[i - 1] else 'red'
        wns_label = f'{"↑" if wns[i] > wns[i - 1] else "↓"} {abs(wns_percent_change[i - 1]):.2f}%'
    else:
        wns_color = 'black'  # No change for the first point
        wns_label = f'{wns[i]:.3f}'

    # Adjust WNS label position to avoid overlap
    plt.text(num_runs[i], wns[i] + wns_offset, wns_label, 
             color=wns_color, 
             fontsize=10, ha='center', va='bottom', 
             bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.3'))

    # Determine color for TNS
    if i > 0:
        tns_color = 'green' if tns[i] > tns[i - 1] else 'red'
        tns_label = f'{"↑" if tns[i] > tns[i - 1] else "↓"} {abs(tns_percent_change[i - 1]):.2f}%'
        # Adjust TNS label position to avoid overlap
        plt.text(num_runs[i], tns[i] + tns_offset, tns_label, 
                 color=tns_color, 
                 fontsize=10, ha='center', va='bottom', 
                 bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.3'))

# Labels and title with increased font size
plt.xlabel('# of runs', fontsize=14)
plt.ylabel('Slack (ns)', fontsize=14)
plt.title('RCT 17X6 PROJECT STABILITY ACROSS RUNS', fontsize=16)

# Set x-ticks to integers and increase font size
plt.xticks(num_runs, fontsize=12)
plt.yticks(fontsize=12)

# Legend with increased font size
plt.legend(fontsize=12, loc='lower left')

# Create an inset for the zoomed view
ax_inset = inset_axes(plt.gca(), width="30%", height="30%", loc='lower right', borderpad=2)

# Plot the zoomed-in view
ax_inset.plot(num_runs, wns, color='lightcoral', linestyle='-', marker='o', linewidth=2)
ax_inset.plot(num_runs, tns, color='skyblue', linestyle='-', marker='o', linewidth=2)

# Set limits for the inset to zoom in on the desired range
ax_inset.set_ylim(-0.05, 0.2)  # Set limits for the zoomed-in axis
ax_inset.set_xlim(1, 5)         # Focus on the relevant runs

# Add green line at y = 0 in the inset
ax_inset.axhline(0, color='green', linestyle='--', linewidth=1, label='Timing Met')

# Add grid to the inset for better visibility
ax_inset.grid(True)

# Add legend for the inset
ax_inset.legend(fontsize=8, loc='upper left')

# Show the plot
plt.tight_layout()  # Adjust layout to make room for labels
plt.show()
