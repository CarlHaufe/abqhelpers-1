# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-15.50.37 167380
# Run by ac134018 on Thu Jul 20 12:59:54 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=163.040618896484, 
    height=173.214813232422)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('3_P_Real-Scale_FGC_Beam.py', __main__.__dict__)
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\helpers/filemanager.py:10: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import os
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\helpers/filemanager.py:11: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import sys
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\helpers/filemanager.py:12: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import shutil
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_parts.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_parts.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_parts.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from driverUtils import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:20: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from caeModules import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:22: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:23: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import pickle
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_property.py:24: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import numpy as np
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_assembly.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_assembly.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_assembly.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_interaction.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_interaction.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_interaction.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_interaction.py:20: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import pickle
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_interaction.py:21: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import numpy as np
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_step.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_step.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_mesh.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_mesh.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_mesh.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_job.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\src/abq_job.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: The model "3_P_Real-Scale_FGC_Beam" has been created.
#: M:/10_FORSCHUNG/02_IntCDC\DigiDesiTool/NumericalExperimentLCRLBeams/abqhelpers-1\helpers/filemanager.py:80: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import os
#* TypeError: String Expected as dictionary Key
#* File "3_P_Real-Scale_FGC_Beam.py", line 195, in <module>
#*     mdb.models[model].Material(name='C30/37')
p = mdb.models['3_P_Real-Scale_FGC_Beam'].parts['concrete_beam-0']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
