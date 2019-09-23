import re



# FOR displaying the groups it can only be used if there is a known output. DOES NOT WORK WITH A "NONE TYPE"!!!!
# if you are going to have a possible None Type, you need to put logic in to catch it

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#
# data = input()
#
# mo = phoneNumRegex.search(data)
#
# print('phone number found: ' + mo.group())
#
phoneNumGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo2 = phoneNumGroup.search('my phone number is 415-555-5555')

print(mo2.group(1))

print(mo2.group(2))

print(mo2.group(0))

print(mo2.group())




# Pipe ( '|') will search for either criteria but will only return the first one if they are both in the search area. It needs to be CASE SENSITIVE


heroRegex = re.compile(r'Batman | Tina Fey')

mo3 = heroRegex.search('Batman & tina fey')

print(mo3.group())

# the below example is how to search for multiple types of words such as Batmobile, Batman, Batcar, etc.... CASE SENSITIVE

batRegex = re.compile(r'Bat(man|mobile|car|woman)')

mo4 = batRegex.search('the Batcar is on its way')

print(mo4.group())


# OPTIONAL MATCHING

optionalRegex = re.compile(r'Bat(wo)?man')

mo5 = optionalRegex.search('im Batwoman')

print(mo5.group())


# the aterik = the group that precedes the asterik can occur any number of times

# If you use a '+' then it will search for ONE or more. There must be at least one present or it will throw an error

starRegex = re.compile(r'Bat(wo)*man')
mo6 = starRegex.search('Im Batwowowowowowoman and I am Batman Batman')
print(mo6.group())


# The (#){#,#} STRUCTURE searches for a match of whatever is inside the parenthese and how many times in the curly brackets. -> if there are two numbers in the curly brackets then is will search for a minimum of the first number and a maximum of the second number. EXAMPLE -> (Ha){3,5} will look for a re-occurence of 'Ha' at a minimum of 3 times to a maximum fo five times.

# NOTE! If given a min and a max it will always search for the longest max -> "GREEDY MATCHING"

# "NON-GREEDY MATCHING" is the format of (#){#,#}?  ---> Adding the question mark makes it search for the first shortest possibility.

haRegex = re.compile(r'(Ha){3}')
mo7 = haRegex.search('HaHaHa')
print(mo7.group())

mo8 = haRegex.search("Ha")

if mo8 == None:
    print(True)
else:
    print(False)

# THE findall() Method
# This will return all matches of the regex instead of groups

findRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo9 = findRegex.findall('Cell: 209-900-9988 and Work: 230-432-4434')
print(mo9)

# if there are parenthesises around the area code or there are groups (\d\d\d)-(\d\d\d)-(\d\d\d\d) --> then it will return a list of tuples
# EXAMPLE --> [('415','555', '4534'), ('234','345','6758')]



xmasRegex = re.compile(r'\d+\s\w+') #This will match ONLY a number(s) followed by a space and then by a match of letters, numeric character or a underline. in other words, a WORD
print(xmasRegex.findall('12 drummers, 11 pipers, 10 milk maids, 9 lords, etc...')) #Will not print the commas, the second word of "maids" or 'etc...'

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats babyfood'))

consanentRegex = re.compile(r'[^aeiouAEIOU]')
print(consanentRegex.findall('Robocop eats baby food.'))



beginsWithHello = re.compile(r'^Hello') # The '^' makes sure it STARTS with "Hello" --> Case sensitive

print(beginsWithHello.search('Hello Hello'))  # RETURNS -> <re.Match object; span=(0, 5), match='Hello'>



endsWithNumber = re.compile(r'\d$') # this will look for and return the last digit ONLY IF the search field ends in a digit and it will only return ONE value.
#To search for a larger number, add the plus sign
print(endsWithNumber.search('the number is 48589392'))      #<re.Match object; span=(21, 22), match='2'>

searchWholeNum = re.compile(r'\d+$')
print(searchWholeNum.search('number is 1239812983123'))     #<re.Match object; span=(10, 23), match='1239812983123'>


#           THE DOT will match everything ex dpt a new line. in the below example it matches everything that ends with 'at'
atRegex = re.compile(r'.at')
print(atRegex.findall('cat, mat, sat, flat, bat, rat, 9at, .at')) #['cat', 'mat', 'sat', 'lat', 'bat', 'rat', '9at', '.at']  //notice it only returned LAT not FLAT

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #This will match anything entered after first and last name field
name = nameRegex.search('First Name: Tim Last Name: Allen')
print(name.group(1))        #Tim
print(name.group(2))        #Allen

#           THE DOT and DOT ASTERIK are greedy matching options, to use non-greedy options,use the '?' to match the first one.

###EXAMPLE###
nongreedyRegex = re.compile(r'<.*?>')
nongreedy = nongreedyRegex.search('<to serve man> for dinner.>')
print(nongreedy.group())

greedyRegex = re.compile(r'<.*>')
greedy = greedyRegex.search('<to serve man> for dinner.>')
print(greedy.group())


### HOW TO SEARCH MULTIPLE LINES: ###
newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('Serve the public. \nProsad \nanother line').group())

### HOW TO IGNORE upper or lower CASE ###
ignoreRegex = re.compile(r'robocop', re.I)      # --> re.I  or re.IGNORECASE ignores case sensitive
print(ignoreRegex.search('rObOcOp was here').group())

namesRegex = re.compile(r'Agent \w+')

x = namesRegex.sub('CENSORED', 'Agent Alice is complicit in the murder of Agent Bond.')
print(x)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
z = agentNamesRegex.sub(r'\1******', 'Agent Alice told Agent Bob that Agent Eve was with Agent Bond.')
print(z)

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*d{2,5})?
)''',re.VERBOSE)

j = phoneRegex.search('408-344-3532, ext 4935')
print(j.group())
