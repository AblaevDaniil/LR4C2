#!/usr/bin/env python3
# -*- coding: utf-8 -*-

openList = ["(","["]
closeList = [")","]"]
def balance(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"

if __name__ == '__main__':
    print(balance("([)]"))