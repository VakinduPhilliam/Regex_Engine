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
# Text Munging:
# 
# sub() replaces every occurrence of a pattern with a string or the result of a function.
#
# This example demonstrates using sub() with a function to “munge” text, or randomize the order of all the characters in each word of a sentence except
# for the first and last characters:
# 

def repl(m):
     inner_word = list(m.group(2))

        random.shuffle(inner_word)

        return m.group(1) + "".join(inner_word) + m.group(3)

text = "Professor Abdolmalek, please report your absences promptly."

re.sub(r"(\w)(\w+)(\w)", repl, text)

# OUTPUT: 'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'

re.sub(r"(\w)(\w+)(\w)", repl, text)


# OUTPUT: 'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
