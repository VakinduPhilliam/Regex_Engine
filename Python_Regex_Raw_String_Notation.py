# Python Regex
# re — Regular expression operations.
# This module provides regular expression matching operations similar to those found in Perl.
# Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes).
# However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode string with a byte pattern or vice-versa; similarly,
# when asking for a substitution, the replacement string must be of the same type as both the pattern and the search string.
# Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their
# special meaning. This collides with Python’s usage of the same character for the same purpose in string literals; for example, to match a literal
# backslash, one might have to write '\\\\' as the pattern string, because the regular expression must be \\, and each backslash must be expressed
# as \\ inside a regular Python string literal.
#
# Raw String Notation:
# 
# Raw string notation (r"text") keeps regular expressions sane. Without it, every backslash ('\') in a regular expression would have to be prefixed with
# another one to escape it. For example, the two following lines of code are functionally identical:
# 

re.match(r"\W(.)\1\W", " ff ")

# OUTPUT: '<re.Match object; span=(0, 4), match=' ff '>'

re.match("\\W(.)\\1\\W", " ff ")

# OUTPUT: '<re.Match object; span=(0, 4), match=' ff '>'

# 
# When one wants to match a literal backslash, it must be escaped in the regular expression. With raw string notation, this means r"\\". Without raw string
# notation, one must use "\\\\", making the following lines of code functionally identical:
# 

re.match(r"\\", r"\\")

# OUTPUT: '<re.Match object; span=(0, 1), match='\\'>'

re.match("\\\\", r"\\")

# OUTPUT: '<re.Match object; span=(0, 1), match='\\'>'
