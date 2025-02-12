# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by ac134018 on Wed Mar  1 19:22:22 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=193.782287597656, 
    height=166.36296081543)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('Demo_Slab.py', __main__.__dict__)
#: C:/temp\GitHub_ch/abqhelpers/helpers/filemanager.py:10: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/helpers/filemanager.py:11: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import sys
#: C:/temp\GitHub_ch/abqhelpers/helpers/filemanager.py:12: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import shutil
#: C:/temp\GitHub_ch/abqhelpers/src/abq_parts.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_parts.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_parts.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from driverUtils import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:20: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from caeModules import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:22: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:23: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import pickle
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:24: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import numpy as np
#: C:/temp\GitHub_ch/abqhelpers/src/abq_assembly.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_assembly.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_assembly.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_interaction.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_interaction.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_interaction.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_interaction.py:20: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import pickle
#: C:/temp\GitHub_ch/abqhelpers/src/abq_interaction.py:21: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import numpy as np
#: C:/temp\GitHub_ch/abqhelpers/src/abq_step.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_step.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_mesh.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_mesh.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_mesh.py:19: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_job.py:17: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqus import *
#: C:/temp\GitHub_ch/abqhelpers/src/abq_job.py:18: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from abaqusConstants import *
#: The model "Demo_Slab" has been created.
#: C:/temp\GitHub_ch/abqhelpers/helpers/filemanager.py:80: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:46: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from material import createMaterialFromDataString
#: Material 'concrete_cdp_C50_60' has been copied to the current model.
#: Material 'support_stiff' has been copied to the current model.
#: Material 'reinforcement_b500' has been copied to the current model.
p = mdb.models['Demo_Slab'].parts['concrete-dummy-plates']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
