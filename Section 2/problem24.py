def merge(intervals):
        intervals.sort()
        stack = []
        # insert first interval into stack
        stack.append(intervals[0])
        for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)

        return stack

arr = [[1,3],[2,6],[8,10],[15,18]]

stack = merge(arr)

for i in stack:
     print(i)
