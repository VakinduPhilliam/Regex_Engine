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
# Splitting Strings:
# 
# The split() method of a pattern splits a string apart wherever the RE matches, returning a list of the pieces.
# It’s similar to the split() method of strings but provides much more generality in the delimiters that you can split by; string split() only supports
# splitting by whitespace or by a fixed string. As you’d expect, there’s a module-level re.split() function, too.
# .split(string[, maxsplit=0]) 
# Split string by the matches of the regular expression. If capturing parentheses are used in the RE, then their contents will also be returned as part
# of the resulting list. If maxsplit is nonzero, at most maxsplit splits are performed. 
# You can limit the number of splits made, by passing a value for maxsplit. When maxsplit is nonzero, at most maxsplit splits will be made, and the
# remainder of the string is returned as the final element of the list.
#
# In the following example, the delimiter is any sequence of non-alphanumeric characters:
# 

p = re.compile(r'\W+')
p.split('This is a test, short and sweet, of split().')

# OUTPUT: '['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', '']'

p.split('This is a test, short and sweet, of split().', 3)

# OUTPUT: '['This', 'is', 'a', 'test, short and sweet, of split().']'
 
#
# Sometimes you’re not only interested in what the text between delimiters is, but also need to know what the delimiter was.
# If capturing parentheses are used in the RE, then their values are also returned as part of the list.
#
# Compare the following calls:
# 

p = re.compile(r'\W+')
p2 = re.compile(r'(\W+)')

p.split('This... is a test.')

# OUTPUT: '['This', 'is', 'a', 'test', '']'

p2.split('This... is a test.')

# OUTPUT: '['This', '... ', 'is', ' ', 'a', ' ', 'test', '.', '']'
 
#
# The module-level function re.split() adds the RE to be used as the first argument, but is otherwise the same.
# 

re.split(r'[\W]+', 'Words, words, words.')

# OUTPUT: '['Words', 'words', 'words', '']'

re.split(r'([\W]+)', 'Words, words, words.')

# OUTPUT: '['Words', ', ', 'words', ', ', 'words', '.', '']'

re.split(r'[\W]+', 'Words, words, words.', 1)

# OUTPUT: '['Words', 'words, words.']'
