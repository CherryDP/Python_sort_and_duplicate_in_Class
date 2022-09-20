class dziaua:
    def __init__(self,tab):
        self.Tab = tab

    def mergeSort(self):
        if len(array) > 1:
            r = len(self.Tab)//2
            L = self.Tab[:r]
            M = self.Tab[r:]


            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    self.Tab[k] = L[i]
                    i += 1
                else:
                    self.Tab[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                self.Tab[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                self.Tab[k] = M[j]
                j += 1
                k += 1

    def printList(self):
        newlist = []
        duplist = []
        for i in self.Tab:
            if i not in newlist:
                newlist.append(i)
            else:
                duplist.append(i)
        print("List of duplicates", duplist)



array = ['A', 'Z', 'K', 'J', 'B', 'D', 'A', 'E', 'C']
d1 = dziaua(array)
d1.mergeSort()
d1.printList()
