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
from .utils.logging import LOG

###############################################################################
# Bootstrap
# -----------------------------------------------------------------------------
LOG.info("\n")
LOG.info("################################################################################")
LOG.info("## Loading: %s (%s)", LOG.name, "SNAPSHOT")
LOG.info("\n")

# Append JNT dir to sys.path for module loading
# sys.path.append(path.JNT_DIR)

LOG.info(sys.path)

# Import JNT modules
from .comfy import nodes

nodes.load_custom_nodes()

LOG.info("Registered custom nodes: %s", nodes.get_custom_nodes())

# from .common import configuration
#
# configuration.JNT_DIR

LOG.info("--------------------------------------------------------------------------------")
LOG.info("\n")

###############################################################################
# ComfyUI Declarations
# -----------------------------------------------------------------------------
NODE_CLASS_MAPPINGS = nodes.to_comfy_node_class_mappings()
NODE_DISPLAY_NAME_MAPPINGS = nodes.to_comfy_node_display_name_mappings()

###############################################################################
# ComfyUI Bootstrap
# -----------------------------------------------------------------------------
# print(f"### Loading: JNT ({JNT_CONFIG['version']})")
#
# import folder_paths

# Append Comfy dir to sys.path & import files
# sys.path.append(COMFY_DIR)
# print(sys.path)
# import comfy.sample
# import comfy.samplers
# import comfy.sd
# import comfy.utils
# sys.path.remove(COMFY_DIR)

# Append Comfy dependencies dir to sys.path & import files
# sys.path.append(COMFY_CUSTOM_NODE_WD14_DIR)
# wd14tagger = importlib.import_module("ComfyUI-WD14-Tagger.wd14tagger")
# sys.path.remove(COMFY_CUSTOM_NODE_WD14_DIR)

# print(ComfyUI_WD14_Tagger)

###############################################################################
# ComfyUI Custom Nodes
# -----------------------------------------------------------------------------
# from jnt.comfy.nodes import JntTagger

# NODE_CLASS_MAPPINGS.update({
#     JntTagger.CONFIG['id']: JntTagger,
# })
# NODE_DISPLAY_NAME_MAPPINGS.update({
#     JntTagger.CONFIG['id']: JntTagger.CONFIG['name'],
# })
# -----------------------------------------------------------------------------

###############################################################################
# ComfyUI Exports
# -----------------------------------------------------------------------------
__all__ = [ 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS' ]