
class simpleOperations(object):
    
    def __init__(self, x,y):
        self.x = x
        self.y = y 
    
    def productXY(self):
        prod = [self.x[i]*self.y[i] for i in range(len(self.x))]
        return prod 
    
    def addOneX(self):
        print self.x
        self.x = [self.x[i]+1 for i in range(len(self.x))]
        print self.x
        return None
    
    def differenceXY(self,x=None,y=None):
        if (x==None and y!= None) or (x!=None and y==None):
            raise NameError('ErrorNeeded')
        if x!=None and y!=None:
            if len(x)!=len(y):
                raise NameError('WrongLength') 
        if x==None:
            x=self.x
        if y==None:
            y=self.y
        diff = [x[i]-y[i] for i in range(len(x))]
        return diff
#     
#     def difference(self):
#         diff = [self.x[i]-self.y[i] for i in range(len(self.x))]
#         
#     def difference(self):    
#         diff = [x[i]-y[i] for i in range(len(x))]
#         
    def printDefaults(self,x=1,y=1,z=1):
        print 'x=',x
        print 'y=',y
        print 'z=',z
    
    def newFun(self):
        #increase the values by 1
#        #calculate the product
#         addOne = [(x[i]+1)*y[i] for i in range(len(x))]
# #         prodXY = [x[i]*y[i] for i in range(len(x))]
#         return addOne
# #             return prodXY
        print 'x-',self.x, 'y-',self.y
        self.addOneX()
        prod = self.productXY()    
        print 'x=', self.x, 'prod =', prod
        
# x = [2,5,3]
# y = [4,5,7]
   
# ranObj = simpleOperations(x,y)
# prod = ranObj.productXY()
# # 
# print x, y, prod
# ranObj.addOneX()

# x = [4,5,7]
# y = [2,5,3]
#  
# ranObj = simpleOperations(x,y)
# diff = ranObj.differenceXY()
# print x, y, diff





