
class Heap:
   def __GetParent(self,i:int)->int:
       return((i+1)//2)-1
   def __GetLeftChild(self,i:int)->int:
       return 2*i+1
   def __GetRightChild(self,i:int)->int:
       return 2*i+2
   def __MaxHeapify(self,i:int)->int:
       left=self.__GetLeftChild(i)
       right=self.__GetRightChild(i)

       if(self._table[left]>self._table[i]):
           largest=left
       else:
           largest = i
       if (self._table[right] > self._table[largest]):
           largest = right
       if(largest!=i):
           self.__Swap(i,largest)
           self.__MaxHeapify(largest)
   def BuildMaxHeap(self,table):
       self._table=table
       for i in range((len(table)//2)-1,-1,-1):
           self.__MaxHeapify(i)


heap= Heap()
tab=[4,1,3,2,16,9,10,14,8,7]
heap.BuildMaxHeap(tab)