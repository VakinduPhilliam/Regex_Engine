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
# Finding all Adverbs and their Positions:
# 
# If one wants more information about all matches of a pattern than the matched text, finditer() is useful as it provides match objects instead of strings.
# Continuing with the previous example, if a writer wanted to find all of the adverbs and their positions in some text, they would use finditer() in the
# following manner:
# 

text = "He was carefully disguised but captured quickly by police."

    for m in re.finditer(r"\w+ly", text):
         print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

#
# OUTPUT:
#
# 07-16: carefully
# 40-47: quickly

