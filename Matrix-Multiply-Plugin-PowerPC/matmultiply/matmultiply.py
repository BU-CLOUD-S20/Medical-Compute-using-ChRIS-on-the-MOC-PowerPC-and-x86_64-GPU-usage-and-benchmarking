#!/usr/bin/env python                                            #
# matmultiply ds ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
import csv
import MatCal

sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp

Gstr_title = """

                  _                   _ _   _       _       
                 | |                 | | | (_)     | |      
  _ __ ___   __ _| |_ _ __ ___  _   _| | |_ _ _ __ | |_   _ 
 | '_ ` _ \ / _` | __| '_ ` _ \| | | | | __| | '_ \| | | | |
 | | | | | | (_| | |_| | | | | | |_| | | |_| | |_) | | |_| |
 |_| |_| |_|\__,_|\__|_| |_| |_|\__,_|_|\__|_| .__/|_|\__, |
                                             | |       __/ |
                                             |_|      |___/ 



"""

Gstr_synopsis = """
(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)
    NAME
       matmultiply.py 
    SYNOPSIS
        python matmultiply.py                                         \\
            <inputDir>                                                  \\
            <outputDir> 
    BRIEF EXAMPLE
        * Bare bones execution
            mkdir in out && chmod 777 out
            python matmultiply.py   \\
                                in    out
    DESCRIPTION
        `matmultiply.py` ...
    ARGS

"""


class Matmultiply(ChrisApp):
    """
    An app to ....
    """
    AUTHORS = 'kefan (kefan29@bu.edu)'
    SELFPATH = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC = os.path.basename(__file__)
    EXECSHELL = 'python3'
    TITLE = 'A ChRIS plugin app'
    CATEGORY = ''
    TYPE = 'ds'
    DESCRIPTION = 'An app to ...'
    DOCUMENTATION = 'http://wiki'
    VERSION = '0.1'
    ICON = ''  # url of an icon image
    LICENSE = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('-c','--coe',
                          dest      =   'coenum',
                          type      =   str,
                          optional  =   True,
                          help      =   'assign coe range, default 32, assign by startNumber : stepLength : endnumber',
                          default   =   '32')

    def run(self,options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)

        self.clist = self.generateCOElist(options.coenum)
        print("clist:" + str(self.clist))######################
        if len(self.clist) != 0:
            for cnum in self.clist:
                print("cur cnum is " + str(cnum)) ######################
                c = int(cnum)
                obj = MatCal.MatMulBench(c)
                ms, st, ft, et = obj.Run()
                print("cur list of pars:" + str([ms,st,ft,et])) ######################
                parse = [{'Matrix_Size': ms, 'Start_Time': st, 'Finish_Time': ft, 'Elapse_Time': et}]
                self.createOrUpdate(parse, options.inputdir, options.outputdir)
                print(parse)

    def createOrUpdate(self, parse, indir, outdir):
        headers = ["Matrix_Size", "Start_Time", "Finish_Time", "Elapse_Time"]
        # open an csv file at current dictionary with name database.csv

        # print("indir: " + os.getcwd() + "/" + indir)
        # print("outdir: " + os.getcwd() + "/" + outdir)
        # print("current path: " + os.getcwd())
#
        # # os.chdir(os.getcwd() + "/" + outdir)
        # print("cur dir : " + os.getcwd())

        # print("indir is :" + os.path.abspath(indir))
        # childdir = os.path.abspath(indir)
        # os.chdir(outdir)
        # print("chdir finished, cur path:" + os.getcwd())

        filepath = outdir  + '/MultiplyRecord.csv'

        print("filepath:" + filepath)
        if (os.path.exists(filepath)):
            # if the file exist add the value of the dictionary,else will build a new file with the header
            with open(filepath, 'a+') as f:

                f_csv = csv.DictWriter(f, headers)
                for item in parse:
                    f_csv.writerow(item)
        else:
            # %s/timestamp.json' % options.outputdir,
            with open(filepath, 'a+') as f:
                f_csv = csv.DictWriter(f, headers)
                # write headers to database.csv
                f_csv.writeheader()
                # write values of input Python Dictionary to database.csv row by row
                for item in parse:
                    f_csv.writerow(item)
    def generateCOElist(self,cpar):
        ## assume input as 32,100,500
        ## start,step,end
        ## start < end, step positive number
        COElist = []
        pars = cpar.split(',')
        if len(pars) == 1:
            COElist.append(pars[0])
        elif len(pars) != 3:
            print("Unexpected error with COE parameter, try correct format like \"32,32,128\" ")
        elif int(pars[0]) > int(pars[2]) or int(pars[0]) <= 0 or int(pars[2]) <= 0 or int(pars[1]) <=0:
            print("start coe must be less than finish coe, no negative or zero is allowed!")
        else:
            cur = int(pars[0])
            step = int(pars[1])
            end = int(pars[2])
            while cur <= end:
                COElist.append(cur)
                cur += step
        return COElist



    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    chris_app = Matmultiply()
    chris_app.launch()
