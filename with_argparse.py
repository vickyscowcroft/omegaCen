#!/usr/bin/env python
# coding: utf-8

import os, re
import argparse
import requests

# this script will query ADS to collect the citations used in a LaTeX file
# into a BibTeX file

# you can add your own command-line option parsing and help line
# using getopt or optparse; we'll assume a command-line single argument FILE
# (given by sys.argv[1]), read from FILE.aux, and write to FILE.bib

# FIRST, we'll collect all citation keys from FILE.aux;
# citations will look like \citation{2004PhRvD..69j4017P,2004PhRvD..69j4017P}

def import_ads(filename):

    auxfile = filename + '.aux'
    bibfile = filename + '.bib'

    cites = set()   # start with an empty set (like list, not ordered, no repetitions)

    with open(auxfile,'r') as aux:
        for line in aux:                                # Python idiom—loop over every line from file
            m = re.search(r'\\citation\{(.*)\}',line)   # match \citation{...}, collect the ...
                                                        # note that we escape \, {, and }
            if m:
                cites.update(m.group(1).split(','))     # if there's a match, split string by commas
    #                                                   # add the resulting keys to set

    # # check: print "Seek:", cites

    # # SECOND, we'll check what refs we have already in FILE.bib, to avoid
    # # repetitive querying of ADS; references will look like
    # # @TYPE{key,
    # # ...

    haves = []

    if os.path.isfile(bibfile):                 # the bibfile exists...
        with open(bibfile, 'r') as bib:
            for line in bib:
                m = re.search(r'@.*?\{(.*),',line)  # .*\{ means "any # of any char followed by {";
                                                    # .*?\{ means "the shortest string matching
                                                    #              any # of any char followed by {"
                if m:
                    haves.append(m.group(1))        # remember: append item to list
                                                #           extend list with list
                                                #           add item to set
                                                #           update set with list
    else:
        print('Bibliography file does not exist. We will write one.')

    new_citations = list(cites - set(haves))
    num_new = len(new_citations)

    if num_new == 0:
        print('No new citations found. Exiting.')
        return
    elif num_new == 1:
        print('1 new citation found.')
    else:
        print('{} new citations found.'.format(num_new))

    # # check: print "Have:", haves

    # # THIRD, we'll query ADS for all the keys that are not in haves,
    # # and write the resulting bibtex entries to FILE.bib

    with open(bibfile,'a') as bibtex:
        for c in new_citations:
            r = requests.post('http://adsabs.harvard.edu/cgi-bin/nph-bib_query',    # CGI script
                              data = {'bibcode': c, 'data_type': 'BIBTEX'} )        # CGI parameters (note pretty indent)

    # we could also have done a (more restrictive) GET HTTP request
    # r = requests.get('http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=%s&data_type=BIBTEX' % c)
    # where % yields the Python %-formatting for strings

            if r.ok:                                            # found it!
                m = re.search(r'(@.*\})',r.content,re.DOTALL)   # get everything after the first @
                                                                # until the last }
                bibtex.write(m.group(1) + '\n')                 # write to file with extra newline
                # check: print "Found:", c
            else:
                bibtex.write('@MISC{%s,note="{%s not found in ADS!}"}' % (c,c))
#                                                             # record not found,
#                                                             # we'll write a useful note in bibtex
#             # check: print "Not found:", c

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', 
                        help='name of file with ADS citations')

    filename = parser.parse_args().filename.split('.')[0] # only restriction is that filename cannot contain period before extension

    import_ads(filename)
