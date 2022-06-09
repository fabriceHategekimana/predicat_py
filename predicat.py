from cli import *
import os.path
from os import path
import sys

if len(sys.argv) > 1:
    runFromExternal(" ".join(sys.argv[2:]))
else:
    MyPrompt().cmdloop()

