tree = {
    "node1": {
        "node11": {
            "node111": [1, 2, 3],
            "node112": [4, 5]
        },
        "node12": [6]
    },
    "node2": [7, 8, 9]
}


flat_tree = [1, 2, 3]


def collect_leaves(x):
    leaves = []
    if isinstance(x, dict):
        for v in x.values():
            if isinstance(v, dict):
                leaves.extend(collect_leaves(v))
            else:
                leaves.extend(v)
    else:
        leaves.extend(x)
    return leaves


print(collect_leaves(tree))

print(collect_leaves(flat_tree))


assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert collect_leaves(flat_tree) == [1, 2, 3]
