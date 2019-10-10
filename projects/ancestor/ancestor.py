

# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # Build edges in reverse
#         graph.add_edge(pair[1], pair[0])
#     # Do a BFS (storing the path)
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = v
#             max_path_len = len(path)
#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.length() > 0:
            return self.queue.pop(0)
        else:
            return None

    def length(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 in self.vertices:
            raise IndexError("Vertex 2 does not exist!")
        elif v2 in self.vertices:
            raise IndexError("Vertex 1 does not exist!")
        else:
            raise IndexError("Those vertices do not exist!")


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    queue = Queue()
    for pair in ancestors:
        parent, child = pair[0], pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    # instigate a bfs
    queue.enqueue([starting_node])
    longest_path = 1
    earliest_ancestor = -1
    while queue.length() > 0:
        print(f"Queue: {queue.queue}")
        path = queue.dequeue()
        print(f"Path: {path}")
        last_node = path[-1]
        if (len(path) >= longest_path and last_node < earliest_ancestor) or len(path) > longest_path:
            longest_path = len(path)
            earliest_ancestor = last_node
            print(
                f"CHANGING THE LONGEST PATH AND EARLIEST ANCESTOR to {earliest_ancestor}")
        for parent in graph.vertices[last_node]:
            path_copy = list(path)
            path_copy.append(parent)
            queue.enqueue(path_copy)
    print(earliest_ancestor)
    print("-   -   -   -   -   -   -   -   -   -   -   -   ")
    return earliest_ancestor

    '''
    parents
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \ 
        6   7   9
    children
    '''


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)
earliest_ancestor(test_ancestors, 2)
earliest_ancestor(test_ancestors, 3)
earliest_ancestor(test_ancestors, 4)
earliest_ancestor(test_ancestors, 5)
earliest_ancestor(test_ancestors, 6)
earliest_ancestor(test_ancestors, 7)
earliest_ancestor(test_ancestors, 8)
earliest_ancestor(test_ancestors, 9)
earliest_ancestor(test_ancestors, 10)
earliest_ancestor(test_ancestors, 11)
