'''
Sensitivity Index Distribution Report
'''

import carmusr.calibration.report_si as si_report


class Report(si_report.SensitivityIndexDistributionReport):
    pass


if __name__ == "__main__":
    from carmusr.calibration.mappings import report_generation as rg
    from carmusr.calibration.developer_tools import reload_calibration_report_modules

    reload_calibration_report_modules.doit()
    rg.display_prt_report(fm="HTML", area=0, scope="object")
