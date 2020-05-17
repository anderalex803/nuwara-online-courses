# Initialize array of replicates: perm_replicates
perm_replicates = ____

# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = ____
    perm_replicates[i] = ____


# Compute p-value: p
p = np.sum(____ >= ____) / len(____)

# Print the p-value
print('p-val =', p)
