#!/usr/bin/python3
for iin range(100):
    if i == 99:
        print(i)
    else:
        print("{}".format('0' + str(i) if i < 10 else i), end=", ")
