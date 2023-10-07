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


class DisjointSetsForNonIntegerLabels:
    def __init__(self, labels, predefined_mapping):
        self.label_to_int = predefined_mapping
        self.int_to_label = {v: k for k, v in predefined_mapping.items()}
        self.p = [predefined_mapping[label] for label in labels]  # Initialize based on the predefined mapping
        self.rank = [0] * len(labels)

    def findset(self, label):
        u = self.label_to_int[label]
        if self.p[u] == u:
            return label
        else:
            self.p[u] = self.findset(self.int_to_label[self.p[u]])
            return self.int_to_label[self.p[u]]

    def union(self, label_u, label_v):
        u = self.label_to_int[label_u]
        v = self.label_to_int[label_v]
        a = self.findset(label_u)
        b = self.findset(label_v)
        if self.rank[a] < self.rank[b]:
            self.p[u] = v
        else:
            self.p[v] = u
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


# Example usage with labels and a predefined mapping
fruit_labels = ["apple", "banana", "orange"]
predefined_mapping = {"apple": 0, "banana": 1, "orange": 2}
djs = DisjointSetsForNonIntegerLabels(fruit_labels, predefined_mapping)

# Initial state
for label in fruit_labels:
    print(f"{label} belongs to Set with Representative {djs.findset(label)}")

# Union operations with labels
djs.union("banana", "orange")
print("\nUnion('banana', 'orange') => Merge sets containing 'banana' and 'orange'.")
print(f"'banana' now belongs to Set with Representative {djs.findset('banana')}")
print(f"'orange' now belongs to Set with Representative {djs.findset('orange')}")

djs.union("apple", "banana")
print("\nUnion('apple', 'banana') => Merge sets containing 'apple' and 'banana'.")
print(f"'apple' now belongs to Set with Representative {djs.findset('apple')}")
print(f"'banana' now belongs to Set with Representative {djs.findset('banana')}")