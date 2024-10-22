###############################################################################
# Dependencies
# -----------------------------------------------------------------------------
import os
import sys
import importlib
from pathlib import Path
import pkgutil

from ...utils.logger import LOG

###############################################################################
# Constants
# -----------------------------------------------------------------------------
COMFY_CUSTOM_NODES = []

###############################################################################
# Declarations
# -----------------------------------------------------------------------------
def register_custom_nodes(id, name, class_type):
    COMFY_CUSTOM_NODES.append({
        'id': id,
        'name': name,
        "class_type": class_type
    })

def get_custom_nodes():
    return COMFY_CUSTOM_NODES

def load_custom_nodes(category = None):
    """
    :param category: if specified detect and load each custom nodes inside a specific category
    :return:
    """
    package_path = Path(os.path.dirname(__file__))
    package_prefix = __name__ + '.'

    if category is not None:
        """Detect and load each custom nodes inside a specific category"""
        package_path = os.path.join(package_path, category)
        package_prefix += category + "."

        for _, custom_node_name, _ in (pkgutil.iter_modules([package_path.__str__()], package_prefix)):
            LOG.info("Loading custom node: %s", custom_node_name)
            importlib.import_module(custom_node_name)
    else:
        """Detect and load each category defined inside this module package"""
        for file in package_path.iterdir():
            if file.is_dir():
                LOG.debug("Loading category: %s", file.name)
                load_custom_nodes(file.name)

def to_comfy_node_class_mappings():
    node_class_mappings = {}

    for custom_node in COMFY_CUSTOM_NODES:
        node_class_mappings.update({
            custom_node['id']: custom_node['class_type']
        })

    return node_class_mappings

def to_comfy_node_display_name_mappings():
    node_display_name_mappings = {}

    for custom_node in COMFY_CUSTOM_NODES:
        node_display_name_mappings.update({
            custom_node['id']: custom_node['name']
        })

    return node_display_name_mappings