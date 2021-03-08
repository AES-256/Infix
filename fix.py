import time
# Python program to convert infix expression to postfix 
# Created By Aref Niksohbbat At 7/March/2021
# Class to convert the expression 
class Conversion: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.tempArray = []
        self.top = -1 
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
        # Precedence setting 
        self.output = [] 
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
    # A utility function to check is the given character 
    # is operand  
    def isOperand(self, ch): 
        return ch.isalpha() 
  
    # Check if the precedence of operator is strictly 
    # less than top of stack or not 
    def notGreater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
              
    # The main function that  
    # converts given infix expression 
    # to postfix expression 
    def infixToPostfix(self, exp): 
          
        # Iterate over the expression for conversion 
        for i in exp: 
            # If the character is an operand,  
            # add it to output 
            if self.isOperand(i): 
                self.output.append(i) 
              
            # If the character is an '(', push it to stack 
            elif i  == '(': 
                self.push(i) 
  
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif i == ')': 
                while( (not self.isEmpty()) and 
                                self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
  
            # An operator is encountered 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 
  
        # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
            #print ("".join(self.output))
            #self.z = "".join(self.output)
        return "".join(self.output)

    def expInReverse(self,exp):
        x = exp[::-1]
        y = ''
        for i in range(len(x)):
            if(x[i] == '('):
                y = y + ')'
            elif(x[i] == ')'):
                y = y + '('
            else:
                y = y + x[i]
        return y
                

    # Get Infix for a given postfix  
    # expression  
    def getInfix(self ,exp) : 
    
        s = []  
    
        for i in exp:      
        
            # Push operands  
            if (self.isOperand(i)) :          
                s.insert(0, i)  
            
            # We assume that input is a  
            # valid postfix and expect  
            # an operator.  
            else: 
            
                op1 = s[0]  
                s.pop(0)  
                op2 = s[0]  
                s.pop(0)  
                s.insert(0, "(" + op2 + i +
                                op1 + ")")  
            
        # There must be a single element in  
        # stack now which is the required  
        # infix.  
        return s[0] 

    def prefixToInfix(self , prefix):
        stack = []
        
        # read prefix in reverse order
        i = len(prefix) - 1
        while i >= 0:
            if not self.isOperator(prefix[i]):
                
                # symbol is operand
                stack.append(prefix[i])
                i -= 1
            else:
                
                # symbol is operator
                str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
                stack.append(str)
                i -= 1
                
        return stack.pop()
    
    def isOperator(self , c):
        if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
            return True
        else:
            return False
        










def demo():
    #input expression to convert in fix to post fix
    exp = "((a+((b+c)*d))-e)"
    
    
    #makeing an object to use
    obj1 = Conversion(len(exp))
    obj2 = Conversion(len(exp))
    
    
    #in fix to postfix
    w = obj1.infixToPostfix(exp)
    
    
    #putting exp in reverse
    x = obj2.expInReverse(exp)
    
    
    #calculate postfix of the reversed exp
    z = obj2.infixToPostfix(x)
    
    
    #reverse the result from calculation
    y = obj2.expInReverse(z)
    
    
    
    #print result of prefix
    print("PreFix is : " + y)
    #print result of postfix
    print("PostFix is : " + w)


def inFixtoPostFix():
    a = input("enter expression : ")
    obj3 = Conversion(len(a))
    b = obj3.infixToPostfix(a)
    print("post fix is : " + b)


def inFixToPreFix():
    c = input("enter expression : ")
    obj4 = Conversion(len(c))
    d = obj4.expInReverse(c)
    e = obj4.infixToPostfix(d)
    f = obj4.expInReverse(e)
    print("post fix is : " + f)


def postfixtoinfix():
    g = input("enter expression : ")
    obj5 = Conversion(len(g))
    h = obj5.getInfix(g.strip())
    print("infix is : " + h)
    
    
def prefixToInfix():
    i = input("enter expression : ")
    obj6 = Conversion(len(i))
    j = obj6.prefixToInfix(i)
    print("infix is : " + j)
    
def menu():
        print("************MAIN MENU**************")
        time.sleep(1)
    
        choice = input("""
    Test Expression : ((a+((b+c)*d))-e)

        A: In Fix To Post Fix
        B: In Fix To Pre Fix
        C: Post Fix To In Fix
        D: Pre Fix To In Fix
        Q: Quit/Log Out

        Please enter your choice: """)
    
        if choice == "A" or choice =="a":
                inFixtoPostFix()
        elif choice == "B" or choice =="b":
                inFixToPreFix()
        elif choice == "C" or choice =="c":
                postfixtoinfix()
        elif choice=="D" or choice=="d":
                prefixToInfix()
        elif choice=="Q" or choice=="q":
                exit()
        else:
                print("You must only select either A,B,C, or D.")
                print("Please try again")
                menu()
                
                
# Driver program to test above function
    
menu()