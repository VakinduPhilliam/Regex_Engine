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
# Groups are marked by the '(', ')' metacharacters. '(' and ')' have much the same meaning as they do in mathematical expressions; they group together the
# expressions contained inside them, and you can repeat the contents of a group with a repeating qualifier, such as *, +, ?, or {m,n}.
#
# For example, (ab)* will match zero or more repetitions of ab.
# 

p = re.compile('(ab)*')
print(p.match('ababababab').span())

# OUTPUT: '(0, 10)'
 
#
# Groups indicated with '(', ')' also capture the starting and ending index of the text that they match; this can be retrieved by passing an argument to
# group(), start(), end(), and span(). Groups are numbered starting with 0. Group 0 is always present; it’s the whole RE, so match object methods all have
# group 0 as their default argument. Later we’ll see how to express groups that don’t capture the span of text that they match.
# 

p = re.compile('(a)b')

m = p.match('ab')
m.group()

# OUTPUT: 'ab'

m.group(0)

# OUTPUT: 'ab'

# 
# Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to determine the number, just count the opening parenthesis characters,
# going from left to right.
# 

p = re.compile('(a(b)c)d')

m = p.match('abcd')
m.group(0)

# OUTPUT: 'abcd'

m.group(1)

# OUTPUT: 'abc'

m.group(2)

# OUTPUT: 'b'
 
#
# group() can be passed multiple group numbers at a time, in which case it will return a tuple containing the corresponding values for those groups.
# 

m.group(2,1,2)

# OUTPUT: '('b', 'abc', 'b')'

# 
# The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are.
# 

m.groups()

# OUTPUT: '('abc', 'b')'
 
#
# Backreferences in a pattern allow you to specify that the contents of an earlier capturing group must also be found at the current location in the
# string.
# For example, \1 will succeed if the exact contents of group 1 can be found at the current position, and fails otherwise.
# Remember that Python’s string literals also use a backslash followed by numbers to allow including arbitrary characters in a string, so be sure to use
# a raw string when incorporating backreferences in a RE.
# 
# For example, the following RE detects doubled words in a string.
# 

p = re.compile(r'\b(\w+)\s+\1\b')
p.search('Paris in the the spring').group()

# OUTPUT: 'the the'
