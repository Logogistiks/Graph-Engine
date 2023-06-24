# Implementation of a directed multigraph permitting loops

from random import randint, sample

class Node:
    def __init__(self, value=0, parents=[], childs=[]):
        self.value = value
        if parents == []:
            self.parents = []
        else:
            self.parents = [] + parents
            for x in parents:
                x.register_child(self)

        if childs == []:
            self.childs = []
        else:
            self.childs = [] + childs
            for x in childs:
                x.register_parent(self)

    def register_value(self, val):
        self.value = val

    def register_parent(self, par):
        if par not in self.parents:
            self.parents.append(par)
        if self not in par.childs:
            par.register_child(self)

    def register_child(self, ch):
        if ch not in self.childs:
            self.childs.append(ch)
        if self not in ch.parents:
            ch.register_parent(self)

    def print_parents(self):
        for x in self.parents:
            print(x.value, "|", x)

    def print_childs(self):
        for x in self.childs:
            print(x.value, "|", x)

def get_graph(node, log=False):
    graph = []
    visited = set()
    queue = [node]
    
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            if log:
                graph.append(current_node.value)
            else:
                graph.append(current_node)
            visited.add(current_node)
            queue.extend(current_node.childs)
            queue.extend(current_node.parents)
    
    return graph

def generate_graph(n, tweak=6):
    nodes = [Node(value=i) for i in range(n)]

    # Randomly connect the nodes by assigning random parents and childs to each node
    for node in nodes:
        num_parents = randint(0, len(nodes)//tweak)
        num_childs = randint(0, len(nodes)//tweak)
        parent_indices = sample(range(len(nodes)), num_parents)
        child_indices = sample(range(len(nodes)), num_childs)
        for parent_index in parent_indices:
            node.register_parent(nodes[parent_index])
        for child_index in child_indices:
            node.register_child(nodes[child_index])
    return nodes