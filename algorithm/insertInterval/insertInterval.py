# Insert Interval
"""
Given a set of non-overlapping intervals,
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially
sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16],
insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
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