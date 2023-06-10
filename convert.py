#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input(encoding="utf-8", inplace=True, backup='.bak'):
    print(re.sub(r'(\(.*?)(\#.*?\))',
                 lambda m: m.group(1) + m.group(2).lower(), line), end='')
