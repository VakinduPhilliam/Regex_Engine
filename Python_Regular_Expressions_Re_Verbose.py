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
# Using re.VERBOSE:
# 
# By now you’ve probably noticed that regular expressions are a very compact notation, but they’re not terribly readable.
# REs of moderate complexity can become lengthy collections of backslashes, parentheses, and metacharacters, making them difficult to read and understand.
# 
# For such REs, specifying the re.VERBOSE flag when compiling the regular expression can be helpful, because it allows you to format the regular expression
# more clearly.
# 
# The re.VERBOSE flag has several effects. Whitespace in the regular expression that isn’t inside a character class is ignored.
# This means that an expression such as dog | cat is equivalent to the less readable dog|cat, but [a b] will still match the characters 'a', 'b', or a space.
# In addition, you can also put comments inside a RE; comments extend from a # character to the next newline. When used with triple-quoted strings, this
# enables REs to be formatted more neatly:
# 

pat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)

# 
# This is far more readable than:
# 

pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")
