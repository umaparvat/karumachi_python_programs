

class DeQueue:
    def __init__(self):
        self.que = []

    def add_rear(self, data):
        """
        O(n) -> push all element to left
        :param data:
        :return:
        """
        self.que.insert(0, data)

    def add_front(self, data):
        """
        amortized cost O(1)
        :param data:
        :return:
        """
        self.que.append(data)

    def remove_front(self):
        """

        O(1)
        :return:
        """
        assert not self.que, "cannot remove item in empty queue"
        return self.que.pop()

    def remove_rear(self):
        """
        After pop, shift elements to front.
        O(n)
        :return:
        """
        assert not self.que, "cannot remove item in empty queue"
        return self.que.pop(0)

    def __len__(self):
        return len(self.que)

    def is_empty(self):
        return len(self.que) == 0
