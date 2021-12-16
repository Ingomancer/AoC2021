from collections import deque

openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
closers = {')': ('(', 3, 1), ']': ('[', 57, 2), '}': ('{', 1197, 3), '>': ('<', 25137, 4)}

def calc_score(input):
    illegal_chars = []
    incomplete_lines = []
    for line in input:
        maybe_corrupted = _check_line_for_errors(line)
        if maybe_corrupted[0]:
            illegal_chars.append(maybe_corrupted[0])
        elif len(maybe_corrupted[1]) != 0:
            incomplete_lines.append(maybe_corrupted[1])
    scores = []
    for line in incomplete_lines:
        fix = []
        score = 0
        for open_bracket in reversed(line):
            fix.append(openers[open_bracket])
        for bracket in fix:
            score *= 5
            score += closers[bracket][2]
        scores.append(score)
    
    return (sum([closers[x][1] for x in illegal_chars]), sorted(scores)[len(scores)//2])

def _check_line_for_errors(line):
    open_brackets = deque()
    for bracket in line:
        if bracket in openers:
            open_brackets.append(bracket)
        else:
            cur_open = open_brackets.pop()
            if cur_open != closers[bracket][0]:
                return (bracket, None)
    return (None, open_brackets)
