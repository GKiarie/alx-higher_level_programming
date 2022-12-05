#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup = (0, None)
        return tup
    return (len(sentence), sentence[0])
