
import re
# mail = 'y65==bigey.n6b7xdnw.g@hyperskill.org'
other_mail = 'my_mail.is.this-one@gmail.org'
regex = r"[a-z\d\.\-_=]{6,30}@gmail\.org"

matchh = re.match(regex, other_mail)

if matchh:
    print("\nmatch")
else:
    print("no match")

print(matchh)
