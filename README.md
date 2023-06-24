# Graph Engine
Implementation of management and visualisation of directed multigraphs permitting loops

![random](/media/random.png)

<br>

## Usage

Use the <code>Node()</code> class to create multiple Nodes indentifiable via value.

```py
node0 = Node(value=0)
node1 = Node(value=1)
node2 = Node(value=2)
```

<br>

You can assign parent and child nodes directly on creation of a node or later with the <code>Node().register_parent()</code> or <code>Node().register_child()</code> functions.

```py
node3 = Node(value=3, parents=[node0])
node1.register_parent(node0)
node1.register_child(node2)
```

<br>

To print the parents of children of a node, use the <code>Node().print_parents()</code> or <code>Node().print_childs()</code> functions.

```py
node1.print_parents()
node1.print_childs()
```

<br>

Get the whole graph a node is connected to with the <code>get_graph(node)</code> function.

```py
my_graph = get_graph(node0)
```

<br>

Draw the graph by using the <code>draw()</code> function.
```py
draw(my_graph)
```

![example](/media/example.png)

<br>
<br>

Or just generate a random graph with the <code>generate_graph()</code> function where \
```n``` is the number of nodes \
```tweak``` is a value to tweak the number of parents and childs each node should have
```py
my_graph2 = generate_graph(n=10, tweak=6)
```
