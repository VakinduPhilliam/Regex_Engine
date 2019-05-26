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
# \b 
# Word boundary. This is a zero-width assertion that matches only at the beginning or end of a word.
# A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.
# 
# The following example matches class only when it’s a complete word; it won’t match when it’s contained inside another word.
# 

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

# OUTPUT: '<re.Match object; span=(3, 8), match='class'>'

print(p.search('the declassified algorithm'))

# OUTPUT: 'None'

print(p.search('one subclass is'))

# OUTPUT: 'None'

#
# There are two subtleties you should remember when using this special sequence. First, this is the worst collision between Python’s string literals and
# regular expression sequences. In Python’s string literals, \b is the backspace character, ASCII value 8. If you’re not using raw strings, then Python
# will convert the \b to a backspace, and your RE won’t match as you expect it to. The following example looks the same as our previous RE, but omits the
# 'r' in front of the RE string.
# 

p = re.compile('\bclass\b')
print(p.search('no class at all'))

# OUTPUT: 'None'

print(p.search('\b' + 'class' + '\b'))

# OUTPUT: '<re.Match object; span=(0, 7), match='\x08class\x08'>'
