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
# The syntax for a named group is one of the Python-specific extensions: (?P<name>...). name is, obviously, the name of the group.
# Named groups behave exactly like capturing groups, and additionally associate a name with a group. The match object methods that deal with capturing
# groups all accept either integers that refer to the group by number or strings that contain the desired group’s name.
# Named groups are still given numbers, so you can retrieve information about a group in two ways:
# 

p = re.compile(r'(?P<word>\b\w+\b)')

m = p.search( '(((( Lots of punctuation )))' )
m.group('word')

# OUTPUT: 'Lots'

m.group(1)

# OUTPUT: 'Lots'
 
#
# Named groups are handy because they let you use easily-remembered names, instead of having to remember numbers.
#
# Here’s an example RE from the imaplib module:
# 

InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')
