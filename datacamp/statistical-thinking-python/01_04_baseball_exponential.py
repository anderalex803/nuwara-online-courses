def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # tau1, tau2 waiting times for no-hitter and hit-the-cycle baseball events
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2
 
# Draw samples of waiting times: waiting_times
# waiting time for no-hitter, tau1 = 764 games
# waiting time for hit-the-cycle, tau2 = 715 games
waiting_times = successive_poisson(764, 715, size=100000)

# Make the histogram
plt.hist(waiting_times, bins=100, normed=True, histtype='step')

# Label axes
plt.xlabel('waiting times')
plt.ylabel('probability')

# Show the plot
plt.show()
