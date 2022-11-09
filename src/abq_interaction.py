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
import os
import pickle
import numpy as np

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


def create_embedded_region(model, name, embeddedInstance, hostInstace):
    a = model.rootAssembly
    c = a.instances[embeddedInstance].cells[:]
    e = a.instances[embeddedInstance].edges[:]
    embeddedRegion = a.Set(edges=e, cells=c, name='m_' + embeddedInstance)

    c = a.instances[hostInstace].cells[:]
    e = a.instances[hostInstace].edges[:]
    hostRegion = a.Set(edges=e, cells=c, name='s_' + hostInstace)

    model.EmbeddedRegion(name=name, embeddedRegion=embeddedRegion, hostRegion=hostRegion,
                         weightFactorTolerance=1e-06, absoluteTolerance=0.0, fractionalTolerance=0.05, toleranceMethod=BOTH)


def create_mpc_beam_constraint(model, referencePoint, instance):
    # Get reference point
    a = model.rootAssembly
    controlPoint = a.Set(referencePoints=(
        referencePoint[1],), name="m_" + referencePoint[0].name,)

    # Get corresponding face
    f = a.instances[instance].faces
    myFace = f.findAt(
        (referencePoint[0].xValue, referencePoint[0].yValue, referencePoint[0].zValue),)
    face = (f[myFace.index:myFace.index+1], )
    surface = a.Set(name="s_" + referencePoint[0].name, faces=face)

    # Create MPC
    model.MultipointConstraint(name="mpc_beam_" + referencePoint[0].name, controlPoint=controlPoint,
                               surface=surface, mpcType=BEAM_MPC, userMode=DOF_MODE_MPC, userType=0, csys=None)
