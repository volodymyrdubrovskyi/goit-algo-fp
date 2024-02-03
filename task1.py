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
    
    # Сортування на базі алгоритму сортування вставками
    def sort_list(self):
        if self.head.next == None:
            return self
        sorted_list = LinkedList() # Створюємо окремий список и вважаємо його відсортированим
        end_of_list = False
        current_node = self.head.next
        sorted_list.insert_at_beginning(self.head.data)
        # Беремо кожний вузел не відсортованого масиву й вставляємо його у відповідне місце сортованого списку
        while not end_of_list:
            # якщо вузел не відсортованого масиву менше першого вузла відсортованого списку, то додаємо його вперед
            if current_node.data <= sorted_list.head.data:  
                sorted_list.insert_at_beginning(current_node.data)
            # інакше шукаємо місце у відсортованому списку
            else:
                sorted_current_node = sorted_list.head
                prev_node = sorted_current_node
                while current_node.data > sorted_current_node.data:
                    prev_node = sorted_current_node
                    if sorted_current_node.next:
                        sorted_current_node = sorted_current_node.next
                    else:
                        break
                sorted_list.insert_after(prev_node, current_node.data)
            # і так доки не пройдемо весь не відсортоаний список
            if not current_node.next:
                end_of_list = True
            else:
                current_node = current_node.next
        return sorted_list
    

def combine_llists(llist1: LinkedList, llist2: LinkedList):
    # переходемо на востанній вузол першого списку
    curr_node = llist1.head
    while curr_node.next: 
        curr_node = curr_node.next
    # об'єднуємо списки:
    curr_node.next = llist2.head
    return llist1.sort_list()

    

def main():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(4)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(3)
    llist.insert_at_beginning(12)

    #llist.delete_node(7)
    
    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    print("Оберненний зв'язний список:")
    llist = llist.reverse_list()
    llist.print_list()

    print("Відсортований зв'язний список:")
    llist = llist.sort_list()
    llist.print_list()


    llist1 = LinkedList()
    llist1.insert_at_beginning(21)
    llist1.insert_at_beginning(19)
    llist1.insert_at_beginning(17)
    llist1.insert_at_beginning(16)
    llist1.insert_at_beginning(10)

    print("Зв'язний список 2:")
    llist1.print_list()

    llist1 = combine_llists(llist, llist1)
    print("Об'єднаний список:")
    llist1.print_list()

if __name__ == '__main__':
    main()