# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_28-20.11.55 183150
# Run by ac134018 on Wed Mar  1 10:47:53 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=176.490097045898, 
    height=155.674072265625)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('4_P_cantilever_Concrete_Beam.py', __main__.__dict__)
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
#: The model "Concrete_beam_4_cantilever_B" has been created.
#: C:/temp\GitHub_ch/abqhelpers/helpers/filemanager.py:80: RuntimeWarning: Parent module 'helpers' not found while handling absolute import
#:   import os
#: C:/temp\GitHub_ch/abqhelpers/src/abq_property.py:46: RuntimeWarning: Parent module 'sec' not found while handling absolute import
#:   from material import createMaterialFromDataString
#: Material 'concrete_cdp_C50_60' has been copied to the current model.
#: Material 'support_stiff' has been copied to the current model.
#: Material 'reinforcement_b500' has been copied to the current model.
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
#: Partitioning failed for instance: concrete-dummy-plates-1
p = mdb.models['Concrete_beam_4_cantilever_B'].parts['concrete-dummy-plates']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2101.5, 
    farPlane=3269.38, cameraPosition=(-925.993, -1895.84, 1137.22), 
    cameraUpVector=(0.268381, 0.284791, 0.920253))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2101.51, 
    farPlane=3269.38, cameraPosition=(-1166.42, -1801.04, 963.032), 
    cameraTarget=(359.577, 144.803, -84.1879))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2099.22, 
    farPlane=3361.79, cameraPosition=(-1416.72, -1729.57, 652.775), 
    cameraUpVector=(0.184817, 0.202931, 0.961593), cameraTarget=(359.577, 
    144.803, -84.1879))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2164.56, 
    farPlane=3296.45, width=641.183, height=225.337, cameraPosition=(-1445.75, 
    -1678.23, 713.383), cameraTarget=(330.548, 196.143, -23.5799))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=ON)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    position=732.732)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    showModelAboveCut=True, showModelBelowCut=False)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    showModelAboveCut=False, showModelBelowCut=True)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    showModelOnCut=False)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    showModelAboveCut=True, showModelBelowCut=False)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    position=164.564)
session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=ON)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    seeds=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=HIDDEN)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=SHADED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2192.61, 
    farPlane=3268.39, width=345.351, height=121.37, cameraPosition=(-1455.92, 
    -1669.48, 711.128), cameraTarget=(320.375, 204.897, -25.8345))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    activeCutName='X-Plane', viewCut=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2175.76, 
    farPlane=3285.24, width=591.941, height=208.032, cameraPosition=(-1463.05, 
    -1653.1, 735.581), cameraTarget=(313.244, 221.269, -1.38221))
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2514.29, 
    farPlane=2856.59, width=1224.67, height=430.397, cameraPosition=(560.93, 
    -2635.44, 72.9869), cameraTarget=(560.93, 50, 72.9869))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(597.112, 
    -2635.44, 90.2657), cameraTarget=(597.112, 50, 90.2657))
#: 
#: Part instance:  concrete-dummy-plates-1,  Number of regions verified:  64
#:  Number of Hex elements verified:  76608
#:    Aspect ratio > 5:  6046 (7.89213%)
#:    Average aspect ratio:  2.71,  Worst aspect ratio:  14.10
#:   Number of elements :  76608,   Analysis errors:  0 (0%),  Analysis warnings:  2495 (3.25684%)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(461.794, 
    -2635.44, 70.6395), cameraTarget=(461.794, 50, 70.6395))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2085.36, 
    farPlane=3497.96, cameraPosition=(-1729, -1211.67, 976.296), 
    cameraUpVector=(0.157269, 0.380943, 0.911125))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1729, 
    -1211.67, 976.296), cameraUpVector=(0.315082, 0.127929, 0.940403), 
    cameraTarget=(461.794, 50, 70.6395))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1729, 
    -1211.67, 976.296), cameraUpVector=(0.287646, 0.176268, 0.941376), 
    cameraTarget=(461.794, 50, 70.6395))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2167.95, 
    farPlane=3415.37, width=245.1, height=88.5288, cameraPosition=(-1846.97, 
    -1090.82, 859.292), cameraTarget=(343.826, 170.854, -46.365))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1846.97, 
    -1090.82, 859.292), cameraUpVector=(0.292584, 0.167723, 0.941416), 
    cameraTarget=(343.826, 170.854, -46.3649))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2169.3, 
    farPlane=3414.03, cameraPosition=(-1865.94, -1082.68, 824.742), 
    cameraTarget=(324.858, 178.99, -80.9146))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2165.88, 
    farPlane=3417.45, width=303.15, height=109.496, cameraPosition=(-1862.91, 
    -1087.01, 826.042), cameraTarget=(327.89, 174.658, -79.6143))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2204.47, 
    farPlane=3245.46, cameraPosition=(-1372.23, -1747.5, 728.262), 
    cameraUpVector=(0.204904, 0.222169, 0.953234), cameraTarget=(346.56, 
    149.527, -83.3347))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1455.34, 
    -1655.45, 767.406), cameraTarget=(263.448, 241.576, -44.1907))
