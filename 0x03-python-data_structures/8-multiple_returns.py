#!/usr/bin/python3
def multiple_returns(sentence):
    sentlen = len(sentence)
    if sentence:
        return (sentlen, sentence[0])
    else:
        return (0, None)
