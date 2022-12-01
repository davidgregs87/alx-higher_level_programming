#!/usr/bin/python3
from sys import argv

if __name__ != "__main__":
        exit()
elif __name__ == "__main__":
    number = 1
    n_arg = len(argv)
    argc = n_arg - 1
if n_arg == 1:
    print("{} arguments.".format(argc))
elif n_arg == 2:
    print("{} argument:".format(argc))
else:
    print("{} arguments:".format(argc))
for arguments in argv[1:]:
        print("{}: {}".format(number, arguments)),
        number = number + 1
