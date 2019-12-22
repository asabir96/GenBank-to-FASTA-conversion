import re
import sys
from textwrap import fill as wrapline 

record = <Insert GenBank File>

#Parse the GenBank file for the VERSION and DEFINITION attributes in each individual record. Stitch the attributes together in the same format as a FASTA header 
def get_header(record):
    linesplit = record.split("\n")
    VER = ""
    DEF = ""
    for line in linesplit:
        if "VERSION" in line: #get the version
            space = line.split()
            VER = space[1]
            
        if "DEFINITION" in line: #get the definition
            space = line.split("DEFINITION")
            DEF = str(space[1]).strip().rstrip()
            DEF = str(DEF[:-1])

    #if not DEF or not VER:
      #return "ERROR"
    return ">" + VER + "    " + DEF

get_header(record)


def get_sequence(record):
    '''
    Function to parse the record for the origin sequence and convert it into a FASTA sequence
    '''
    linesplit = record.split("\n")
    origin_seq = False
    Fseq = "  "
    for line in linesplit:
        if origin_seq and "//" not in line:
            space = line.split()
            for i in space[1:]:
                Fseq += i
        if "ORIGIN" in line:
            origin_seq = True
        
    if Fseq:
        Fseq = Fseq.upper() #Uppercase
        Fseq = wrapline(Fseq,width=70)
    
    return Fseq

#Function to write and append the original record to the file  
def write_record(Outfile,FASTA):
    with open(Outfile,"a+") as f:
        f.write(FASTA)


#Function to convert Genbank to FASTA
#Takes the previous header and sequence from the first two functions and joins them to create a FASTA formatted file
def GenBank_to_FASTA(Infile,Outfile):
    with open(Infile,"r") as f:
        record = "  "
        for line in f:
            replaceline = line
            if replaceline.replace("\n","") != "//":
                record += line

            else:
                header = get_header(record)
                sequence = get_sequence(record)
                FASTA = header + "\n" + "".join(sequence) + "\n\n"
                print(FASTA)
                write_record(Outfile,FASTA)
                record = "  "



if __name__ == "__main__":
    input_ = <Insert GenBank File>
    output_ = <Insert FASTA File>
    GenBank_to_FASTA(input_,output_)
    
