# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  Helper functions for ABAQUS Property
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      03.11.2022
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

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

def create_analysis_step(model, stepName, preStepName, initialInc, minInc, maxInc, incNumber, nlgeom):
    a = model.StaticStep(name=stepName, previous=preStepName,
                         initialInc=initialInc, maxInc=maxInc, minInc=minInc, nlgeom=nlgeom)
    a = model.steps[stepName].setValues(maxNumInc=incNumber)


def create_support_at_RP(model, referencePoint, bcName='support_', stepName="Initial",u1=UNSET, u2=SET, u3=SET,
                         ur1=SET, ur2=UNSET, ur3=UNSET,):
    # Get reference point
    a = model.rootAssembly
    region = a.Set(referencePoints=(
        referencePoint[1],), name="bcName_" + referencePoint[0].name,)
    # Assign boundary condition
    model.DisplacementBC(name=bcName + referencePoint[0].name, createStepName=stepName, region=region, u1=u1, u2=u2, u3=u3,
                         ur1=ur1, ur2=ur2, ur3=ur2, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)


def create_roller_support_at_RP(model, referencePoint, bcName='roller_', stepName="Initial"):
    create_support_at_RP(model, referencePoint, bcName=bcName, stepName="Initial",u1=UNSET, u2=SET, u3=SET,ur1=SET, ur2=UNSET, ur3=UNSET),


def create_hinge_support_at_RP(model, referencePoint, bcName='hinge_', stepName="Initial"):
    create_support_at_RP(model, referencePoint, bcName=bcName, stepName="Initial", u1=SET, u2=SET, u3=SET, ur1=SET, ur2=UNSET, ur3=UNSET),


def create_suppress_axial_rotation_at_edge(model, instance, stepName="Initial"):
    # Get edges
    a = model.rootAssembly
    e = a.instances[instance].edges[:]
    region = a.Set(edges=e, name='axial_rotation_' + instance)

    # Assign boundary condition
    model.DisplacementBC(name='axial_rotation_' + instance, createStepName=stepName, region=region, u1=UNSET, u2=UNSET, u3=UNSET,
                         ur1=SET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)


#running function:
# # Create Loading
# for referencePoint in referencePoints:
#     if 'load_traverse' in referencePoint[1]:
#         abq_step.create_vertical_disp_at_RP(
#             model, referencePoint[0], uz=-30, bcName='load_disp_', stepName='load_disp')

def create_vertical_disp_at_RP(model, referencePoint, uz=1, bcName='load_disp_', stepName="load_disp"):
    # Get reference point
    a = model.rootAssembly
    region = a.Set(referencePoints=(
        referencePoint[1],), name="load_disp_" + referencePoint[0].name,)
    # Assign boundary condition
    model.DisplacementBC(name=bcName + referencePoint[0].name, createStepName=stepName, region=region, u1=SET, u2=SET, u3=uz,
                         ur1=SET, ur2=UNSET, ur3=SET, amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
#def create_seesaw_support_at_RP(model, referencePoint, bcName='load_traverse', stepName="Initial"):
#    create_support_at_RP(model, referencePoint, bcName=bcName, stepName="Initial", u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET),


def create_prestress_temperature_at_(model, instance, magnitude, stepName='Prestress'):
    # Get edges
    a = model.rootAssembly
    e = a.instances[instance].edges[:]
    region = a.Set(edges=e, name='prestress_' + instance)
    model.Temperature(name='prestress_' + instance, createStepName=stepName, region=region,
                      distributionType=UNIFORM, crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(magnitude, ))


def create_prestress_temperature_at_solid(model, instance, magnitude, stepName='Prestress'):
    # Get edges
    a = model.rootAssembly
    c = a.instances[instance].cells[:]
    region = a.Set(cells=c, name='prestress_' + instance)
    model.Temperature(name='prestress_' + instance, createStepName=stepName, region=region,
                      distributionType=UNIFORM, crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(magnitude, ))

def deactivate_boundary_condition(model, bcName, stepName):
    model.boundaryConditions[bcName].deactivate(stepName)

def reset_predefined_field_to_initial(model, fieldName, stepName):
    model.predefinedFields[fieldName].resetToInitial(stepName)