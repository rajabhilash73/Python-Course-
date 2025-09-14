"""
Module is a file containing python code. May contain function classes etc.
used with modular programming used to seprate a program into parts.
"""
import messages
messages.Hello()
messages.Bye()

import messages as msg
msg.Hello()
msg.Bye()

from messages import Hello, Bye
Hello()
Bye()


from messages import *
Hello()
Bye()

help("modules")