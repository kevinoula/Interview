class queue:
    def __init__(self):
        self.data = []

    # Add data to list
    def enqueue(self,data):
        self.data.append(data)

    # Display stored data
    def display(self):
        result = ""
        for i in range(0,len(self.data)):
            result += str(self.data[i])
            if i != len(self.data)-1:
                result += ", "
        return print(result)

    def dequeue(self):
        print("%s has been dequeued." % str(self.data[0]))
        self.data = self.data[1:]


class priority_queue(queue):
    # Remove the max element from the queue
    def dequeue(self):
        top = max(self.data)
        idx = self.data.index(top)
        self.data.pop(idx)
        print("%s has been dequeued. " % str(top))

