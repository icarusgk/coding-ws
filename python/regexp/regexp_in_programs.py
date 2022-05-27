import re


def find_emails(string):
    pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
    emails = re.findall(pattern, string)
    for email in emails:
        print(email)


# Suppose we have a text with various email addresses
string = '''cat billy123@something.com, dog 456 
          alice_2000@website.com johnnY.b@blahblahblah.com'''
find_emails(string)

# billy123@something.com
# alice_2000@website.com
# johnnY.b@blahblahblah.com


# Email validation 2.0
# Let's say we want the username to be at least 5 characters long
# and the domain name of 2 to 4 characters
pattern = re.compile(r'[\w\.-]{5,}@[\w-]+\.\w{2,4}')


def find_emails_2(string):
    # Here we compile our simple pattern that will match email addresses
    pattern = re.compile(r'[\w\.-]{5,}@[\w-]+\.[\w]{2,4}')

    # Remember that re.findall() returns a list of all matched email strings
    emails = re.findall(pattern, string)

    # To print the matched strings one by one
    for email in emails:
        print(email)


string = '''_@._ mary_liu@abc._ billy123@something.com, dog 456 
            alice_2000@website.com johnnY.b@blahblahblah.com one@one.one'''
print()
find_emails_2(string)


# billy123@something.com
# alice_2000@website.com
# johnnY.b@blahblahblah.com


# * Tokenization


def tokenize(string):
    tokens = re.split(r'\s+', string)
    return tokens


string = "This is a sample string. (And here's another one!!)"
print(tokenize(string))
# ['This', 'is', 'a', 'sample', 'string.', '(And', "here's", 'another', 'one!!)']


def tokenize_2(string):
    # Let's create a pattern that contains punctuation marks
    punctuation = re.compile(r'[\.,\?!\*:;()]')

    # Substitute the punctuations with empty strings
    no_punct = re.sub(punctuation, '', string)
    print(no_punct)
    # This is a sample string And here's another one

    # Split sentences by whitespaces
    tokens = re.split('\s+', no_punct)
    return tokens


print(tokenize_2(string))
# ['This', 'is', 'a', 'sample', 'string', 'And', "here's", 'another', 'one']