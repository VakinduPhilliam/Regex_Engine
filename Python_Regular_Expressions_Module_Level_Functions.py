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
# Module-Level Functions:
# 
# You don’t have to create a pattern object and call its methods; the re module also provides top-level functions called match(), search(), findall(),
# sub(), and so forth. These functions take the same arguments as the corresponding pattern method with the RE string added as the first argument, and
# still return either None or a match object instance.
# 

print(re.match(r'From\s+', 'Fromage amk'))

# OUTPUT: 'None'

re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')  

# OUTPUT: '<re.Match object; span=(0, 5), match='From '>'
