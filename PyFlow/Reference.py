
class Ref(object):
    """
    Data wrapper
    """
    def __init__(self, val, data_type):
        super(Ref, self).__init__()
        self.data = val
        self.data_type = data_type

    @staticmethod
    def set(obj, val):
        obj.data = val

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        return other.data + self.data

    def __mul__(self, other):
        return other.data * self.data

    def __sub__(self, other):
        return self.data - other.data

    def __mod__(self, other):
        return self.data % other.data

    def __truediv__(self, other):
        return self.data / other.data

    def __getitem__(self, index):
        return self.data[index]

    def __contains__(self, value):
        return value in self.data

    def __len__(self):
        return len(self.data)

    def __lt__(self, other):
        return self.data < other

    def __le__(self, other):
        return self.data <= other

    def __eq__(self, other):
        return self.data == other

    def __ne__(self, other):
        return self.data != other

    def __gt__(self, other):
        return self.data > other

    def __ge__(self, other):
        return self.data >= other