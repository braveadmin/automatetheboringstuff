#! python3

# Date Detection

import re

datesPool = "29/02/1992, 29/02/1583, 31/04/2015, 14/09/2021, 21/12/1994, 00/12/1994, 23/13/1997, 13/12/1000, 11/11/999"

specialMonths = ('04','06','09','11')

dateRegex = re.compile(r'(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([12][0-9]{3})')

matches = []

for dates in dateRegex.findall(datesPool):

    valid = True

    # store strings into dict keys

    date = {'day':0, 'month':1, 'year':2}
    
    for i, j in date.items():

        date[i] = dates[j]

    if date['day'] in ['29','30','31']:

        if date['day'] == '29' and date['month'] == '02': # detect leap years

            if (int(date['year']) % 4 == 0) and (int(date['year']) % 100 != 0) or \
            (int(date['year']) % 400 == 0) and (int(date['year']) % 100 != 0):

                valid = True

            else:

                valid = False

        if date['day'] == '31' and date['month'] != '02': # detect invalid dates in April, June, September and November

            if date['month'] not in specialMonths:
            
                valid = True

            else:

                valid = False
 
        if date['day'] == '30' and date['month'] != '02':

            if date['month'] in specialMonths:

                valid = True
            
            else:

                valid = False

    print(valid)

    if valid:

        matches.append(date)


#print matches well-formated 

for i in range(len(matches)):

    print('Dates found: ' + matches[i]['day'] + '/' + matches[i]['month'] + '/' + matches[i]['year'])