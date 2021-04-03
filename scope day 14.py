class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=m
    def __init__(self,__elements):
        self.__elements=a

    # Add your code here
    def computeDifference(self):
        list1=[]
        self.__elements=sorted(a)
        for i in range(1,len(self.__elements)):
            har=abs(self.__elements[0]-self.__elements[i])
            list1.append(har)
        self.maximumDifference=max(list1)
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
