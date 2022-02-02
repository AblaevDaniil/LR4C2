#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def clear_str(string):
        r = ""
        for s in string:
            if s in "()[]{}<>":
                r = r + s
        return r


    # Проверка

    def check_par(string):
        if len(string) == 0:
            return True
        else:
            f = string[0]
            l = string[-1]
            kf = "([{<".find(f)
            if kf == -1:
                return False
            if l == ")]}>"[kf]:
                return check_par(string[1:len(string) - 1])
            else:
                return False

    def task(string):
        return check_par(clear_str(string))


    print(task(input()))

