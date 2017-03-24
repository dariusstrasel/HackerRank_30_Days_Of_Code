class Difference:
    def __init__(self, a):
        self.__elements = a

# Add your code here
    def computeDifference(self):
        elements_list = [element for element in self.__elements]
        # print("elements: ", elements_list)
        difference = [[abs(abs(element) - abs(elements_list[index])) for element in elements_list] for index in range(len(elements_list))]
        largest = max([max([integer for integer in item]) for item in difference])
        # print("largest: ", largest)
        self.maximumDifference = largest
        # print("difference: ", difference)
        # End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)