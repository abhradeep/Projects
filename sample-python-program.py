''' This is a Python code snippet '''

# This counts the number of words in a passed string

w = 'abhradeep in australia'

count = {}

for letter in w:
    if letter in count.keys():
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1

print "The letter count is the supplied word is %s"%(count)
