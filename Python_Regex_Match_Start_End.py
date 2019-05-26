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
# Match.start([group]) Match.end([group]). 
# Return the indices of the start and end of the substring matched by group; group defaults to zero (meaning the whole matched substring).
# Return -1 if group exists but did not contribute to the match. For a match object m, and a group g that did contribute to the match, the substring
# matched by group g (equivalent to m.group(g)) is;
 
m.string[m.start(g):m.end(g)]

# 
# Note that m.start(group) will equal m.end(group) if group matched a null string. For example, after m = re.search('b(c?)', 'cba'), m.start(0) is
# 1, m.end(0) is 2, m.start(1) and m.end(1) are both 2, and m.start(2) raises an IndexError exception.
#
 
#
# An example that will remove remove_this from email addresses:
# 

email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)

email[:m.start()] + email[m.end():]

# OUTPUT: 'tony@tiger.net'
