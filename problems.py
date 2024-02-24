
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.length = self.__len__()

    def __len__(self):
         length = 0
         while(self.next):
              length = length + 1
         


        
      
class Solution(object):
	def addTwoNumbers(self, l1, l2):
              finalList = []
              carry = 0


              if (l1.length > l2.length):
                l2 += [0]*(l1.len - l2.len)
                finalListLength = l1.length 


              elif (l2.length > l1.length):
                 l1 += [0]*(l2.len - l1.len)
                 finalListLength = l2.length

              else: 
                 finalListLength = l1.length

                  
                  
              for i in range(finalListLength):
                  sum = l1[i] + l2[i] + carry

                  if (sum > 10): 
                      carry = 1 
                      current_sum -= 10
                    
                  else: carry = 0
               
                  finalList.append(current_sum)

              if(carry):
                      finalList.append(carry)
         
              return finalList
                

l1 = ListNode()
l2 = ListNode()

l1  = [int(x) for x in input("Enter the first array: ").split()]
l2 = [int(x) for x in input("Enter the second array: ").split()]

solution = Solution()

finalList = solution.addTwoNumbers(l1,l2)

finalSum = ListNode(finalList)

print(finalSum)
