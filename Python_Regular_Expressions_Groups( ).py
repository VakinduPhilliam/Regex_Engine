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
# Regex Groups:

m.group()

# OUTPUT: 'tempo'

m.start(), m.end()

# OUTPUT: '(0, 5)'

m.span()

# OUTPUT: '(0, 5)'

# 
# group() returns the substring that was matched by the RE. start() and end() return the starting and ending index of the match. span() returns both start
# and end indexes in a single tuple. Since the match() method only checks if the RE matches at the start of a string, start() will always be zero.
# However, the search() method of patterns scans through the string, so the match may not start at zero in that case.
# 

print(p.match('::: message'))

# OUTPUT: 'None'

m = p.search('::: message'); print(m)

# OUTPUT: '<re.Match object; span=(4, 11), match='message'>'

m.group()

# OUTPUT: 'message'

m.span()

# OUTPUT: '(4, 11)'
