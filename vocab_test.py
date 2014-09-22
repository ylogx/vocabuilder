#!/usr/bin/env python2
#
#  vocab_test.py - Use files created by vocab_enter_word.py or by you and ask you test questions
#
#  Copyright (c) 2014 Shubham Chaudhary <me@shubhamchaudhary.in>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys,time
import os,re
import string
from tts import *
from random import *

printable = set(string.printable)

def filter_out_hindi(data_str):
    ''' Remove the hindi character from string '''
    out_str = ""
    if not data_str:
        return;
    for char in data_str:
        if char in printable:
            out_str += char
            #TODO: Change (n) to noun
    return out_str;

def get_tuples(filename):
    return NotImplemented;

def get_tuples_from_line(line):
    ''' Seperate out word and its meaning using regex '''
    if not line:
        print 'Nothing passed';
        return;
    match = re.search(r'(\w+)\s-\s([\S \s]*)',line);
    word = ''; meaning = ''
    if match:
        word = match.group(1);
        meaning = match.group(2);

    if word or meaning: #XXX
        return (word,meaning);
    return None;

def parse(filename=None):
    if not filename:
        #Get directory for file
        filename = os.path.expanduser('~/vocab/')
        if not os.path.exists(filename):
            os.mkdir(os.path.expanduser('~/vocab/'))
            filename = os.path.expanduser('~/vocab/');
        # filename as current date
        filename += time.strftime("%m%d.txt");   ## "%d/%m/%Y"  ## dd/mm/yyyy format
    try:
        f = open(filename,'rU');
        lines = f.readlines();
        for line in lines:
            line = filter_out_hindi(line);
            ret_tuple = get_tuples_from_line(line);
            if not ret_tuple:
                print 'Empty/Wrong formatted line';
                continue;
            (word, meaning) = ret_tuple[0],ret_tuple[1];
            print 'Word:',word;
            say('Word is: '+word);
            print 'Meaning:',meaning;
            say('Meaning is: '+meaning);
#             print line,; say(line);
        f.close();
#     except FileNotFoundError:
#         print 'Sorry file not found';
    except:
        raise;

def parse_randomized(filename,randomize):
    #TODO
    return NotImplemented

def main(argv):
    from optparse import OptionParser
    usage = "%prog [-c] [-f filename]"#%sys.argv[0];
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option("-c", "--custom", action='store_true', dest="custom", default=False, help="Open Custom user specified file")
    parser.add_option("-f", "--file", type='str', dest="file", help="Use the specified file")
    parser.add_option("-l", "--list", action='store_true', dest="lst", default=False, help="Open list of files from following arguments")
    (options, args) = parser.parse_args()
    if options.file:
        parse(options.file);
    elif options.custom:
        if args:
            parse(args[0]);
    elif options.lst:
        if args:
            files = list(args);
            print 'Total %d files passed.'%len(files);
            while files:
                #Randomize list
                index = randint(0,len(files)-1);
                print 'Currently Parsing: ',files[index];
                parse(files.pop(index));
#             for filename in args:
#                 parse(filename);
    else:
        parse();

    return;


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv));
    except KeyboardInterrupt:
        print('\nExiting gracefully\n');
    except:
        raise;
