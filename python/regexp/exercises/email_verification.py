import re

string = "132456@hyperskill org"
template = r"[a-z0-9\-\.=_]{6,30}@(gmail\.com|(jetbrains|hyperskill)\.org)"

match = re.match(template, string)

if match:
    print(match)
else:
    print("No result")