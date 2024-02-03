class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        current_node = self.head
        if current_node.next == None:
            return self
        temp = None
        while current_node.next:
            next_node = current_node.next
            current_node.next = temp
            temp = current_node
            current_node = next_node
        current_node.next = temp    
        self.head = current_node
        return self

def main():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(4)
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(1)
    
    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()


    print("Оберненний зв'язний список:")
    llist = llist.reverse_list()
    llist.print_list()

if __name__ == '__main__':
    main()