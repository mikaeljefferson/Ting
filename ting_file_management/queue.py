from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data == []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            raise IndexError("Fila vazia!")

    def search(self, index):
        if index not in range(len(self.data)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
