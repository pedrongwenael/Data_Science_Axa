
# coding: utf-8

# In[78]:

"""
A. match_ends:
Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first 
and last chars of the string are the same.
Note: python does not have a ++ operator, but += works.
"""

# FUNCTION
def match_ends(words):
    nb = 0
    for wd in words:
        if len(wd) >= 2 and wd[0].lower() == wd[-1].lower():
            nb += 1
    return nb

# TESTS
name = ["Amelia", "Amelie", "amelia", "AA", "Aa", "A"];
print match_ends(name)



# In[79]:

"""
B. front_x
Given a list of strings, return a list with the strings in sorted order, except group all 
the strings that begin with 'x' first.
e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']   yields 
     ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
Hint: this can be done by making 2 lists and sorting each of them before combining them.
"""

# FUNCTION
def front_x(words):
    list_x = []
    list_others = []
    for wd in words:
            if wd.lower().startswith('x'):
                list_x.append(wd)
            else:
                list_others.append(wd)         
    return sorted(list_x) + sorted(list_others)

# TESTS
list = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
print front_x(list)


# In[81]:

"""
C. sort_last
Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)]    yields 
     [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
Hint: use a custom key= function to extract the last element form each tuple.
"""

# FUNCTION
def last(t): return t[-1]

def sort_last(tuples):
    return sorted(tuples, key=last)

# TESTS
tup = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print sort_last(tup)


# In[82]:

"""
D. remove_adjacent
Given a list of numbers, return a list where all adjacent 
== elements have been reduced to a single element, 
so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
"""

# FUNCTION
def remove_adjacent(nums):
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result

# OTHER SOLUTION
def unique_list(nums):
    return sorted(set(nums))

# TESTS
num1 = [1, 2, 2, 3]
num2 = [2, 2, 3, 3, 3]

print remove_adjacent(num1)
print remove_adjacent(num2)
print unique_list(num1)
print unique_list(num2)



# In[75]:

"""
E. linear_merge
Given two lists sorted in increasing order, create and return a merged list of all the 
elements in sorted order. You may modify the passed in lists. 
Ideally, the solution should work in "linear" time, making a single pass of both lists.
"""

# FUNCTION
def linear_merge(list1, list2):
    result = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1)
    result.extend(list2)
    return result

#OTHER SOLUTION
def linear_merge2(list1, list2):
    return sorted(list1 + list2)

#TESTS
List1 = ['aa', 'xx', 'zz']
List2 = ['bb', 'cc']

print linear_merge2(List1,List2)
print linear_merge(List1,List2)



# In[83]:

# OTHER TESTS
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main(): 
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    print
    
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    print
    
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    print
    
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    print
    
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()

