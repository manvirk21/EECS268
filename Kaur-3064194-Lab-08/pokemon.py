class Pokemon:
    def __init__(self, US_name, id_num, jpn_name):  # initiating Pokemon class
        self.US_name = US_name
        self.jpn_name = jpn_name
        self.id_num = id_num

# comparing two Pokemon objects
    def __eq__(self, other):
        return self.id_num == other.id_num

    def __lt__(self, other):
        return self.id_num < other.id_num

    def __gt__(self, other):
        return self.id_num > other.id_num

# comparing two id_num elements
    def __eq__(self, num):
        return self.id_num == num

    def __lt__(self, num):
        return self.id_num < num

    def __gt__(self, num):
        return self.id_num > num
