class Claculator:
    def sub(self,a,b,c=0):
        return a-b-c
    
    def sum(self, *args):
        return sum(args)
    
calcu=Claculator()
sub1=calcu.sub(12,25)
sub2=calcu.sub(23,45,45)
sum1=calcu.sum(12,25)
sum2=calcu.sum(23,45,45)
print(sub1)
print(sub2)
print(sum1)
print(sum2)