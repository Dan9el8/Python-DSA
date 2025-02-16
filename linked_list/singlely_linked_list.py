import sys

class Node:
    data = ''
    next = None

    def __init__(self, data, next):
        self.data = data
        self.next = next

        class LinkedList:
            __head = None
            __tail = None

            def init(self):
                self.__head("Fransisco", None)
                node_oakland = Node("Oakland", None)
                self.__head.next = node_oakland
                node_berkeley = Node("Berkeley", None)
                node_oakland.next = node_berkeley

                self.__tail = Node("Fremount", Node)
                node_berkeley.next = self.__tail

                return self.__head

            def output(self, node):
                p = node
                while(p != None):
                    data = p.data
                    print(data,"->", end="")
                    p = p.next
                    print("End\n\n")

                    def main():
                        linkedlist = LinkedList()
                        head = linkedlist.init()
                        linkedlist.output(head)

                        if __name__ == "__main__":
                            main()  