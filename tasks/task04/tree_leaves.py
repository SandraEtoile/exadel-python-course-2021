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


def collect_leaves(tree):
    leaves = []
    for k, v in tree.items():
        if isinstance(v, dict):
            leaves.extend(collect_leaves(v))
        else:
            leaves.extend(v)
    return leaves


print(collect_leaves(tree))


assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]