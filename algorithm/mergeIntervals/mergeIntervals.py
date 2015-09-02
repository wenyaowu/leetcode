# Merge Intervals
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals): #Use Insert Intervals
        if not intervals:
            return []
        result = []    
        for interval in intervals:
            result = self.insert(result, interval)
        return result 
    
    def insert(self, intervals, newInterval):
    	res = []
    	for interval in intervals:
    		if (interval.end<newInterval.start) or (interval.start>newInterval.end):
    			res.append(interval)
    		elif (interval.end>newInterval.end) and (newInterval.start>interval.start):
    			newInterval = interval
    		else:
    			if newInterval.start<=interval.start<=newInterval.end:
    				if interval.end>newInterval.end:
    					newInterval.end = interval.end
    			if newInterval.start<=interval.end<=newInterval.end:
    				if interval.start<newInterval.start:
    					newInterval.start = interval.start
        res.append(newInterval)
        res = sorted(res, key=lambda res: res.start)
        return res