import re

def customsplit(inputstring, customdelimiters):
    output = list(filter(None, re.split('|'.join(map(re.escape, customdelimiters)), inputstring)))
    return output
inputstring = 'sdfkdjsadfsd diweiw; 1231:foo'
customdelimiters = [' ', 's', ':','2']

output=customsplit(inputstring, customdelimiters)
print(output)