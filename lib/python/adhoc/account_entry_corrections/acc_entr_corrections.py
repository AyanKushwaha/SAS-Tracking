import csv
from datetime import datetime

import adhoc.fixrunner as fixrunner
from AbsTime import AbsTime
from carmensystems.basics.uuid import uuid
import utils.Names

'''
Usage:
    1. Read from csv file (reference SKSD-10241)
    2. Change open statements to target correct files, change dates
    3. Update __version__
    4. Run using
        $ python va_va1_corrections.py
'''
 
corrEntries = []
def main():
    create_corrections()
    fixit()
 
def create_corrections():
    with open('./account_entry_corrections.csv') as csvFile:
        data = csv.reader(csvFile, delimiter=',', quotechar='|')
        for row in data:
            tmp_date = datetime(int(row[1][6:10]), int(row[1][3:5]), int(row[1][0:2])).strftime("%d%b%Y %H:%M:%S:%f")
            print(tmp_date)
            corrEntries.append(dict({'id': row[0],'tim': tmp_date,'account': row[2],'source': row[3],'amount': row[4],'man': row[5],'si': row[6],'published': row[7], 'rate': row[8],'reasoncode': row[9]}))         
    

@fixrunner.once
@fixrunner.run
def fixit(dc, *a, **k):
    date = str(datetime.now()).replace('-', '')    
    time = AbsTime(date[:14])
    print(time)
 
    ops = list()
    for corrEntry in corrEntries:
        ops.append(fixrunner.createOp('account_entry', 'N', {'id': uuid.makeUUID64(),
                                                            'crew': corrEntry['id'],
                                                            'tim': int(AbsTime(corrEntry['tim'][:15])),
                                                            'account': corrEntry['account'],
                                                            'source': corrEntry['source'],
                                                            'amount': int(corrEntry['amount']),
                                                            'man': 'Y',
							                                'si': corrEntry['si'],
                                                            'published': 'Y',
                                                            'rate': int(corrEntry['rate']),
                                                            'reasoncode': corrEntry['reasoncode'],
                                                            'entrytime': int(time),
                                                            'username': utils.Names.username()}))
    return ops
 
__version__ = '2022-09-07b'
fixit.program = 'acc_entr_corrections.py (%s)' % __version__
 
main()
