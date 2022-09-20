class Wozi:
    def __init__(self,tab):
        self.Tab = tab

    def sort_word(self):
        new_list = []

        while self.Tab:
            min = self.Tab[0]
            for x in self.Tab:
                if x < min:
                    min = x
            new_list.append(min)
            self.Tab.remove(min)
        self.list = new_list
        return self.list

    def __duplicat__(self):
        newlist = []
        duplist = []
        for i in self.list:
            if i not in newlist:
                newlist.append(i)
            else:
                duplist.append(i)
        print("List of duplicates", duplist)

d1 = Wozi(['A', 'Z', 'K', 'J', 'J', 'B', 'D', 'A', 'E', 'C'])
d1.sort_word()
d1.__duplicat__()
