# Task: Fix the bug without touching MyClass or increment_all
class MyClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def __eq__(self, other):
        return other.value == self.value


def increment_all(classes):
    for c in classes:
        c.increment()


first_list = [MyClass(1), MyClass(2)]

second_list = first_list.copy()
increment_all(second_list)

expected_1 = [MyClass(1), MyClass(2)]
expected_2 = [MyClass(2), MyClass(3)]

assert first_list == expected_1
assert second_list == expected_2
