import argparse
import re

parser = argparse.ArgumentParser(description='MySQL trace file reformat')
parser.add_argument(dest= 'trace_file', type= str, help= 'trace file path',)

args = parser.parse_args()

class frame():
    
    pattern = '(\w*.\w*): *(\d*):? *(.*) *([<>])(.*)'
    
    def __init__(self, string_line):
        self.meta = string_line
        
        self.matchObj = re.search( frame.pattern, string_line, re.I)
        if self.matchObj is not None:
            self.file        = self.matchObj.group(1)
            self.line        = self.matchObj.group(2)
            self.indentation = self.matchObj.group(3)
            self.in_out      = self.matchObj.group(4)
            self.func_name   = self.matchObj.group(5)


if __name__=="__main__":
    with open(file=args.trace_file, mode='r') as f:
        for i in f:
            l = frame(i)
            if l.matchObj is None:
                print(l.meta)
            elif l.in_out == ">":
                print(l.indentation + l.in_out + ' ' + l.func_name + ' (' + l.file + ':' + l.line +')')
            else:
                print(l.indentation + l.in_out + ' ' + l.func_name)
