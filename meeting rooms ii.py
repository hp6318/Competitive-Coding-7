'''
Sort the meetings based on their start time. Maintain a min-heap,
comparator on end-time of the interval. Iterate over the meetings
and check if the top of the heap's meeting ends before the start
of the current meeting in the interator. If yes, just assign this meeting
to the same room and update/extend the end time. 
Time : O(NlogN)
Space: O(N)
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[0]) # sorting based on start time
        heap = [] # min-heap based on end time

        heapq.heappush(heap,intervals[0][1]) # inserting first meeting
        
        for i in range(1,len(intervals)):
            if heap[0]<=intervals[i][0]: # start_time of next >= end of prev
                heapq.heappop(heap) # remove top
            
            heapq.heappush(heap,intervals[i][1]) # add/update new room
        
        return len(heap) # number of rooms