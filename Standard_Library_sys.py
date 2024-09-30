# sys is a built-in module that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
import sys
arguments = sys.argv
print(f"We received the following arguments:")
for arg in arguments:
    print(f" - {arg}")

print(f"We are running on a '{sys.platform}' machine")


