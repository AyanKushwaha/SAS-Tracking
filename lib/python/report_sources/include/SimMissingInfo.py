"""
 $Header$
 
 PGT Missing Info

 
 
 Created:    August 2007
 By:         Anna Olsson, Jeppesen

"""

# imports ================================================================{{{1
import carmensystems.rave.api as R
from carmensystems.publisher.api import *
from report_sources.include.SASReport import SASReport
from AbsDate import AbsDate
from RelTime import RelTime
import Cui

# constants =============================================================={{{1
#CONTEXT = 'default_context'
CONTEXT = 'sp_crew'
TITLE = 'Sim Missing Info'

class SimMissingInfo(SASReport):
    
    def create(self, report_type):
        # Basic setup
        SASReport.create(self, TITLE, orientation=PORTRAIT, usePlanningPeriod=True)

        # Get the rosters that are missing PC
        pc_expr = R.foreach(
            R.iter('iterators.roster_set', 
                    where='report_ccr.%must_have_pc_any% and planning_area.%crew_is_in_planning_area%', 
                    sort_by='crew.%id%'),
            'report_common.crew_name',
            'report_common.employee_number',
            'report_ccr.%pc_exp_date_show%')
        
        # Get the rosters that are missing OPC
        opc_expr = R.foreach(
            R.iter('iterators.roster_set', 
                    where='report_ccr.%must_have_opc_any% and planning_area.%crew_is_in_planning_area%', 
                    sort_by='crew.%id%'),
            'report_common.crew_name',
            'report_common.employee_number',
            'report_ccr.%opc_exp_date_show%')
        
              
        # Evaluate rave expression
        pc_rosters, = R.eval(CONTEXT, pc_expr)
        opc_rosters, = R.eval(CONTEXT, opc_expr)

        
        ##Print things in report
        
        # Table header
        self.add(self.getTableHeader(('Crew Id','Crew Name','Type','Expiry date','Notes')))
        
       
        crews = 0
        # Print RAVE PC data in table      
        for (ix, crew_string,emp_nr,exp_date) in pc_rosters:
            self.add(Row(Column(emp_nr),Column(crew_string),Column("PC"),Column(exp_date)))
            crews += 1
            self.page0()
            
        # Print RAVE OPC data in table      
        for (ix, crew_string,emp_nr,exp_date) in opc_rosters:
            self.add(Row(Column(emp_nr),Column(crew_string),Column("OPC"),Column(exp_date)))
            crews += 1
            self.page0()

            
        print "Number of crew fetched:", crews

# End of file
