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
# Checking for a Pair:
# 
# In this example, we’ll use the following helper function to display match objects a little more gracefully:
# 

def displaymatch(match):

    if match is None:
        return None

    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
 
#
# Suppose you are writing a poker program where a player’s hand is represented as a 5-character string with each character representing a card, “a” for
# ace, “k” for king, “q” for queen, “j” for jack, “t” for 10, and “2” through “9” representing the card with that value.
# 
# To see if a given string is a valid hand, one could do the following:
# 

valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))  # Valid.

# OUTPUT: "<Match: 'akt5q', groups=()>"

displaymatch(valid.match("akt5e"))  # Invalid.
displaymatch(valid.match("akt"))    # Invalid.
displaymatch(valid.match("727ak"))  # Valid.

# OUTPUT: "<Match: '727ak', groups=()>"

# 
# That last hand, "727ak", contained a pair, or two of the same valued cards. To match this with a regular expression, one could use backreferences
# as such:
# 

pair = re.compile(r".*(.).*\1")
displaymatch(pair.match("717ak"))     # Pair of 7s.

# OUTPUT: "<Match: '717', groups=('7',)>"

displaymatch(pair.match("718ak"))     # No pairs.
displaymatch(pair.match("354aa"))     # Pair of aces.

# OUTPUT: "<Match: '354aa', groups=('a',)>"

# 
# To find out what card the pair consists of, one could use the group() method of the match object in the following manner:
# 

pair.match("717ak").group(1)

# OUTPUT: '7'

# Error because re.match() returns None, which doesn't have a group() method:

pair.match("718ak").group(1)

# Traceback (most recent call last):
#  File "<pyshell#23>", line 1, in <module>

    re.match(r".*(.).*\1", "718ak").group(1)

# AttributeError: 'NoneType' object has no attribute 'group'

pair.match("354aa").group(1)

# OUTPUT: 'a'
