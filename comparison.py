#! /usr/bin/env python3
# coding: utf-8

"""
=================================================
  Analyse Woman / Man balance in expression rate
=================================================
"""
import argparse
import re
import logging as lg

import analysis.file_csv as c_an


lg.basicConfig(level=lg.DEBUG)

def parse_arguments():
    """ Get arguments from the command line
    to get different results according to our needs.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of
        information about women's expression rate in radio and TV channels""")
    parser.add_argument("-y", "--year",type=int, help="""year's study""")
    parser.add_argument("-c", "--bychannel", action='store_true', help="""displays
        a graph for each channel""")
    parser.add_argument("-t", "--bytype", action='store_true', help="""displays
        a graph by type of channel (tv or radio) """)

    return parser.parse_args()

if __name__ == '__main__':
    ARGS = parse_arguments()
    try:
        DATAFILE = ARGS.datafile
        YEAR = ARGS.year
        if DATAFILE is None:
            raise Warning('You must indicate a datafile!')
        if YEAR is None:
            raise Warning('You must indicate the year!')
        if YEAR not in range(2002, 2019):
            raise Warning('You must indicate a valid year between 2002 and 2019!')
    except Warning as exception:
        lg.warning(exception)
    else:
    		c_an.launch_analysis(DATAFILE, YEAR, ARGS.bychannel, ARGS.bytype)
    finally:
        lg.info('#################### Analysis is over ######################')

