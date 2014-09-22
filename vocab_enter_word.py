#!/usr/bin/env python3
#
#  vocab_enter_word.py - create a list of vocabulary words maintained in files named uniquely by current date and month
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


import os,sys,time;

def file_len(fname):
#     return sum(1 for line in open(fname))
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def enter_words(word,meaning):
    line_to_write = word.capitalize() +' - '+meaning;
    #Process word and meaning
    line_to_write = line_to_write.replace('\n','\t');
    #At the end of line
    line_to_write += '\n';

    #Get directory for files
    filename = os.path.expanduser('~/vocab/')
    if not os.path.exists(filename):
        os.mkdir(os.path.expanduser('~/vocab/'))
        filename = os.path.expanduser('~/vocab/');
    # filename as current date
    filename += time.strftime("%m%d.txt");   ## "%d/%m/%Y"  ## dd/mm/yyyy format

    try:
        f = open(filename,'a');
        f.write(line_to_write);
        f.close();
    except FileNotFoundError:
        print('Sorry file not found')
    except:
        raise;

    print('Added',word.capitalize(),'to file: ',filename);
    print(file_len(filename),'words added so far');# to',filename);
    return;

def get_input(msg):
    word = input('%s: '%msg).strip();
    while not word:
        print('Error: Empty String')
        word = input('%s again: '%msg).strip();
    return word;

def cat_today():
    # filename as current date
    filename = os.path.expanduser('~/vocab/')
    filename += time.strftime("%m%d.txt");   ## "%d/%m/%Y"  ## dd/mm/yyyy format

    try:
        f = open(filename,'rU');
        data_list = f.readlines()
        f.close();
    except FileNotFoundError:
        print('File not found!')
        print('Do some work and then call me.')
        return;
    except:
        raise;
    if data_list:
        print('%d words in %s\n'%(len(data_list),filename));
        for i in range(len(data_list)):
            print('%d: %s'%(i+1,data_list[i]), end='');
    return ;


def main(argv):
    from optparse import OptionParser
    usage = "%prog [word] [-c]"#%sys.argv[0];
    parser = OptionParser(usage=usage, version="%prog 1.0")
    parser.add_option("-c", "--cat", action='store_true', dest="cat", default=False, help="Show today's file")
    parser.add_option("-t", "--today", action='store_true', dest="today", default=False, help="Show today's file")

    (options, args) = parser.parse_args()
    if options.cat or options.today:
        cat_today();
        return;
    if args:
        argc = len(args);
        if argc == 1:
            word = args[0];
            meaning = get_input('Enter meaning of '+word.capitalize());
        elif argc == 2:
            word = args[0];
            meaning = args[1];
        else:
            print('Unknown number of arguments');
            return;
    else:
        word = get_input('Enter word');
        meaning = get_input('Enter meaning');
    try:
        enter_words(word,meaning);
    except:
        raise;

if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv));
    except KeyboardInterrupt:
        print('\nDidn\'t save anything\n');
    except:
        raise;

