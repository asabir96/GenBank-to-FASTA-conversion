# GenBank-to-FASTA-conversion
#Convert Gebbank entries into FASTA file format

#get_header() function will accept a parameter(a GenBank Record).
#Function will parse for the VERSION and DEFINITION values within record and stitch them together to form a FASTA header.

#get_sequence() function will accept a parameter(a GenBank Record).
#Function wil parse for the ORIGIN value within record and convert sequence into FASTA format.

#split_records() function will accept a parameter(Filename)
#Function will open the file and read it so it can split the file into individual GenBank records

