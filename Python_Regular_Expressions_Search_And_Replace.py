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
# Search and Replace:
# 
# Another common task is to find all the matches for a pattern, and replace them with a different string. The sub() method takes a replacement value, which
# can be either a string or a function, and the string to be processed.
# .sub(replacement, string[, count=0]). 
# Returns the string obtained by replacing the leftmost non-overlapping occurrences of the RE in string by the replacement replacement.
# If the pattern isn’t found, string is returned unchanged.
# 
# The optional argument count is the maximum number of pattern occurrences to be replaced; count must be a non-negative integer.
# The default value of 0 means to replace all occurrences.
# 
# A simple example of using the sub() method. It replaces colour names with the word colour:
# 

p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')

# OUTPUT: 'colour socks and colour shoes'

p.sub('colour', 'blue socks and red shoes', count=1)

# OUTPUT: 'colour socks and red shoes'

# 
# The subn() method does the same work, but returns a 2-tuple containing the new string value and the number of replacements that were performed:
# 

p = re.compile('(blue|white|red)')
p.subn('colour', 'blue socks and red shoes')

# OUTPUT: '('colour socks and colour shoes', 2)'

p.subn('colour', 'no colours at all')

# OUTPUT: '('no colours at all', 0)'
 
#
# Empty matches are replaced only when they’re not adjacent to a previous empty match.
# 

p = re.compile('x*')
p.sub('-', 'abxd')

# OUTPUT: '-a-b--d-'

# 
# If replacement is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r is converted to
# a carriage return, and so forth. Unknown escapes such as \& are left alone. Backreferences, such as \6, are replaced with the substring matched by
# the corresponding group in the RE. This lets you incorporate portions of the original text in the resulting replacement string.
# 
# This example matches the word section followed by a string enclosed in {, }, and changes section to subsection:
# 

p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First} section{second}')

# OUTPUT: 'subsection{First} subsection{second}'

# 
# There’s also a syntax for referring to named groups as defined by the (?P<name>...) syntax. \g<name> will use the substring matched by the group named
# name, and \g<number> uses the corresponding group number. \g<2> is therefore equivalent to \2, but isn’t ambiguous in a replacement string such as
# \g<2>0. (\20 would be interpreted as a reference to group 20, not a reference to group 2 followed by the literal character '0'.) 
# The following substitutions are all equivalent, but use all three variations of the replacement string.
# 

p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First}')

# OUTPUT: 'subsection{First}'

p.sub(r'subsection{\g<1>}','section{First}')

# OUTPUT: 'subsection{First}'

p.sub(r'subsection{\g<name>}','section{First}')

# OUTPUT: 'subsection{First}'

# 
# replacement can also be a function, which gives you even more control.
# If replacement is a function, the function is called for every non-overlapping occurrence of pattern. On each call, the function is passed a match object
# argument for the match and can use this information to compute the desired replacement string and return it.
# 
# In the following example, the replacement function translates decimals into hexadecimal:
# 

def hexrepl(match):
        "Return the hex string for a decimal number"
        value = int(match.group())

        return hex(value)

    p = re.compile(r'\d+')

    p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')

# OUTPUT: 'Call 0xffd2 for printing, 0xc000 for user code.'
 
#
# When using the module-level re.sub() function, the pattern is passed as the first argument. The pattern may be provided as an object or as a string; if
# you need to specify regular expression flags, you must either use a pattern object as the first parameter, or use embedded modifiers in the pattern
# string, e.g. sub("(?i)b+", "x", "bbbb BBBB") returns 'x x'.
