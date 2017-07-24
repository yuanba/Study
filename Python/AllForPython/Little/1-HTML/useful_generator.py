#!/usr/bin/python3

def lines(file):
    for line in file:
        yield line
    yield '\n'    # Promissing that the file must have the ending.

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block)
            block = []


