# Task, make the lambda functions return the correct values when called.
def append_string(msg):
    return msg + "ight"

funcList=[]
for m in ('fl', 'm', 'bl', 't'):
    funcList.append(lambda: append_string(m))

# Don't touch anything below here.
result = [f() for f in funcList]
expected = ["flight", "might", "blight", "tight"]

assert result == expected
