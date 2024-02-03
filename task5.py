from task4 import create_graph, draw_tree, Node
from collections import deque

def dfs_recursive(root: Node, color_index,  color_pallete):
    if root.color == 'skyblue':
        root.color = color_pallete[color_index]
        color_index += 1
    if root.left:
        color_index = dfs_recursive(root.left, color_index, color_pallete)
    if root.right:
        color_index = dfs_recursive(root.right, color_index, color_pallete)
    return color_index

def bfs_recursive(root: Node, queue, color_index,  color_pallete):
    if root.color == 'skyblue':
        root.color = color_pallete[color_index]
        color_index += 1
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return color_index
    node = queue.popleft()
    if node.color == 'skyblue':
        node.color = color_pallete[color_index]
        color_index += 1
    if node.left:
        queue.extend([node.left])
    if node.right:
        queue.extend([node.right])
    color_index = bfs_recursive(root, queue, color_index,  color_pallete)
    return color_index

def main():
    # Бінарну купу задаємо как масив
    arr = [0, 4, 1, 5, 10, 3, 2, 15, 12]

    # Створення дерева
    root = create_graph(arr)
    #color_pallete = ['#0026E8', '#0098E5', '#00E2E2', '#00DD93', '#00DB49', '#00D800', '#47D600', '#8DD300', '#D1D100', '#CE8900', '#CC4300']
    color_pallete = ['#0600CC', '#1714CC', '#2828CC', '#3D3DCC', '#5151CC', '#6666CC', '#7A7ACC', '#8E8ECC', '#A3A3CC', '#B7B7CC', '#CCCCCC']

    dfs_recursive(root, 0,  color_pallete)
    
    # Відображення дерева, розмальованого відповідно до DFS
    draw_tree(root)

    # Заново робимо стандартний граф с голубою заливкою
    root = create_graph(arr)

    bfs_recursive(root, deque([root]), 0,  color_pallete)

    # Відображення дерева, розмальованого відповідно до BFS
    draw_tree(root)

if __name__ == '__main__':
    main()