"""
Title: ComfyUI-JNT
Version: 0.0.1

Authors:
    - JervNorsk (Lead Developer, Core Implementation)

Description: This extensions provides various nodes to support JNT workflows.

"""
###############################################################################
# Dependencies
# -----------------------------------------------------------------------------
import os
import sys
import importlib
import pkgutil

from .utils.path import JNT_DIR
from .utils.logger import LOG

###############################################################################
# Bootstrap
# -----------------------------------------------------------------------------
LOG.debug("\n")
LOG.debug("################################################################################")
# TODO: write configurations and set real version instead SNAPSHOT
LOG.info("### Loading: %s (%s)", LOG.name, "SNAPSHOT")
LOG.debug("\n")

# Import JNT modules
from .comfy import nodes
from . import externals

# Load ComfyUI Custom Nodes
nodes.load_custom_nodes()

LOG.debug("--------------------------------------------------------------------------------")
LOG.debug("\n")

###############################################################################
# ComfyUI
# -----------------------------------------------------------------------------
NODE_CLASS_MAPPINGS = nodes.to_comfy_node_class_mappings()
NODE_DISPLAY_NAME_MAPPINGS = nodes.to_comfy_node_display_name_mappings()
WEB_DIRECTORY = os.path.join(JNT_DIR, "comfy")