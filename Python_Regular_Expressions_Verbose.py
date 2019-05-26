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
# VERBOSE 
# This flag allows you to write regular expressions that are more readable by granting you more flexibility in how you can format them.
# When this flag has been specified, whitespace within the RE string is ignored, except when the whitespace is in a character class or preceded by an
# unescaped backslash; this lets you organize and indent the RE more clearly. This flag also lets you put comments within a RE that will be ignored by
# the engine; comments are marked by a '#' that’s neither in a character class or preceded by an unescaped backslash.
# 
# For example, here’s a RE that uses re.VERBOSE; see how much easier it is to read?
# 

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

#
# Without the verbose setting, the RE would look like this:
# 

charref = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")
