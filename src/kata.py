import shlex
import sys
import queue


#
# Apply Method
# @param list
# @param it
# @return
#    
def apply(list, it):
    #your code here
    return list

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply([0, 5, 6, 6, 6],  3))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 