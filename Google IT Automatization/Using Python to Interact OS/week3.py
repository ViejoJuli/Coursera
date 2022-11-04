#!/usr/bin/env python3
import re

log = "hola [12345] hola"
regex = r"\[(\d+)\]"  # r is for raw strings
result = re.search(regex, log)  # patern, place. re.IGNORECASE to avoid uppercases
print(result[1])
print(re.findall(r"cat|dog", "i love cats and dogs"))


def repeating_letter_a(text):
    result = re.search(r"[aA].*[aA]", text)
    return result != None


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
    return result != None


print(re.search(r"^A.*a$", "Australia"))
# Capturing Groups
result = re.search(r"^(\w*), (\w*)$", "Rios, Julian")  # Use () to group
print(result.groups())
print(result[1])
f"{result[2]} {result[1]}"


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w.*\.)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2, \1", "Rios, Julian")
