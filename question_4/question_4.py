# Given a sequence of open and closed brackets, make an algorithm to determine whether or not the sequence is valid or not
# i.e. (()()) is valid, but ((() is not

def is_sequence_valid(input_string):
    pass


result_1 = is_sequence_valid("(((())))")
assert result_1 is True

result_2 = is_sequence_valid("(((()()))())")
assert result_2 is True

result_3 = is_sequence_valid("(((()()))())(())()")
assert result_3 is True

result_4 = is_sequence_valid("(((()()))((())()")
assert result_4 is False

result_5 = is_sequence_valid("(((()())))))")
assert result_5 is False
