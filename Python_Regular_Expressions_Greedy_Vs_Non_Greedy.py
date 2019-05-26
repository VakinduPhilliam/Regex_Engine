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
# Greedy versus Non-Greedy:
# 
# When repeating a regular expression, as in a*, the resulting action is to consume as much of the pattern as possible.
# This fact often bites you when you’re trying to match a pair of balanced delimiters, such as the angle brackets surrounding an HTML tag.
# The naive pattern for matching a single HTML tag doesn’t work because of the greedy nature of .*.
 
s = '<html><head><title>Title</title>'
len(s)

# OUTPUT: '32'

print(re.match('<.*>', s).span())

# OUTPUT: '(0, 32)'

print(re.match('<.*>', s).group())

# OUTPUT: '<html><head><title>Title</title>'
 
#
# The RE matches the '<' in '<html>', and the .* consumes the rest of the string. There’s still more left in the RE, though, and the > can’t match at the
# end of the string, so the regular expression engine has to backtrack character by character until it finds a match for the >.
# The final match extends from the '<' in '<html>' to the '>' in '</title>', which isn’t what you want.
# 
# In this case, the solution is to use the non-greedy qualifiers *?, +?, ??, or {m,n}?, which match as little text as possible.
# In the above example, the '>' is tried immediately after the first '<' matches, and when it fails, the engine advances a character at a time, retrying
# the '>' at every step. This produces just the right result:
# 

print(re.match('<.*?>', s).group())

# OUTPUT: <html>
