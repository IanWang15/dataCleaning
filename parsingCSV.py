# read the input CSV DATAFILE line by line, and split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
import os

DATADIR = "./"
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
		header = f.readline().split(",")
#		print header
# ['Title', 'Released', 'Label', 'UK Chart Position', 'US Chart Position', 'BPI Certification', 'RIAA Certification\n']
#		print header[6].strip()
		counter = 0
#		print f.readline()
		for line in f:
#		    print line
		    # ex. Please Please Me,22 March 1963,Parlophone(UK),1,-,Gold,Platinum
		    if counter == 10: # process 10 lines only in this practise, because the following lines have different format
		        break
		    fields = line.split(",")
		    entry = {} # create an empty dictionary
		    
		    for i,value in enumerate(fields):
#		        print fields
		        # ex. ['Please Please Me', '22 March 1963', 'Parlophone(UK)', '1', '-', 'Gold', 'Platinum\n']
#		        print i, value
		        # ex. 0 With the Beatles
#		        print value.strip()
#		        print header[i].strip()
		        entry[header[i].strip()] = value.strip()
		        # dict[key] = list
		        # add a list into the dictionary
		        # ex. {'Title': 'Please Please Me', 'UK Chart Position': '1'...}       
# Python string method strip() will come in handy to get rid of the extra whitespace (that includes newline character at the end of line)
# like 'RIAA Certification\n' becomes 'RIAA Certification'
# \n comes from using .split(",") to split the line.
		    data.append(entry)
		    # add a dictionary to a list
		    counter += 1

    return data # the return is a list of dictionaries,


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

#    print d[0]
    assert d[0] == firstline
    assert d[9] == tenthline

    
test()
