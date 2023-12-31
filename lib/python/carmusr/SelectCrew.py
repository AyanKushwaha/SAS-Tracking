#

#
"""
Functions to select crew from etables (directly or generated by reports)
"""

import os
import Cui
import String
import Errlog
import carmstd.area as a
from carmstd.report import Report
from carmstd.parameters import parameter

# Location where crew select etables are stored
etabDir = os.path.join("$CARMDATA", "tmp")

def fromEtab(etabName, area=Cui.CuiWhichArea, mode=Cui.CrewMode, subSelect=False):
   """
   Selects crew from an etable in $CARMDATA/tmp if the etable exists.
   """
   if os.path.isfile(os.path.expandvars(os.path.join(etabDir, etabName))):
      parameter["studio_select.csl_string_1"] = etabName
      Cui.CuiCrcRefreshEtabs(etabDir, Cui.CUI_REFRESH_ETAB_FORCE)
      if subSelect:
         selectFilter="fast_crew_group_subselect"
      else:
         selectFilter="fast_crew_group"
      try:
         Cui.CuiDisplayFilteredObjects(Cui.gpc_info, area, mode, selectFilter)
      except Exception, e:
         Errlog.log("%s" % e)
         Errlog.set_user_message("Select filter failed (etable: %s)" % etabName)

def fromAnyEtab(etabPath, subSelect=False):
   area = Cui.CuiWhichArea
   mode = a.getAreaMode(area)
   etab = "crew_selection_" + os.path.expandvars("$USER") + "_tmp"
   os.system("cp " + etabPath + " " + etabDir + "/" + etab)
   fromEtab(etab, area, mode, subSelect)

def fromPersonalEtab(etabNumber, subSelect=False):
   area = Cui.CuiWhichArea
   # mode = a.getAreaMode(area)
   mode = Cui.CrewMode
   etab = "crew_selection_" + os.path.expandvars("$USER") + "_%d" % etabNumber
   fromEtab(etab, area, mode, subSelect)

def toPersonalEtab(etabNumber):
   etab = "crew_selection_" + os.path.expandvars("$USER") + "_%d" % etabNumber
   if not os.path.exists(os.path.expandvars(etabDir)):
      os.mkdir(os.path.expandvars(etabDir))
   etabPath=os.path.join(etabDir, etab)
   try:
      Report("fastSelectGroupEtab_create.output", Cui.CuiWhichArea, "window").save(etabPath)
   except Exception, e:
      Errlog.log("%s" % e)
      Errlog.set_user_message("Failed to create select filter")
         
def fromReport(report, area=Cui.CuiWhichArea):
   """
   Creates an etab with crewids and pass it on to a select filter.
   The report is expected to be in crg/hidden or have a path like:
   'include/<report>'
   """
   etabName =  report+".etab"
   etabPath=os.path.join(etabDir, etabName)
   try:
      Report(report).save(etabPath)
      fromEtab(etabName, area)
   except Exception, e:
      Errlog.log("%s" % e)
      Errlog.set_user_message("Select filter failed (report: %s)" % report)

if __name__=='__main__':
   SelectCrew.fromReport(sys.argv[1])
