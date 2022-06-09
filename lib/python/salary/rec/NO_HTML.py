
# -*- coding: latin-1 -*-
# [acosta:06/313@16:52] Redesign, added coding

"""
Norwegian salary system.
HTML format.
"""

from salary.fmt import HTMLFormatter

class NO_HTML(HTMLFormatter):
    class Headings:
        admcode   = 'Slag'
        amount    = 'Bel�p'
        extartid  = 'Slag'
        extperkey = 'Extperkey'
        extsys    = 'L�nneskontor'
        firstdate = 'F�rste dato'
        lastdate  = 'Siste dato'
        note      = 'Kommentar'
        runid     = 'L�penummer'
        starttime = 'Kj�relse dato'
        selector  = 'Utvalg'
        total     = 'Samlet'

# EOF
