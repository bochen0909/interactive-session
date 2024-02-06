import interactive_session as m
assert m.__version__ == "0.0.1"
assert m.add(1, 2) == 3
assert m.subtract(1, 2) == -1

session = m.InteractiveSession("bash", "exit")
print(session.execute("echo hello"))
session.close()
