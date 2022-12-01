#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for str in range(len(sys.argv)):
        if (str == 0):
            continue
        else:
            res += int(sys.argv[str])
    print("{}".format(res))
