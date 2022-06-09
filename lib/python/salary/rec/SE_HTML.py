
# -*- coding: latin-1 -*-
# [acosta:06/313@16:52] Redesign, added coding

"""
Swedish salary system.
HTML format.
"""

from salary.fmt import HTMLFormatter

class SE_HTML(HTMLFormatter):
    class Headings:
        admcode   = 'K�rningstyp'
        amount    = 'Belopp'
        extartid  = 'Slag'
        extperkey = 'Extperkey'
        extsys    = 'L�nekontor'
        firstdate = 'F�rsta datum'
        lastdate  = 'Sista datum'
        note      = 'Kommentar'
        runid     = 'L�pnummer'
        starttime = 'K�rdatum'
        selector  = 'Urval'
        total     = 'Totalsumma'

# EOF
