#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    j = ''
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            j += char
            i += 1
    return j
