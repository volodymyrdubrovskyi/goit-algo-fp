import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def create_graph(arr: list):
    if len(arr) == 0:
        return None
    graph = Node(arr[0])
    if len(arr) <= 3:  # Базовий випадок
        if len(arr) >= 2:
            graph.left = Node(arr[1])
        if len(arr) == 3:
            graph.right = Node(arr[2])

    else:  # массив від 4х елементів, розкладаємо на дві купи
        arr_left = [arr[1]]
        arr_right = [arr[2]]
        i = 3
        while i < len(arr):
            arr_left.append(arr[i])
            if i+1 < len(arr):
                arr_left.append(arr[i+1])
            i = 2*i +1
        i = 5
        while i < len(arr):
            arr_right.append(arr[i])
            if i+1 < len(arr):
                arr_right.append(arr[i+1])
            i = 2*i +1
        graph.left = create_graph(arr_left)
        graph.right = create_graph(arr_right)
    return graph

# Бінарну купу задаємо как масив
arr = [0, 4, 1, 5, 10, 3, 2, 15, 12]

# Створення дерева
root = create_graph(arr)

# Відображення дерева
draw_tree(root)