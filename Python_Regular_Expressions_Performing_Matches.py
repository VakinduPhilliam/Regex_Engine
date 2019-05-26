# Python Regular Expressions
# Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python
# and made available through the re module. Using this little language, you specify the rules for the set of possible strings that you want to match; this
# set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like.
# You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere in this string?”.
# You can also use REs to modify a string or to split it apart in various ways.
# 
# Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C.
# For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a certain way in order to 
# produce bytecode that runs faster. Optimization isn’t covered in this document, because it requires that you have a good understanding of the matching
# engine’s internals.
# 
# The regular expression language is relatively small and restricted, so not all possible string processing tasks can be done using regular expressions.
# There are also tasks that can be done with regular expressions, but the expressions turn out to be very complicated. In these cases, you may be better
# off writing Python code to do the processing; while Python code will be slower than an elaborate regular expression, it will also probably be more
# understandable.
#
# Performing Matches:

import re

p = re.compile('[a-z]+')
p

# OUTPUT: 're.compile('[a-z]+')'

#
# Now, you can try matching various strings against the RE [a-z]+. An empty string shouldn’t match at all, since + means ‘one or more repetitions’.
# match() should return None in this case, which will cause the interpreter to print no output. You can explicitly print the result of match() to make
# this clear.
# 

p.match("")
print(p.match(""))

# OUTPUT: 'None'
 
#
# Now, let’s try it on a string that it should match, such as tempo. In this case, match() will return a match object, so you should store the result in
# a variable for later use.
# 

m = p.match('tempo')
m

# OUTPUT: '<re.Match object; span=(0, 5), match='tempo'>'
