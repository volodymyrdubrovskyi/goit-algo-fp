import classes

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
        s = classes.Stack()
        while current_node.next:
            s.push(current_node.data)
            current_node = current_node.next
        s.push(current_node.data)
        r_llist = LinkedList()
        r_llist.insert_at_beginning(s.pop())
        while not s.is_empty():
            curr_data = s.pop()
            r_llist.insert_at_end(curr_data)
        return r_llist

def main():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(6)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(12)
    
    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()


    print("Оберненний зв'язний список:")
    llist = llist.reverse_list()
    llist.print_list()

if __name__ == '__main__':
    main()