
# -*- coding: latin-1 -*-
# [acosta:06/313@15:05] Redesign, added coding.

"""
Danish salary system.
HTML format.
"""

from salary.fmt import HTMLFormatter

class DK_HTML(HTMLFormatter):
    class Headings:
        admcode   = 'Slag'
        amount    = 'Bel�b'
        extartid  = 'Slag'
        extperkey = 'Extperkey'
        extsys    = 'L�nkontor'
        firstdate = 'F�rste dato'
        lastdate  = 'Sidste dato'
        note      = 'Bem�rkning'
        runid     = 'L�benummer'
        starttime = 'Dato f�r k�ring'
        selector  = 'Udvalg'
        total     = 'Samlet'

# EOF
