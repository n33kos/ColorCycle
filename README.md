# ColorCycle
A python script to modify hex values in a file or string based on various filters


#### Arguments:
  - `-s | -f {string|path}` Select string or file mode
  - `-m {method}` Select modulation method {modulation values are +-16 }
  - `-o {filename}` Select output file name        

#### Examples:
  - `python3 colorcycle.py -s "#0055CC"`
  - `python3 colorcycle.py -s "Here is my color to modify #ffaa55." -m darken 10`
  - `python3 colorcycle.py -f ./test.css -m cycle 12`
  - `python3 colorcycle.py -f ./test.css -o /apps/creations/colorlist_new.css -m invert`
