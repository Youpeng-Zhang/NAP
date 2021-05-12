# NAP
NAP is a neutralizing antibody prediction algorithm for COVID-19 based on dipeptide coding.

############################################################
########################Preparation#########################
############################################################

Please make the following preparations before using:

1. Install Python3 and add it to the global variable
   You can get the latest release version of Python3 at  at https://www.python.org

2. Install the required packages for python from the command line
   pip3 install sklearn

3.Prepare your input file in the format of example_input.fasta at the folder "NAP"

############################################################
#########################Prediction#########################
############################################################

##########################Command###########################

python3 /path/to/NAP/neutralizing_prediction.py parameters

#########################Parameters#########################

-h           show help information

-p           specify the path to the location of the folder "NAP"

-i           specify the input file

-o           specify the output file

##########################Example###########################

python3 /Users/Zhang/Downloads/NAP/neutralizing_prediction.py -p /Users/Zhang/Downloads/ -i /Users/Zhang/Downloads/NAP/example_input.fasta -o /Users/Zhang/Downloads/NAP/example_output.txt

