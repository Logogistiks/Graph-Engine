from Graph import Node, get_graph, generate_graph
from Draw import draw

"""obj0 = Node(value=0) # config 2
obj1 = Node(value=1)
obj2 = Node(value=2)
obj3 = Node(value=3)
obj4 = Node(value=4)
obj5 = Node(value=5)
obj6 = Node(value=6)
obj7 = Node(value=7)
obj1.register_parent(obj0)
obj0.register_child(obj3)
obj0.register_child(obj5)
obj0.register_parent(obj7)
obj7.register_parent(obj6)
obj7.register_child(obj6)
obj6.register_parent(obj5)
obj5.register_parent(obj4)
obj2.register_child(obj3)
obj1.register_child(obj1)
obj5.register_child(obj5)

mygraph = get_graph(obj0)"""

#draw(generate_graph(10, 6))

node0 = Node(value=0)
node1 = Node(value=1)
node2 = Node(value=2)

node3 = Node(value=3, parents=[node0])
node1.register_parent(node0)
node1.register_child(node2)

node1.print_parents()
node1.print_childs()

my_graph = get_graph(node0)

draw(my_graph)