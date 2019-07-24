#!/usr/bin/env python
#read file
#find and return the min, max and average values for the COAST region
#find and return the time value for the min and max entries

import xlrd
from zipfile import ZipFile
datafile = "./2013_ERCOT_Hourly_Load_Data.xls"
datafile0 = "./2013-ercot-hourly-load-data"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0) # 0 means the first sheet in xls file
    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    cv = sheet.col_values(1,start_rowx=1, end_rowx=None)# load the 1st column; column slicing tech
    maxval = max(cv) # find the maximum value in 1st column
    minval = min(cv)
    
    maxpos = cv.index(maxval) + 1 # return index of the maxmum value in cv file, first value starts line 1, so +1
    minpos = cv.index(minval) + 1
    
    maxtime = sheet.cell_value(maxpos,0) # get the value in column 0 at maxpos row [maxpos,0]
    realtime = xlrd.xldate_as_tuple(maxtime,0) # convert 41499.7083333 to (2013, 8, 13, 17, 0, 0)
    mintime = sheet.cell_value(minpos,0)
    realmintime = xlrd.xldate_as_tuple(mintime,0)
    
    data = {'maxtime': realtime, 'maxvalue':maxval,'mintime':realmintime,'minvalue':minval,'avgcoast':sum(cv)/float(len(cv))}
    
#    data = {
#            'maxtime': (0, 0, 0, 0, 0, 0),
#            'maxvalue': 0,
#            'mintime': (0, 0, 0, 0, 0, 0),
#            'minvalue': 0,
#            'avgcoast': 0
#    }
    return data


def test():
    open_zip(datafile0) # unzip the zip file "datafile0"
    data = parse_file(datafile) # load the xls file in the zip file
    
#    import pprint
#    pprint.pprint(data) # not necessary, used to print the file in a more nice structured way

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
