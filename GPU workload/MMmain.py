import sys, os

sys.path.insert(1, os.path.join(os.path.dirname(__file__), '../MatrixMul'))

from MatrixMulbench import MatrixMultiply
from argparse import RawTextHelpFormatter
from argparse import ArgumentParser

str_version = "0.0.1"
str_desc = "Matrix Multiplexing Test" + " " + str_version

def synopsis(ab_shortOnly=False):
    scriptName = os.path.basename(sys.argv[0])
    shortSynopsis = '''
    NAME
        %s - running matrix multiplication test locally.
    SYNOPSIS
            %s                                          \\
                -C |--COE <COE TPBxCOE = matrix size(Ract matrix>
                ## TPB fixed for 32
                [-t|--timeSpent <ElapseTime>]
                
    BRIEF EXAMPLE
        %s                                              \\
                -C 128                                  \\
                -t                                      \\
    ''' % (scriptName, scriptName, scriptName)

    description = '''
    DESCRIPTION
        ''This is description for %s 
    
    ARGS
        -C |--COE  <COE TPBxCOE = matrix size(Ract matrix>
        Assign the COE argument
        [-t|--timeSpent <ElapseTime>]
        Whether to print out the elapse time or not, print out when with '-t True'
        otherwise with '-t False'
        
        
        
    EXAMPLE
        MatrixMultiply -C 128                           \\
                        -t True
        
    ''' % (scriptName)
    if ab_shortOnly:
        return shortSynopsis
    else:
        return shortSynopsis + description

parser = ArgumentParser(description=str_desc, formatter_class=RawTextHelpFormatter)

parser.add_argument("-C", "--COE",
                    help="assign COE parameter",
                    dest='COEnumber',
                    default=128)
parser.add_argument("-t", "--timeSpent",
                    help="elapse time",
                    dest='ElapseTime',
                    default='True')

args = parser.parse_args()

if args.man or args.synopsis:
    print(str_desc)
    if args.man:
        str_help = synopsis(False)
    else:
        str_help = synopsis(True)
    print(str_help)
    sys.exit(1)

if args.b_version:
    print("Version: %s" % str_version)
    sys.exit(1)

Matrix_Multiply = MatrixMultiply.MatBench(
    COEnumber=args.COEnumber,
    ElapseTime=args.ElapseTime
)

# run the program
d_MatrixMultiply = Matrix_Multiply.Run()

if args.ElapseTime == 'True':
    print(d_MatrixMultiply)

sys.exit(0)