#: 
#: Part instance:  concrete-dummy-plates-1,  Number of regions verified:  64
#:  Number of Hex elements verified:  76608
#:    Aspect ratio > 4:  12244 (15.9827%)
#:    Average aspect ratio:  2.71,  Worst aspect ratio:  14.10
#:   Number of elements :  76608,   Analysis errors:  0 (0%),  Analysis warnings:  2495 (3.25684%)
#: 
#: Part instance:  concrete-dummy-plates-1,  Number of regions verified:  64
#:  Number of Hex elements verified:  76608
#:    Aspect ratio > 4:  12244 (15.9827%)
#:    Average aspect ratio:  2.71,  Worst aspect ratio:  14.10
#:   Number of elements :  76608,   Analysis errors:  0 (0%),  Analysis warnings:  2495 (3.25684%)
a = mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly
e1 = a.instances['concrete-dummy-plates-1'].elements
elements1 = e1.getSequenceFromMask(mask=(
    '[#70381e0 #c #0 #381c0000 #c070 #0 #c0000000', 
    ' #c070381 #0:2 #10000000 #0 #f00800 #800e00f #0:2', 
    ' #e00f00f #80 #0 #f00f000 #e0 #0:3 #e1800000', 
    ' #f #8000000 #e0fff386 #1c0e03c1 #804038 #f80c0201 #f', 
    ' #0 #ffe1800 #18180c1e #80402010 #fe020100 #f #30200000', 
    ' #40fe7c38 #870c1830 #40fffde3 #1c383060 #c03fbf1e #3803c03 #20', 
    ' #0 #3c03c00 #38 #0 #3c00000 #3803c #0', 
    ' #4000 #30000000 #c00000 #1c0e0780 #30 #0 #e0700000', 
    ' #301c0 #0:2 #301c0e07 #0 #20000000 #1f0f83c0 #8040203', 
    ' #80402010 #c03ff80 #20 #1000000 #7c0700c #7ff #0:2', 
    ' #fff01000 #c0200803 #380c0300 #1fffe0f0 #c030040 #f01c030 #7fff07c', 
    ' #e00e07e #200200a0 #ff300200 #2002007 #20020020 #300200 #7003803', 
    ' #40060070 #c00400 #3c01c00c #3c0007c0 #3803c0 #2 #0', 
    ' #803c03c0 #2003 #0 #c03c0000 #3803 #0 #78000000', 
    ' #301c0e0 #0:2 #1c0e0700 #30 #0 #e0700000 #301c0', 
    ' #0:2 #40000 #0 #e07e07e #200200e0 #200200 #30207fe3', 
    ' #8f0e0c18 #60c1fdf #bc70c183 #1f81fff #1c01c01f #100100 #1ff003', 
    ' #0 #80000000 #fe1 #0 #fff38608 #0:2 #fe180', 
    ' #0 #7c383020 #381e0fe #c07 #0 #1c000000 #c07038', 
    ' #0:2 #70381c0 #c #0 #8 #30 #f00c0000', 
    ' #e00f00 #8 #0 #f00f00 #e #0 #f00000', 
    ' #e00f #0 #1000 #2 #0 #f0080000 #403ffc0', 
    ' #0 #80000000 #fe0e0300 #7e1e0ff #40381c0e #2010080 #200ff80c', 
    ' #0:2 #f008000 #c3e0fffc #10080c7 #10080402 #ffe020 #803', 
    ' #40000000 #f01c0300 #200ffc1 #c03008 #f83c0e03 #c01007ff #700c0300', 
    ' #fc1f03c0 #80300f #0 #c0300400 #1ffc1f01 #804020 #781c0601', 
    ' #c07fe7f0 #7007c07 #40050078 #ffc00c00 #20100804 #7018040 #3ff9fc1e', 
    ' #80080180 #800800 #e00c00c #801f80f0 #1001001 #10010010 #700300', 
    ' #801003 #8008008 #c0080080 #e00c00 #c #381e024 #381c0e07', 
    ' #1c0e070 #c0603 #0:6 #c3e0f008 #10381c0 #10080402 #ffe020', 
    ' #30000 #c070381e #0:2 #381c000 #c07 #0 #1c000000', 
    ' #c07038 #0 #800000 #70381e0 #c #0 #381c0000', 
    ' #c070 #0 #c0000000 #c070381 #0 #8000000 #f00f000', 
    ' #800e0 #0 #f000000 #e00f0 #0:2 #e00f00f0 #0', 
    ' #10000000 #0 #c00 #f81f0030 #80380381 #800802 #1ffcc008', 
    ' #c030040 #f01c030 #803ff07c #300c0200 #f0380c0 #1f01fffe #e01e01e0', 
    ' #1001601 #3ff0030 #20 #0 #800000 #403ffc0f #0:2', 
    ' #e0e03008 #200fff #0:2 #fc0f0080 #80300f #0 #c0300400', 
    ' #1ffc1f01 #c030040 #f01c030 #7ff07c #4006007 #c00c0040 #3c01c00', 
    ' #f878007c #e070381 #80402010 #7fe0300 #40040060 #400400 #1c00c004', 
    ' #200400c0 #200200 #2002002 #38030020 #700700 #4004006 #c00c00c0', 
    ' #7c03c01 #10080400 #c0c04020 #fffff3c1 #ff #fff #1ff0', 
    ' #400 #0:5 #20000000 #f00f00 #f00f00f #e00e00f0 #800e00', 
    ' #0:5 #1000000 #780780f0 #80680780 #800800 #ffcc #c0000', 
    ' #1003000 #c03004 #c0f01c03 #7007ff07 #400600 #c00c004 #c03c01c0', 
    ' #1f878007 #e07038 #8040201 #403fe030 #2010080 #3c1c0c04 #1c01ffff', 
    ' #100180 #3003001 #f00f0070 #80080101 #800800 #8008008 #c00e00c0', 
    ' #1001801 #10010010 #300300 #ff003007 #f000000f #ff #1ff', 
    ' #40 #0:5 #2000000 #f00f00f0 #f00f00 #e00e00f #800e0', 
    ' #0:5 #100000 #780780f #8068078 #c0080080 #ffc #30', 
    ' #c0000 #c00000 #30000 #c070381e #0:2 #381c000 #c07', 
    ' #0 #1c000000 #c07038 #0 #800000 #f00f00 #800e', 
    ' #0 #f00000 #e00f #0:2 #e00f00f #0 #1000000', 
    ' #2000 #0 #80000000 #1ffc0700 #100180 #1001001 #70030010', 
    ' #c0100300 #1001801 #30030010 #f00700 #2010001f #1008040 #ffcf0703', 
    ' #100807f #70180402 #ff9fc1e0 #801803 #8008008 #e00c00c0 #e0f80f00', 
    ' #1c0e07e1 #804038 #f80c0201 #1e01f01f #601e01e0 #3001001 #3ff0', 
    ' #f00c0000 #e00f00 #8 #0 #f00f00 #e #0', 
    ' #f00000 #e00f #0 #e0001000 #c070381 #0:2 #70381c00', 
    ' #c0 #0 #81c00000 #c0703 #0 #80000 #300000', 
    ' #c7c3e0f #40201008 #2010080 #80300ffe #0 #30040000 #fc1f01c0', 
    ' #1f #0:2 #1fffc040 #804020 #781c0601 #403fe7f0 #2010080', 
    ' #3c1c0c04 #1c01ffff #100180 #3003001 #f00f0070 #80080101 #800800', 
    ' #8008008 #c00e00c0 #e07e1e0 #8040381c #c020100 #f00ff8 #800e00f', 
    ' #0:2 #e00f00f #0:2 #f00f000 #e0 #0 #81e00010', 
    ' #c0703 #0:2 #c070381c #0:2 #381c000 #c07 #0', 
    ' #800 #3000 #1c000000 #e01e01f0 #1601e01 #f0030010 #802003f', 
    ' #300c030 #fff83c0e #c01007 #c0700c03 #fffc1f03 #80381f81 #802803', 
    ' #cc008008 #801c01ff #1001001 #70030030 #1f00f00 #800801 #8008008', 
    ' #c00c0080 #1c00e00 #10010018 #100100 #7003003 #18030030 #80080080', 
    ' #c00800 #f00e00c #f8 #2000000 #1fe7c383 #380c020 #ffdfe1f', 
    ' #e00fc0f8 #800e00 #f8018008 #40040007 #400400 #c006006 #80080080', 
    ' #1801800 #4000008 #60060040 #c0780700 #c060100f #feff0f81 #3', 
    ' #40000008 #c03c0000 #2003803 #0 #c0000000 #3803c03 #20', 
    ' #0 #3c03c00 #38 #0 #e0780000 #301c0 #0:2', 
    ' #301c0e07 #0:2 #c0e07800 #301 #0 #7e040000 #7007c0', 
    ' #c004007 #7fc00c0 #1c0e078 #3 #0 #e070000 #301c', 
    ' #0 #70000000 #301c0e0 #0 #2000000 #3c03c00 #20038', 
    ' #0 #3c00000 #3803c #0:2 #3803c03c #0 #4000000', 
    ' #0 #300 #7c0400c #78078078 #400580 #ffc00c #c02008', 
    ' #f0380c03 #401fffe0 #300c0300 #7c0f01c0 #7e07fff0 #a00e00e0 #200200', 
    ' #fff3002 #20020060 #200200 #3803003 #6007e03c #400400 #c004004', 
    ' #c01c00c0 #200400 #2002002 #30020020 #380300 #6007007 #c0040040', 
    ' #1c00c00 #7c03c #40000 #0 #3c03c02 #20038 #0', 
    ' #3c00000 #2003803c #0:2 #3803c03c #0:2 #c0e07800 #301', 
    ' #0 #7000000 #301c0e #0:2 #1c0e070 #3 #0:3', 
    ' #7f860000 #400400 #c00c004 #783c0040 #40206030 #2010080 #3ff80804', 
    ' #0 #e0c08000 #e07ff9f0 #e00e07 #2002002 #7fe30020 #c183020', 
    ' #1fdf8f0e #c1830608 #fffbc70 #0 #86080000 #1801fff3 #30000180', 
    ' #20000 #400700 #6002000 #60100008 #78000400 #301c0e0 #0:2', 
    ' #1c0e0700 #30 #0 #e0700000 #301c0 #0:2 #3803c03c', 
    ' #200 #0 #3c03c000 #200380 #0 #3c000000 #3803c0', 
    ' #0:3 #4000002 #e07e07c0 #200e00 #2002002 #207fe30 #f0e0c183', 
    ' #60c1fdf8 #c70c1830 #1f81fffb #c01c01f0 #1001001 #1ff0030 #c0080080', 
    ' #e00c00 #1001f80f #100100 #3003003 #8008000 #c0080080 #1c00c00', 
    ' #30030010 #f00700 #381e001f #c070 #0 #c0000000 #c070381', 
    ' #0:2 #70381c00 #c0 #0 #f000000 #800e00f0 #0:2', 
    ' #e00f00f0 #800 #0 #f00f0000 #e00 #0:2 #800000', 
    ' #10010000 #c01f01f8 #1001c01 #f0030010 #1830401f #fde3870c #306040ff', 
    ' #bf1e1c38 #e07e07ff #200e00 #2002002 #2003fe30 #300200 #3c03803', 
    ' #4004007e #c00400 #400c #20020020 #300200 #4007003 #c00c00c0', 
    ' #7c03c01 #80000c00 #1800001 #300000 #c00000c0 #2c00002 #c000', 
    ' #c00000c0 #1c00000 #8008008 #100180 #8060100 #18008010 #c02000', 
    ' #1801800 #18 #1c0003 #800001 #10018 #f0080080 #e00f00', 
    ' #8 #0 #f00f00 #800e #0 #f00000 #e00f', 
    ' #0:2 #8000000 #100000 #70381e0 #c #0 #381c0000', 
    ' #c070 #0 #c0000000 #c070381 #0:2 #80c1e0f0 #2010081', 
    ' #20100804 #ffe0 #0 #e7c38302 #f #0 #fec000', 
    ' #8008008 #c00c0080 #1001c00 #70030030 #3f00f00 #6020100 #ffffdf0e', 
    ' #1c060100 #ffeff0f8 #e07e07 #200200e #30020020 #3fe #4004007', 
    ' #20020060 #80600 #4006010 #1804000 #10 #0 #e7c38302', 
    ' #80c0201f #fdfe1f03 #fc0fc0f #800e00e0 #1800800 #10087f8 #f0f81c06', 
    ' #2003fef #30030020 #e03c0380 #4004007 #c00c0040 #c00 #2002002', 
    ' #30030020 #f078200 #e07038 #8040201 #3fe070 #80800000 #381e0e07', 
    ' #81c0e070 #180c0703 #30 #0:6 #80000000 #e00037fc #ff00003f', 
    ' #1f80001 #0:7 #c000 #c00000c0 #7000000 #40 #2c00000c', 
    ' #2c0000 #c00 #20000000 #fe7c3830 #380c0201 #ffdfe1f0 #f00f80', 
    ' #800e00e #80180180 #6010087f #ff0f81c0 #2003fe #3003002 #7e03c038', 
    ' #400400 #c00c004 #20000040 #200200 #3003002 #3c03c020 #c03c03c0', 
    ' #3803c03 #20038038 #0:6 #3ffc00 #3ffc000 #7fc0000 #1800000', 
    ' #0:6 #7e04000 #7007007e #400400 #7fc00c #20000000 #0', 
    ' #1c0e0782 #30 #0 #e0700000 #301c0 #0:2 #301c0e07', 
    ' #0 #20000000 #40000000 #0 #3c02000 #2003803c #0:2', 
    ' #3803c03c #200 #0 #3c03c000 #380 #0:3 #87000000', 
    ' #3f #20000000 #83ffce18 #70380f07 #20100e0 #e0300804 #4004007f', 
    ' #c00400 #400c #30020020 #c0380300 #1807e03 #f87c0e03 #40201ff7', 
    ' #f3e1c0c0 #1f81fff #1c01c01f #300100 #1ff003 #600003 #6000', 
    ' #70000c00 #400400 #2004004 #60060 #1001c000 #20180000 #200', 
    ' #2003001 #c02000 #400400c #18008 #30000180 #30000080 #b00000', 
    ' #3000 #c00030 #e078300 #301c #0 #70000000 #301c0e0', 
    ' #0:2 #1c0e0700 #30 #0 #3c00000 #2003803c #0:2', 
    ' #3803c03c #200 #0 #3c03c000 #380 #0:2 #200000', 
    ' #4004000 #7007c07e #400700 #fc00c004 #60c1007 #ff78e1c3 #c18103f', 
    ' #efc7870e #381f81ff #80080380 #800800 #800ff8c #c00c0080 #80f00e00', 
    ' #1001001f #300100 #1003 #8008008 #c00c0080 #1001c00 #70030030', 
    ' #1f00f00 #1800001 #18000 #7000002 #30000 #70000c #4006002', 
    ' #0 #200 #e0780004 #301c0 #0:2 #301c0e07 #0:2', 
    ' #c0e07000 #301 #0 #3c000000 #3803c0 #2 #0', 
    ' #803c03c0 #2003 #0 #c03c0000 #3803 #0:3 #60000000', 
    ' #4007f8 #c004004 #c00c00c0 #6030783 #10080406 #80804020 #3ff', 
    ' #8000000 #7f9f0e0c #c00400 #3c01c00c #4000fc0 #7c381808 #403ffff', 
    ' #c3e07018 #f81fffbf #80380381 #800800 #ff8c008 #0 #38302000', 
    ' #201fe7c #e1f0380c #f80ffdf #e00e00fc #800800 #7f8018 #40040040', 
    ' #600400 #800c006 #80080080 #801801 #4004000 #70060060 #fc0780', 
    ' #f81c0601 #7fffeff0 #3fe0003 #1ff000 #1f80 #0:7 #60000000', 
    ' #7e07e0 #4007007 #c00c0040 #3ffc7f #3ffc000 #7fc0000 #1800000', 
    ' #0:7 #48000 #18010018 #80080 #c00030 #10018008 #80080000', 
    ' #1001 #201c000 #800c00 #100001 #2003 #6010010 #60060040', 
    ' #200600 #4007000 #60000 #18 #800c0003 #1001800 #803000', 
    ' #0 #c0300400 #1ffc1f01 #804020 #781c0601 #c07fe7f0 #7807807', 
    ' #40058078 #ffc00c00 #2002004 #20020020 #300200 #7003803 #40040060', 
    ' #400400 #1c00c00c #600c00c0 #200200 #3002002 #3c038030 #100807e0', 
    ' #1804020 #f9fc1e07 #1f01f81f #601e01c0 #3001001 #fff3ff0 #fff00000', 
    ' #ff000000 #40000001 #0:6 #f0020000 #f00f00 #f00f00f #e00e00e0', 
    ' #800 #0:5 #1000 #2400000 #24000000 #c0300401 #f01c0300', 
    ' #7ff07c0 #40060070 #c00400 #3c01c00c #878007c0 #e070381f #4020100', 
    ' #3fe03008 #1008040 #1c0c0402 #1ffff3c #1001801c #300100 #f007003', 
    ' #80101f0 #80080080 #800800 #e00c008 #1801c0 #1001001 #30030010', 
    ' #300700 #e07e1e0 #8040381c #c020100 #9ffff8 #ff80 #e00007fc', 
    ' #7 #0:6 #2000 #fff90000 #ff000000 #f000000f #1f', 
    ' #4 #0:5 #200000 #c000000 #8030 #0 #1c03004', 
    ' #201ffc1f #1008040 #f0781c06 #7c07fe7 #7807007c #400500 #4ffc00c', 
    ' #40201008 #1e070180 #803ff9fc #800801 #c008008 #f00e00c0 #1801f80', 
    ' #10010010 #100100 #3007003 #8008010 #80080080 #c00800 #c00e00c', 
    ' #24000000 #70381e0 #70381c0e #301c0e0 #c06 #0:5 #8000000', 
    ' #c0c3e0f0 #2010381 #20100804 #ffe0 #1e000300 #c07038 #0:2', 
    ' #70381c0 #c #0 #381c0000 #c070 #0 #e0008000', 
    ' #c070381 #0:2 #70381c00 #c0 #0 #81c00000 #c0703', 
    ' #0 #80000 #e00f00f0 #800 #0 #f00f0000 #e00', 
    ' #0 #f0000000 #e00f00 #0 #100000 #0 #3000000c', 
    ' #81f81f00 #2803803 #8008008 #401ffcc0 #300c0300 #7c0f01c0 #803ff0', 
    ' #c0300c02 #fe0f0380 #e01f01ff #1e01e01 #30010016 #2003ff00 #0:2', 
    ' #f008000 #403ffc #0 #8000000 #ffe0e030 #200f #0', 
    ' #80000000 #ffc0f00 #8030 #0 #1c03004 #f00ffc1f #e00f00', 
    ' #8 #0 #f00f00 #e #0 #f00000 #e00f', 
    ' #0 #e0001000 #c070381 #0:2 #70381c00 #c0 #0', 
    ' #81c00000 #c0703 #0 #80000 #300000 #0 #381f81fc', 
    ' #80280380 #800800 #401ffcc #300c030 #7c0f01c #200803ff #c0300c0', 
    ' #ffe0f038 #1e01f01f #601e01e0 #3001001 #1c013ff0 #100180 #3003001', 
    ' #f00f0070 #80080101 #800800 #c008008 #c00e00c0 #1001801 #10010010', 
    ' #300300 #3003007 #8008018 #c0080080 #e00c00 #81e0f80f #c0703', 
    ' #0:2 #c070381c #0:2 #381c000 #c07 #0 #800', 
    ' #3000 #c000000 #e00f00f0 #800 #0 #f00f0000 #e00', 
    ' #0 #f0000000 #e00f00 #0 #100000 #200 #0', 
    ' #8000000 #3ffc070 #4 #0 #e030080 #e1e0fffe #381c0e07', 
    ' #1008040 #1ff80c02 #100180 #1001001 #70030010 #80300300 #800801', 
    ' #c008008 #f00e00c0 #40201f80 #6010080 #e7f0781c #80403f #c040201', 
    ' #ffff3c1c #c7c3e0f #40201008 #2010080 #300ffe #3800000 #180004', 
    ' #1800 #400700 #4006004 #20020 #0:6 #c03c0000 #2003803', 
    ' #0 #c0000000 #3803c03 #20 #0 #3c03c00 #38', 
    ' #0 #e0780000 #301c0 #0:2 #301c0e07 #0:2 #c0e07000', 
    ' #301 #0:2 #400 #7e000000 #e00e07e0 #200200 #e3002002', 
    ' #1830207f #df8f0e0c #83060c1f #ffbc70c1 #1f01f81f #1c01c0 #3001001', 
    ' #10011ff0 #300300 #1f00f007 #8008000 #c0080080 #1c00c00 #10010010', 
    ' #300300 #800003 #c00c008 #f80f00e0 #0:7 #803 #40000000', 
    ' #f01c0300 #201ffc1 #60100804 #7f0781c0 #c07e07fe #7807007 #c0040058', 
    ' #4ffc00 #2002002 #20020020 #80300300 #6007003 #40040040 #c00400', 
    ' #c01c00c #200600c0 #200200 #3003002 #7e03c038 #2010080 #e0701804', 
    ' #ff9fc1 #2400000 #300000 #f80009ff #7fc0000f #7e0000 #0:7', 
    ' #1f01f812 #601e01c0 #3001001 #fff3ff0 #fff00000 #ff000000 #40000001', 
    ' #0:6 #30020000 #80 #4000000 #1f01c030 #40201ffc #6010080', 
    ' #e7f0781c #7c07e07f #80780700 #c004005 #804ffc0 #80402010 #fc1e0701', 
    ' #1803ff9 #8008008 #c00c0080 #80f00e00 #1001801f #100100 #3001001', 
    ' #10030070 #80080080 #800800 #c00c008 #c00e0 #240000 #f0030000', 
    ' #ff80009f #7fc0000 #7e000 #0:6 #20000000 #1f01f01 #1601e01c', 
    ' #300100 #fff3ff #fff0000 #1ff00000 #4000000 #0:6 #4012000', 
    ' #300c030 #7c0f01c #7007ff #4004006 #c00c00c0 #7c03c01 #381f8780', 
    ' #100e070 #30080402 #80403fe0 #4020100 #ff3c1c0c #801c01ff #1001001', 
    ' #70030030 #1f00f00 #800801 #8008008 #c0080080 #1c00e00 #10010018', 
    ' #100100 #7003003 #f81f0030 #80780381 #800806 #ffcc008 #f00f00f0', 
    ' #f00f00 #e00e00f #800e0 #0:5 #100000 #fff #fff0', 
    ' #1ff00 #4000 #0:6 #2 #90 #80300c00 #0', 
    ' #30040000 #fc1f01c0 #8040201f #1c060100 #7fe7f078 #807807c0 #5807807', 
    ' #c00c0040 #100804ff #1804020 #f9fc1e07 #801803f #80080080 #c00c00', 
    ' #1f80f00e #100180 #1001001 #70030010 #80100300 #800800 #8008008', 
    ' #e00c00c0 #f00c00 #f00f00f #e00f00f0 #e00e00 #8 #0:5', 
    ' #fff0010 #fff00000 #ff000000 #40000001 #0:6 #f8120000 #1c01f81', 
    ' #1001601e #3ff00300 #0 #9 #c0 #0:6 #70381e0', 
    ' #c #0 #381c0000 #c070 #0 #c0000000 #c070381', 
    ' #0:2 #f00f000 #800e0 #0 #f000000 #800e00f0 #0:2', 
    ' #e00f00f0 #0:3 #800 #1f010010 #c01c01f0 #1001001 #1ff0030', 
    ' #70c18304 #fffde38 #c3830604 #7ffbf1e1 #e00e07e0 #200200 #e3002002', 
    ' #c004007f #1c00c00 #7c03c #20020020 #300200 #4007003 #c0040040', 
    ' #400c00 #2002000 #38030030 #3e03c0 #0:6 #30204000 #8f0e0c18', 
    ' #2003fdf #e0060060 #7e01e00 #1c0783c0 #807038 #18040201 #2003ff0', 
    ' #60020020 #600600 #1001000 #18010010 #380180 #6006002 #e01e00e0', 
    ' #6020007 #ffbc1c0c #81f81fff #803803 #8008008 #f00ff8c0 #f00f00', 
    ' #f00f00f #e00e00e0 #800 #0:5 #ff000000 #f000000f #ff', 
    ' #1ff #60 #0:6 #80000000 #0 #300008 #60100c0', 
    ' #20000040 #400600 #6002000 #60060 #200 #0:12 #80000000', 
    ' #301c0e07 #0:2 #c0e07000 #301 #0 #7000000 #301c0e', 
    ' #0 #200000 #c00000 #0 #3c03c030 #200380 #0', 
    ' #3c000000 #3803c0 #0:2 #803c03c0 #3 #40000000 #80000', 
    ' #0:2 #ff03c020 #100f #0 #c020000 #83fff838 #70381f87', 
    ' #20100e0 #e0300804 #803f #0:2 #fff03c02 #31f0f83 #10080402', 
    ' #80804020 #200c03ff #0 #c010000 #ff07c070 #c01007 #c0700c03', 
    ' #ffc1f03 #3008020 #c0e0300c #c03fff83 #3803c03 #20 #0', 
    ' #3c03c00 #38 #0 #3c00000 #3803c #0 #80004000', 
    ' #301c0e07 #0:2 #c0e07000 #301 #0 #7000000 #301c0e', 
    ' #0 #200000 #c00000 #0 #7807c070 #80780780 #c004005', 
    ' #800ffc0 #300c020 #e0f0380c #401fff #c0300c03 #f07c0f01 #e07e07ff', 
    ' #a00e00 #2002002 #c03ff30 #20 #1000000 #7c0700c #7ff', 
    ' #0:2 #fff01000 #6007007 #c0040040 #1c00c00 #407c03c #20020020', 
    ' #200200 #3003002 #10070038 #c0300c0 #1f03c070 #1c01ffc #10010018', 
    ' #300300 #1f00f007 #e07e1e00 #40381c0 #c0201008 #1801ff80 #100100', 
    ' #1001001 #30070030 #80080100 #800800 #8008008 #c00e00c0 #1801c01', 
    ' #30010010 #700300 #1f00f #8040201 #f0703010 #e07ffffc #1e00e07', 
    ' #200201a #3ff30020 #c03c03c0 #3c03c03 #3803803c #200380 #0:5', 
    ' #400000 #3ffc #3ffc0 #7fc00 #10000 #0:6 #8', 
    ' #240 #3c03000 #2003803c #0:2 #3803c03c #0:2 #3c03c000', 
    ' #380 #0 #40 #300000 #8000c000 #301c0e07 #0:2', 
    ' #c0e07000 #301 #0 #7000000 #301c0e #0 #c0200000', 
    ' #31f0f83 #10080402 #80804020 #200c03ff #0 #c010000 #ff07c070', 
    ' #7 #0:2 #7fff010 #20020020 #200200 #3002002 #70070038', 
    ' #400600 #c00c004 #c03c01c0 #8040007 #c0402010 #fff3c1c0 #8040201f', 
    ' #1c060100 #3fe7f078 #381f878 #20100e07 #3008040 #c01007fe #700c0300', 
    ' #fc1f03c0 #1801c01f #100100 #7003003 #1f00f0 #c0e07e1e #8040381', 
    ' #80c02010 #20100ff #30100804 #fffcf070 #6007007 #c0040040 #1c00c00', 
    ' #407c03c #20020020 #200200 #3002002 #60070038 #400400 #c004004', 
    ' #c01c00c0 #0 #e0780900 #70381c0 #70381c0e #30180c0 #0:6', 
    ' #7800200 #301c0e #0:2 #1c0e070 #3 #0 #e070000', 
    ' #301c #0 #2000 #8000c000 #70381f87 #20100e0 #e0300804', 
    ' #200c03f #0 #c01000 #7ff07c07 #2010080 #e0701804 #1ff9fc1', 
    ' #1e01e01f #1601e0 #ff003001 #8008013 #80080080 #c00800 #1c00e00c', 
    ' #100180 #1001001 #70030030 #80300300 #800801 #c008008 #f00e00c0', 
    ' #40201f80 #6010080 #e7f0781c #3c03c03f #c03c03c0 #3803c03 #20038038', 
    ' #0:5 #40000000 #3ffc00 #3ffc000 #7fc0000 #1000000 #0:6', 
    ' #7e04800 #7807007e #400580 #ffc00c #c0000 #0 #c01007', 
    ' #c0700c03 #1ffc1f03 #1801c0 #3001001 #f0070030 #1e001f00 #81c0e07e', 
    ' #10080403 #ff80c020 #1001801 #10010010 #300100 #1003007 #8008008', 
    ' #80080080 #c00800 #1c01c00e #100180 #3003001 #f00f0070 #2010001', 
    ' #30100804 #fffcf070 #e07e07f #201a01e0 #200200 #3c03ff3 #3c03c03c', 
    ' #803c03c0 #3803803 #20 #0:5 #3ffc0040 #ffc00000 #fc000003', 
    ' #7 #1 #0:5 #80000 #2400000 #30000000 #c00000', 
    ' #1c0e0780 #30 #0 #e0700000 #301c0 #0:2 #301c0e07', 
    ' #0 #20000000 #3c03c000 #200380 #0 #3c000000 #3803c0', 
    ' #0:2 #803c03c0 #3 #40000000 #0 #803000 #0:2', 
    ' #f01c0200 #100ff #0 #c0200000 #3fff8380 #381f878 #20100e07', 
    ' #3008040 #80403fe #c0402010 #fff3c1c0 #8040201f #1c060100 #ffe7f078', 
    ' #200600 #2002002 #38030030 #7e03c0 #4004006 #40040040 #1c00c00', 
    ' #7c0400c #78078078 #400580 #4ffc00c #300c010 #3c0700c #c01ffc1f', 
    ' #1001801 #30030010 #f00700 #7e1e001f #301c0e8 #20100804 #1ff80c0', 
    ' #10010018 #100100 #7003001 #8010030 #80080080 #800800 #e00c008', 
    ' #801c01c0 #1001001 #70030030 #1f00f00 #4020100 #70301008 #83fffcf0', 
    ' #70381f87 #20100e0 #e0300804 #27fff #f00003fe #1f80001f #0:7', 
    ' #80 #3c02400 #2003803c #0:2 #3803c03c #0:2 #3c03c000', 
    ' #380 #0 #40 #78300000 #301c0e0 #0:2 #1c0e0700', 
    ' #30 #0 #e0700000 #301c0 #0 #20000 #3803c03c', 
    ' #200 #0 #3c03c000 #380 #0 #3c000000 #3803c0', 
    ' #0 #40000 #0 #c000003 #7807c040 #80780780 #c004005', 
    ' #800ffc0 #300c020 #e0f0380c #401fff #c0300c03 #f07c0f01 #e07e07ff', 
    ' #a00e00 #2002002 #c03ff30 #20 #1000000 #7c0700c #7ff', 
    ' #0:2 #fff01000 #2002007 #20020020 #300200 #7003803 #40060070', 
    ' #c00400 #3c01c00c #100407c0 #c0300c0 #1f03c070 #1c01ffc #10010018', 
    ' #300300 #1f00f007 #e07e1e00 #40381c0 #c0201008 #100ff80 #10080402', 
    ' #fcf07030 #7007ff #4004006 #c00c00c0 #7c03c01 #2002004 #20020020', 
    ' #200200 #7003803 #40040060 #400400 #1c00c00c #e07c00c0 #1e00e07', 
    ' #200201a #3ff30020 #c03c03c0 #3c03c03 #3803803c #200380 #0:5', 
    ' #400000 #3ffc #3ffc0 #7fc00 #10000 #0:6 #8', 
    ' #240 #3000 #c0 #c0300000 #3803c03 #20 #0', 
    ' #3c03c00 #38 #0 #3c00000 #3803c #0 #80004000', 
    ' #301c0e07 #0:2 #c0e07000 #301 #0 #7000000 #301c0e', 
    ' #0 #200000 #80 #0 #2000000 #7ff01c #4004006', 
    ' #40040040 #1c00c00 #600c00c #20020020 #300200 #3c03803 #100807e', 
    ' #70180402 #ff9fc1e0 #4020100 #70301008 #7fffcf0 #40060070 #c00400', 
    ' #3c01c00c #f83c07c0 #402031f0 #2010080 #fff80804 #e07e07 #200a00e', 
    ' #30020020 #c03ff #e00000 #60001 #600 #800800c0 #1001801', ' #8008 ]', ), 
    )
