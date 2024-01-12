l = [1,2,3,4,5]
# li = iter(l)  #l.__iter__()

#for loop
# while True:
#     try:
#         item = next(li)
#         print(item)
#     except StopIteration:
#         break


#range
# class MyRange:

#     def __init__(self, start, end):
#         self.value = start
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value +=1
#         return current
    

# nums = MyRange(1,10)

# for num in nums:
#     print(num)


# print(next(nums))

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

# nums = my_range(1,10)
# print(next(nums))


# https://www.youtube.com/watch?v=jTYiNjvnHZY