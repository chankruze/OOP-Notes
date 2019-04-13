import subprocess # to execute shell commands
subprocess.call('clear')

# import regular expression
import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, not the other !'

# search for pattern
for pattern in patterns:
    print("I'm searching for : " + pattern)

    if re.search(pattern, text):
        print("Match\n")
    else:
        print("No match\n")

# get matched term index
text2 = "Index term2"
match = re.search("term2", text2)

print("Got match at index " + str(match.start()) + "\n")

# split term
split_term = '@'
email = 'example@domain.com'
print(re.split(split_term, email))

print(re.findall("match","test phrase match in match in match middle"))

##### Multi Search #####

## Inclusion Search
# function defined for easiness
def multi_re_find(patterns, phrase):

    for pattern in patterns:
        print("\nsearching for pattern {}".format(pattern))
        print(re.findall(pattern,phrase))

test_phrase_01 = "ab.......ab...dog..cat...sex.money..github...gist..batman--abbb--kabbab....aap..aaaabbbb"

# * here is to find a followed by 0 or more b
test_pattern_01 = ['ab*']
# + here is to find a must followed by 1 or more b
test_pattern_02 = ['ab+']
# ? here is to find a followed by either 0 or 1 b
test_pattern_03 = ['ab?']
# {} here is to find a must followed by n b
test_pattern_04 = ['ab{3}']

# a followed by either 1/more a or 1/more b
test_pattern_05 = ['a[ab]+']

multi_re_find(test_pattern_01, test_phrase_01)
multi_re_find(test_pattern_02, test_phrase_01)
multi_re_find(test_pattern_03, test_phrase_01)
multi_re_find(test_pattern_04, test_phrase_01)
multi_re_find(test_pattern_05, test_phrase_01)

## Exclusion Search
test_phrase_02 = "This is a string!. But it has punctuation. How can we remove it ?"

# exclude one or more '!', '.', '?'
test_pattern_06 = ['[^!.?]+']
multi_re_find(test_pattern_06, test_phrase_02)

# sequences of lowercase letters
test_pattern_07 = ['[a-z]+']
multi_re_find(test_pattern_07, test_phrase_02)

# sequences of uppercase letters
test_pattern_08 = ['[A-Z]+']
multi_re_find(test_pattern_08, test_phrase_02)

# escape codes (prefixing character by '\')
test_phrase_03 = "This is a string with numbers 12312 and a symbol #linux"

# 'd' = digits
test_pattern_09 = [r'\d+']
multi_re_find(test_pattern_09, test_phrase_03)

# 'D' = non digits
test_pattern_10 = [r'\D+']
multi_re_find(test_pattern_10, test_phrase_03)

# 's' = whitespaces
test_pattern_11 = [r'\s+']
multi_re_find(test_pattern_11, test_phrase_03)

# 'S' = non whitespace
test_pattern_12 = [r'\S+']
multi_re_find(test_pattern_12, test_phrase_03)

# 'w' = alphanumeric
test_pattern_13 = [r'\w+']
multi_re_find(test_pattern_13, test_phrase_03)

# 'W' = non alphanumeric
test_pattern_14 = [r'\W+']
multi_re_find(test_pattern_14, test_phrase_03)
