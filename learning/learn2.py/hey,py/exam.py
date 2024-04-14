# import numpy as np
# from sklearn.cluster import KMeans

# # Given dataset
# D = [2, 3, 4, 10, 11, 12, 20, 25, 30]
# data = np.array(D).reshape(-1, 1)  # Reshape the data for KMeans

# # Create a KMeans model with K=2
# kmeans = KMeans(n_clusters=2, random_state=0)

# # Fit the model to the data
# kmeans.fit(data)

# # Get the cluster assignments for each data point
# cluster_assignments = kmeans.labels_

# # Get the cluster centroids
# centroids = kmeans.cluster_centers_

# # Display the results
# for i in range(len(D)):
#     print(f"Data point {D[i]} belongs to Cluster {cluster_assignments[i]}")

# print(f"Centroids: {centroids}")



# import numpy as np
# from sklearn.cluster import KMeans

# # Data - Ages of website visitors
# ages = np.array([10, 9 , 16, 15, 13 , 20, 25,35,17,18,21,32,11,30]).reshape(-1, 1)

# # Initial centroids
# initial_centroids = np.array([[10], [20]])

# # Create a KMeans model with K=2 and use the initial centroids
# kmeans = KMeans(n_clusters=2, init=initial_centroids, n_init=1, random_state=0)

# # Fit the model to the data
# kmeans.fit(ages)

# # Get the cluster assignments for each age
# cluster_assignments = kmeans.labels_

# # Get the cluster centroids
# centroids = kmeans.cluster_centers_

# # Display the results
# for i in range(len(ages)):
#     print(f"Age {ages[i][0]} belongs to Group {cluster_assignments[i] + 1}")

# print(f"Cluster Centroids: {centroids}")




from collections import defaultdict

# Given dataset
dataset = [
    ["Apple", "Berries", "Coconut"],
    ["Berries", "Coconut", "Dates"],
    ["Coconut", "Dates"],
    ["Berries", "Dates"],
    ["Apple", "Coconut"],
    ["Apple", "Coconut", "Dates"],
]

# Minimum support threshold
min_support = 0.3 * len(dataset)

# Step 1: Data Preprocessing
transactions = [set(transaction) for transaction in dataset]

# Step 2: Count Item Frequencies
item_counts = defaultdict(int)
for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1

# Step 3: Filter Items by Minimum Support
frequent_items = [item for item, count in item_counts.items() if count >= min_support]

# Step 4: Sort Items by Frequency
frequent_items.sort(key=lambda item: item_counts[item], reverse=True)

# Step 5: Create the FP-Tree
class Node:
    def __init__(self, item, count):
        self.item = item
        self.count = count
        self.children = []

def insert_tree(node, items):
    if not items:
        return
    for child in node.children:
        if child.item == items[0]:
            child.count += 1
            insert_tree(child, items[1:])
            return
    new_child = Node(items[0], 1)
    node.children.append(new_child)
    insert_tree(new_child, items[1:])

root = Node("null", 0)  # Create the root node
for transaction in transactions:
    ordered_items = [item for item in frequent_items if item in transaction]
    insert_tree(root, ordered_items)

# Step 6: Mine Frequent Itemsets
def mine_fp_tree(node, prefix, frequent_itemsets):
    if node.item != "null":
        prefix.append(node.item)
        frequent_itemsets.append((prefix.copy(), node.count))
    for child in node.children:
        mine_fp_tree(child, prefix.copy(), frequent_itemsets)

frequent_itemsets = []
mine_fp_tree(root, [], frequent_itemsets)

# Display frequent itemsets
for itemset, support in frequent_itemsets:
    if support >= min_support:
        print(f"Frequent Itemset: {', '.join(itemset)} (Support: {support}/{len(dataset)})")
