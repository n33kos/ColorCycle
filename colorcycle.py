#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------ColorCycle Version 1.1--------
#This script replaces all Hex color values in a file or string with a new value based on various methods of modulation.
#    Arguments:
#        Select string or file mode     [-s | -f] {string or file path : string}
#        Select modulation method       [-m] {modulation method(invert,cycle,darken,lighten) :string} {modulation value(+-16) :integer}
#        Select output file name        [-o] {file path : string}
#   Examples:
#        python3 colorcycle.py -s "#0055CC"
#        python3 colorcycle.py -s "Here is my color to modify #ffaa55." -m darken 10
#        python3 colorcycle.py -f ./test.css -m cycle 12
#        python3 colorcycle.py -f ./test.css -o /apps/creations/colorlist_new.css -m invert

import os, sys, re

#---------Global Variables-----------
f = []
sourcetext = ''
method = ''
modulation = ''
outputfilename = ''
modulationvalue = 0
args = sys.argv

#---------Parse Arguments-----------
for i, arg in enumerate(args):
    if arg == "-m":
        if i+1 < len(args):
            modulation = args[i+1]
            if i+2 < len(args):
                modulationvalue = int(args[i+2])
        else:
            print("You must select a modulation: invert, cycle {+-16}, darken {1-16}, lighten {1-16}")
            raise SystemExit
    if arg == "-f":
        if i+1 < len(args):
            sourcetext = args[i+1]
            method = 'file'
        else:
            print("You must include a file name/path")
            raise SystemExit
    if arg == "-o":
        if i+1 < len(args):
            outputfilename = args[i+1]
        else:
            print("You must include an output file name/path")
            raise SystemExit
    if arg == "-s":
        if i+1 < len(args):
            sourcetext = args[i+1]
            method = 'string'
        else:
            print("You must include a string to modify")
            raise SystemExit

if modulation == '':
    modulation = 'invert'

#------------Functions---------------
def openFile(filename):
    global f
    f = open(filename, 'r')

def closeFile(filevar):
    filevar.close()

def savefile(filename, newcontents):
    if outputfilename != '':
        print("\nSaving " + str(outputfilename) + "...")
        f_results = open(outputfilename, 'w')
    else:
        print("\nSaving " + str(filename) + "...")
        f_results = open(filename, 'w')
    f_results.write(newcontents)
    closeFile(f_results)

def process_file(filename):
    global f
    openFile(filename)
    print('Reading From ' + str(f.name) + '...')
    filecontent = f.read()

    if modulation == "invert":
        print('Running Invert Modulation...\n')
        result = modulation_invert(filecontent)

    elif modulation == "cycle":
        print('Running Cycle Modulation...\n')
        result = modulation_cycle(filecontent)

    elif modulation == "darken":
        print('Running Darken modulation...\n')
        result = modulation_darken(filecontent)

    elif modulation == "lighten":
        print('Running Lighten modulation...\n')
        result = modulation_lighten(filecontent)
    else:
        print('modulation not found.')

    savefile(filename + '.color_cycled', result)

def process_string(sourcetext):
    if modulation == "invert":
        print('Running invert Modulation...\n')
        result = modulation_invert(sourcetext)
    elif modulation == "cycle":
        print('Running Cycle Modulation...\n')
        result = modulation_cycle(sourcetext)
    elif modulation == "darken":
        print('Running Darken modulation...\n')
        result = modulation_darken(sourcetext)
    elif modulation == "lighten":
        print('Running Lighten modulation...\n')
        result = modulation_lighten(sourcetext)
    else:
        print('modulation not found.')

    #output final string
    print(result)

def modulation_cycle(val):
    #Get all matches
    regex = re.compile("#[A-Fa-f0-9]{3,6}", re.IGNORECASE)
    match_array = regex.findall(val)

    #replace values
    for match in match_array:
        og_string = '123456789abcde'
        if modulationvalue >= 0:
            cycled_string = og_string[modulationvalue:] + og_string[:modulationvalue]
        else:
            cycled_string = og_string[modulationvalue:] + og_string[:modulationvalue]

        table = str.maketrans(og_string,cycled_string)

        replace = match.lower().translate(table).upper()
        print(match + " -> " + replace)
        val = val.replace(match, replace, 1)
    return val

def modulation_invert(val):
    #Get all matches
    regex = re.compile("#[A-Fa-f0-9]{3,6}", re.IGNORECASE)
    match_array = regex.findall(val)

    #replace values
    for match in match_array:
        table = str.maketrans('0123456789abcdef', 'fedcba9876543210')

        replace = match.lower().translate(table).upper()
        print(match + " -> " + replace)
        val = val.replace(match, replace, 1)
    return val

def modulation_darken(val):
    #Get all matches
    regex = re.compile("#[A-Fa-f0-9]{3,6}", re.IGNORECASE)
    match_array = regex.findall(val)

    #replace values
    for match in match_array:
        og_string = '0123456789abcdef'
        zerocount = ''
        for i in range(0, modulationvalue):
            zerocount += '0'
        cycled_string = zerocount + og_string[:16-modulationvalue]
        table = str.maketrans(og_string,cycled_string)

        replace = match.lower().translate(table).upper()
        print(match + " -> " + replace)
        val = val.replace(match, replace, 1)
    return val

def modulation_lighten(val):
    #Get all matches
    regex = re.compile("#[A-Fa-f0-9]{3,6}", re.IGNORECASE)
    match_array = regex.findall(val)

    #replace values
    for match in match_array:
        og_string = '0123456789abcdef'
        effcount = ''
        for i in range(0, modulationvalue):
            effcount += 'F'
        cycled_string = og_string[modulationvalue:] + effcount
        table = str.maketrans(og_string,cycled_string)

        replace = match.lower().translate(table).upper()
        print(match + " -> " + replace)
        val = val.replace(match, replace, 1)
    return val

#------------Execute---------------
if method == "file":
    process_file(sourcetext)
elif method == "string":
    process_string(sourcetext)
else:
    print("You must select either -s \"string\" for a string of -f \"filename\" for a file")
    raise SystemExit
