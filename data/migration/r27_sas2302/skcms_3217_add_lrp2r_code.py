"""
SKCMS-3217 A2LR: Add LRP2R to table activity_set.
Release: SAS2006
"""


import adhoc.fixrunner as fixrunner
from AbsTime import AbsTime

__version__ = '2023-02-09a'


@fixrunner.once
@fixrunner.run
def fixit(dc, *a, **k):
    valid_from = int(AbsTime('01Jan1986'))
    valid_to = int(AbsTime('31Dec2035'))

    ops = list()
    ops.append(fixrunner.createOp('activity_set', 'N', {'id': 'LRP2R', 'grp': 'COD', 'si': 'Added in SKCMS-3217'}))
    ops.append(fixrunner.createOp('activity_set_period', 'N', {'id': 'LRP2R',
                                                               'validfrom': valid_from,
                                                               'validto': valid_to,
                                                               'si': 'Added in SKCMS-3217'}))

    return ops


fixit.program = 'skcms_3217_add_lrp2r_code.py (%s)' % __version__
if __name__ == '__main__':
    fixit()