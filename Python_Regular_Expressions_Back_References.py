# Python Regular Expressions.
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
# The syntax for backreferences in an expression such as (...)\1 refers to the number of the group.
# There’s naturally a variant that uses the group name instead of the number. This is another Python extension: (?P=name) indicates that the contents of
# the group called name should again be matched at the current point. The regular expression for finding doubled words, \b(\w+)\s+\1\b can also be written
# as \b(?P<word>\w+)\s+(?P=word)\b:
# 

p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
p.search('Paris in the the spring').group()

# OUTPUT: 'the the'
