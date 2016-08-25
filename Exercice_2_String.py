
# coding: utf-8

# In[1]:

"""
A. donuts
Given an int count of a number of donuts, return a string of the form 'Number of donuts: ', where  is 
the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
"""

#FUNCTION
def donuts(count):
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'

#TESTS
print donuts(5)
print donuts(23)


# In[3]:

"""
B. both_ends
Given a string s, return a string made of the first 2 and the last 2 chars of the original string, 
so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.
"""

#FUNCTION
def both_ends(s):
    if len(s) < 2 : 
        return ''
    else :
        first2 = s[0:2]
        last2 = s[-2:]
        return first2 + last2

#TESTS
print both_ends("spring")
print both_ends("p")


# In[8]:

"""
C. fix_start
Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
e.g. 'babble' yields 'ba**le'
Assume that the string is length 1 or more. Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.
"""

#FUNCTION
def fix_start(s):
    first = s[0]
    others = s[1:]
    fixed_others = others.replace(first, '*')
    return first + fixed_others

#TESTS
print fix_start("babble")
print fix_start("daddy")


# In[9]:

"""
D. MixUp
Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
e.g.'mix', pod' -> 'pox mid'
'dog', 'dinner' -> 'dig donner'
Assume a and b are length 2 or more.
"""

#FUNCTION
def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped

#TESTS
print mix_up("mix","pod")
print mix_up("dog","dinner")


# In[10]:

"""
D. verbing
Given a string, if its length is at least 3, add 'ing' to its end. 
Unless it already ends in 'ing', in which case add 'ly' instead. 
If the string length is less than 3, leave it unchanged. 
Return the resulting string.
"""

#FUNCTION
def verbing(s):
    if len(s) >= 3:
        if s[-3:] != 'ing': s = s + 'ing'
        else: s = s + 'ly'
    return s

#TESTS
print verbing("acting")
print verbing("in")
print verbing("act")


# In[20]:

"""
E. not_bad
Given a string, find the first appearance of the substring 'not' and 'bad'. 
If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
Return the resulting string.
So 'This dinner is not that bad!' yields: This dinner is good!
"""

#FUNCTION
def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if n != -1 and b != -1 and b > n:
        s = s[:n] + 'good' + s[b+3:]
    return s #, n, b

#TESTS
print not_bad('This dinner is not that bad!')


# In[16]:

"""
F. front_back
Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half.
e.g. 'abcde', the front half is 'abc', the back half 'de'.
Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back
"""

#FUNCTION
def front_back(a, b):
    a_middle = len(a) / 2
    b_middle = len(b) / 2
    if len(a) % 2 == 1:  # = odd number
         a_middle = a_middle + 1
    if len(b) % 2 == 1:
        b_middle = b_middle + 1 
    return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]

#TESTS
print front_back('Kitten', 'Donut')
print front_back('AT', 'RT')


# In[21]:

#OTHERS TESTS
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


def main():
    
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
    
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')
    
main()

