class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n
        
    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u,v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

# Example: create a DisjointSets instance with 5 elements.
djs = DisjointSets(5)

# Initial state, each element is its own parent
print("Step 1: Initial State")
for i in range(5):
    print(f"Element {i} belongs to Set with Representative {djs.findset(i)}")

# Merge sets containing elements 3 and 4
djs.union(3, 4)
print("\nStep 2: Union(3, 4) => Merge sets containing elements 3 and 4.")
print(f"Element 3 now belongs to Set with Representative {djs.findset(3)}")
print(f"Element 4 now belongs to Set with Representative {djs.findset(4)}")

# Merge sets containing elements 4 and 1.
djs.union(4, 1)
print("\nStep 3: Union(4, 1) => Merge sets containing elements 4 and 1.")
print(f"Element 4 now belongs to Set with Representative {djs.findset(4)}")
print(f"Element 1 now belongs to Set with Representative {djs.findset(1)}")

class DisjointSetsForNonIntegerLabels:
    def __init__(self, labels, predefined_mapping):
        self.label_to_set = {}  # Maps labels to sets
        self.set_to_label = {}  # Maps sets to labels
        self.rank = {}

        # Initialize each label as a separate set with rank 0
        for label in labels:
            self.label_to_set[label] = label
            self.set_to_label[label] = label
            self.rank[label] = 0

    def findset(self, label):
        # Find the representative (root) of the set containing the label
        current = label
        while current != self.label_to_set[current]:
            current = self.label_to_set[current]
        return current

    def union(self, label_u, label_v):
        root_u = self.findset(label_u)
        root_v = self.findset(label_v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] < self.rank[root_v]:
                self.label_to_set[root_u] = root_v
                self.set_to_label[root_v] = label_u
            elif self.rank[root_u] > self.rank[root_v]:
                self.label_to_set[root_v] = root_u
                self.set_to_label[root_u] = label_v
            else:
                self.label_to_set[root_v] = root_u
                self.set_to_label[root_u] = label_v
                self.rank[root_u] += 1


# Example usage with labels and a predefined mapping
fruit_labels = ["Label 1", "Label 2", "Label 3"]
predefined_mapping = {"Label 1": 0, "Label 2": 1, "Label 3": 2}
djs = DisjointSetsForNonIntegerLabels(fruit_labels, predefined_mapping)

# Initial state
for label in fruit_labels:
    print(f"{label} belongs to Set with Representative {djs.findset(label)}")

# Union operations with labels
djs.union("Label 2", "Label 3")
print("\nUnion('Label 2', 'Label 3') => Merge sets containing 'Label 2' and 'Label 3'.")
print(f"'Label 2' now belongs to Set with Representative {djs.findset('Label 2')}")
print(f"'Label 3' now belongs to Set with Representative {djs.findset('Label 3')}")

djs.union("Label 1", "Label 2")
print("\nUnion('Label 1', 'Label 2') => Merge sets containing 'Label 1' and 'Label 2'.")
print(f"'Label 1' now belongs to Set with Representative {djs.findset('Label 1')}")
print(f"'Label 2' now belongs to Set with Representative {djs.findset('Label 2')}")

