#!/usr/bin/env python3

import os

print("Python test: user input")
os.system('mkdir _out')
os.system('touch _out/diff.patch')
os.system('diff -u ~/.vimrc ~/_PRJ/my/sys/vim/.vimrc >> _out/diff.patch')
os.system('vim _out/diff.patch')
decision = input("Remove temp dir? (y/n): ")
if decision == 'y' or decision == 'Y':
    os.system('rm -rf _out')
print("exit")
