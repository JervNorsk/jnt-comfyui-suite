###############################################################################
# Dependencies
# -----------------------------------------------------------------------------
import os
import sys
import importlib

from ..utils.logger import LOG


###############################################################################
# Declarations
# -----------------------------------------------------------------------------
def __load_module(owner, name):
    module_path = f"ComfyUI-JNT.externals.{owner}.{name}"

    LOG.info("Loading external module: %s", module_path)

    return importlib.import_module(module_path)

###############################################################################
# Exports
# -----------------------------------------------------------------------------
WD14TAGGER = lambda: __load_module("pythongosssss", "wd14-tagger")