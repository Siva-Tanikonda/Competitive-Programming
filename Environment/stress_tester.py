import os
import filecmp
import sys
import time

def printFileContents(name):
    file = open(name, "r")
    file_contents = file.read()
    file_contents = file_contents[:-1]
    print(file_contents)
    file.close()

class color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    END = "\033[0m"

#You need arguments when running the scripts
fileBase = sys.argv[1]
fileName = sys.argv[2]
directoryBase = sys.argv[3]

print("Beginning process...")

#These are just the build commands
os.system("g++ -std=c++17 -fdiagnostics-color=always -Wall -Wno-pragmas -Wno-attributes -o " + "build\\" + fileBase + "_generator_compiled -g " + fileBase + "_generator.cpp")
os.system("g++ -std=c++17 -fdiagnostics-color=always -Wall -Wno-pragmas -Wno-attributes -o " + "build\\" + fileBase + "_compiled -g " + fileBase + ".cpp")
os.system("g++ -std=c++17 -fdiagnostics-color=always -Wall -Wno-pragmas -Wno-attributes -o " + "build\\" + fileBase + "_slow_compiled -g " + fileBase + "_slow.cpp")
print("Building complete...")

#Change this if you want to run more or fewer tests
n = 100

print("Beginning tests...")
for i in range(1, n + 1):
    print("Test " + str(i) + ":", end = " ")
    os.system("build\\" + fileBase + "_generator_compiled > \"" + directoryBase + "\\input.txt\"")
    os.system("build\\" + fileBase + "_compiled < \"" + directoryBase + "\\input.txt\" > " + fileBase + "_output.txt")
    os.system("build\\" + fileBase + "_slow_compiled < \"" + directoryBase + "\\input.txt\" > " + fileBase + "_slow_output.txt")
    res = filecmp.cmp(fileBase + "_output.txt", fileBase + "_slow_output.txt")
    if (not res):
        print(color.RED + "FAILED" + color.END)
        print(color.BOLD + "input.txt:", color.END)
        printFileContents(directoryBase + "\\input.txt")
        print(color.BOLD + fileBase + "_output.txt:", color.END)
        printFileContents(fileBase + "_output.txt")
        print(color.BOLD + fileBase + "_slow_output.txt:", color.END)
        printFileContents(fileBase + "_slow_output.txt")
        break
    else:
        print(color.GREEN + "SUCCESS" + color.END)
print("Done")