a.Set(elements=elements1, name='PoorElements-1')
set1 = mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.sets['PoorElements-1']
leaf = dgm.LeafFromSets(sets=(set1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2242.54, 
    farPlane=3231.57, width=796.523, height=287.7, cameraPosition=(-1442.59, 
    -1645.21, 818.34), cameraTarget=(276.199, 251.814, 6.74342))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2234.35, 
    farPlane=3239.76, cameraPosition=(-1442.59, -1645.21, 818.34), 
    cameraUpVector=(0.000828773, 0.392707, 0.919663), cameraTarget=(276.199, 
    251.814, 6.74341))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2269.73, 
    farPlane=2977.83, cameraPosition=(-709.054, -1966.42, 1162.01), 
    cameraUpVector=(0.162156, 0.396099, 0.903776), cameraTarget=(290.03, 
    245.757, 13.2235))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2318.01, 
    farPlane=2929.53, width=247.841, height=89.5189, cameraPosition=(-767.13, 
    -1968.02, 1108.43), cameraTarget=(231.954, 244.16, -40.3604))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2299.1, 
    farPlane=3364.03, cameraPosition=(-1838.99, -1211.79, 831.867), 
    cameraUpVector=(0.264207, 0.184744, 0.946607), cameraTarget=(257.148, 
    226.385, -33.8601))
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    position=362.762)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    activeCutName='X-Plane', viewCut=ON)
session.viewports['Viewport: 1'].assemblyDisplay.viewCuts['X-Plane'].setValues(
    position=84.084)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2256.03, 
    farPlane=3407.1, width=798.421, height=288.385, cameraPosition=(-1893.29, 
    -1114.8, 861.509), cameraTarget=(202.846, 323.373, -4.21833))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1678.09, 
    -1401.52, 906.269), cameraTarget=(418.05, 36.6577, 40.5419))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=OFF)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
