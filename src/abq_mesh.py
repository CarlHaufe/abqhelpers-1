# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  Helper functions for ABAQUS Mesh
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      28.09.2022
# Execution:    Import functions / collections (from pyLek.helpers import util)
# Status:       In Progress
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Sources
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------

from abaqus import *
from abaqusConstants import *
import os

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Aus Journalfile übernommen -ch
# ------------------------------------------------------------------------------

# mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.setMeshControls(
#     elemShape=HEX, regions=
#     mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.instances['concrete-dummy-plates-1'].cells.getSequenceFromMask(
#     ('[#ffffffff #fe6bd7ff #3f ]', ), ), technique=STRUCTURED)

# mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.setElementType(
#     elemTypes=(ElemType(elemCode=C3D8R, elemLibrary=STANDARD), ElemType(
#     elemCode=C3D6, elemLibrary=STANDARD), ElemType(elemCode=C3D4, 
#     elemLibrary=STANDARD)), regions=(
#     mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.instances['concrete-dummy-plates-1'].cells.getSequenceFromMask(
#     ('[#ffffffff #fe6bd7ff #3f ]', ), ), ))

# mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.seedPartInstance(
#     deviationFactor=0.1, minSizeFactor=0.1, regions=(
#     mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.instances['concrete-dummy-plates-1'], 
#     ), size=5.0)

# mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.generateMesh(regions=(
#     mdb.models['Concrete_beam_4_cantilever_B'].rootAssembly.instances['concrete-dummy-plates-1'], 
#     ))

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# Seeding mesh für alle Instanzen kann genauso übernommen werden -ch
def seed_all_active_instances(model, size=4.0, deviationFactor=0.1, minSizeFactor=0.1):
    a = model.rootAssembly
    for key in a.instances.keys():
        # choose only active instances
        if a.instances[key].ips != None:
            # seed part instance
            a.seedPartInstance(
                regions=(a.instances[key],), size=size, deviationFactor=deviationFactor, minSizeFactor=minSizeFactor),

# # Seeding mesh zZ nicht gebraucht -ch
# def seed_active_instance(model, instance, size=10.0, deviationFactor=0.1, minSizeFactor=0.1):
#     a = model.rootAssembly
#     # choose only active instances
#     if a.instances[instance].ips != None:
#         # seed part instance
#         a.seedPartInstance(
#             regions=(a.instances[instance],), size=size, deviationFactor=deviationFactor, minSizeFactor=minSizeFactor),


# # Setting elementtypes for mesh bs (TET und FREE) zZ nicht gebraucht -ch
# def assign_mesh_control_all_active_instances(model, elemTypes, elemShape=TET, technique=FREE, ):
#     a = model.rootAssembly
#     for key in a.instances.keys():
#         # choose only active instances
#         if a.instances[key].ips != None:
#             c = a.instances[key].cells[:]
#             # choose only instances with cells (e.g no linear elements)
#             if c:
#                 a.setMeshControls(
#                     regions=c, elemShape=elemShape, technique=technique)
#                 a.setElementType(regions=(c,), elemTypes=(elemTypes))


# Setting elementtypes for mesh bs (HEX und STRUCTURED) -ch
def assign_mesh_control_all_active_instances(model, elemTypes, elemShape=HEX, technique=STRUCTURED, ):
    a = model.rootAssembly
    for key in a.instances.keys():
        # choose only active instances
        if a.instances[key].ips != None:
            c = a.instances[key].cells[:]
            # choose only instances with cells (e.g no linear elements)
            if c:
                a.setMeshControls(
                    regions=c, elemShape=elemShape, technique=technique)
                a.setElementType(regions=(c,), elemTypes=(elemTypes))


# Generate mesh
def generate_mesh_all_active_instances(model,):
    a = model.rootAssembly
    for key in a.instances.keys():
        # choose only active instances
        if a.instances[key].ips != None:
            # generate mesh
            a.generateMesh(
                regions=(a.instances[key],)),


# Delete mesh
def delete_mesh_all_active_instances(model,):
    a = model.rootAssembly
    for key in a.instances.keys():
    # choose only active instances
        if a.instances[key].ips != None:
            a.deleteMesh(
                regions=(a.instances[key],)),


# ------------------------------------------------------------------------------
# Original von bs
# ------------------------------------------------------------------------------
# def seed_all_active_instances(model, size=10.0, deviationFactor=0.1, minSizeFactor=0.1):
#     a = model.rootAssembly
#     for key in a.instances.keys():
#         # choose only active instances
#         if a.instances[key].ips != None:
#             # seed part instance
#             a.seedPartInstance(
#                 regions=(a.instances[key],), size=size, deviationFactor=deviationFactor, minSizeFactor=minSizeFactor),

# def seed_active_instance(model, instance, size=10.0, deviationFactor=0.1, minSizeFactor=0.1):
#     a = model.rootAssembly
#     # choose only active instances
#     if a.instances[instance].ips != None:
#         # seed part instance
#         a.seedPartInstance(
#             regions=(a.instances[instance],), size=size, deviationFactor=deviationFactor, minSizeFactor=minSizeFactor),

# def assign_mesh_control_all_active_instances(model, elemTypes, elemShape=TET, technique=FREE, ):
#     a = model.rootAssembly
#     for key in a.instances.keys():
#         # choose only active instances
#         if a.instances[key].ips != None:
#             c = a.instances[key].cells[:]
#             # choose only instances with cells (e.g no linear elements)
#             if c:
#                 a.setMeshControls(
#                     regions=c, elemShape=elemShape, technique=technique)
#                 a.setElementType(regions=(c,), elemTypes=(elemTypes))

# def generate_mesh_all_active_instances(model,):
#     a = model.rootAssembly
#     for key in a.instances.keys():
#         # choose only active instances
#         if a.instances[key].ips != None:
#             # seed part instance
#             a.generateMesh(
#                 regions=(a.instances[key],)),


# def delete_mesh_all_active_instances(model,):
#     a = model.rootAssembly
#     for key in a.instances.keys():
#     # choose only active instances
#         if a.instances[key].ips != None:
#             a.deleteMesh(
#                 regions=(a.instances[key],)),