'''
Solution 1: Using Min-Heap
    - Maintain a min-heap of size min(total rows, k)
    - add the first element of all lists indexed from 0 to k-1 in the heap along with
      row_idx, col_idx
    - Then, pop elements from the heap for 'k' times. Each time, when you pop, 
      add next column element of same row index in heap (if not out of bounds).
    - Final answer is the kth element popped from the heap.
Time Complexity: k*log(min(N,k)), N = number of rows, k = kth smallest number to be found
Space Complexity: log(min(N,k))
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [] # size of min(N rows, k) // store (element, row_idx, col_idx)
        rows = len(matrix) # number of rows
        cols = len(matrix[0])
        for i in range(len(matrix)):
            if len(heap)==k:
                break
            heapq.heappush(heap,(matrix[i][0],i,0)) # store (element, row_idx, col_idx)
        
        answer = 0
        while k>0 and len(heap)>0:
            answer,row_idx,col_idx = heapq.heappop(heap)
            k-=1
            if col_idx+1<cols:
                heapq.heappush(heap,(matrix[row_idx][col_idx+1],row_idx,col_idx+1))
        
        return answer