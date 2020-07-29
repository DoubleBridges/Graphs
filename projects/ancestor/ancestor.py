from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for (parent, child) in ancestors:
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    paths = graph.dft_recursive(starting_node)
    longest = len(sorted(paths, key=len)[-1])
    longest_paths = list(filter(lambda path: len(path) == longest, paths))

    if longest == 1:
        return -1

    if len(longest_paths) > 1:
        ancestors = []
        for path in longest_paths:
            ancestors.append(path[-1])
        return min(ancestors)

    else:
        return longest_paths[-1][-1]


# test_ancestors = [
#     (1, 3),
#     (2, 3),
#     (3, 6),
#     (5, 6),
#     (5, 7),
#     (4, 5),
#     (4, 8),
#     (8, 9),
#     (11, 8),
#     (10, 1),
# ]

# print(earliest_ancestor(test_ancestors, 6))
