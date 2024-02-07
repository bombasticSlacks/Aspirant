#!/usr/bin/env python3
#embeds md blocks
import os
import subprocess

rootdir = "Game"
dir = "Game/Blocks"

for block in os.listdir(dir):
    # Skip .bak files
    if block.find(".bak") == -1:
        address = dir + "/" + block
        name = block.strip(".md")
        print(address)
        print(name)
        f = open(address, "r")

        # Wrap our block with some HTML
        contents = '<div markdown="1" class="block">\n'
        contents += f.read()
        contents += '\n</div>'

        # find the relevant files
        result = subprocess.run(["grep", "-r", "-l", "--regexp=!\[.*\](\/Blocks\/.*)", "Game/"], capture_output=True, text=True)
        files = result.stdout.split("\n")
        # remove last empty entry
        files.pop()
        for fi in files:
            print(fi)
            with open(fi, 'r') as fileBuffer:
                fileContents = fileBuffer.read()

            # Replace the strings
            fileContents = fileContents.replace(f'![{name}](/Blocks/{name})', contents)
        
            # Replace the file
            with open(fi, 'w') as fileBuffer:
                fileBuffer.write(fileContents)

