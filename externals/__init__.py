###############################################################################
# Dependencies
# -----------------------------------------------------------------------------
import os
import sys
import importlib

###############################################################################
# Declarations
# -----------------------------------------------------------------------------
# def load_external_module():
#     COMFY_CUSTOM_NODE_WD14_DIR = os.path.abspath(os.path.join(COMFY_CUSTOM_NODE_DIR, 'ComfyUI-WD14-Tagger'))
#
#     try:
#         if COMFY_CUSTOM_NODE_WD14_DIR not in sys.path:
#             sys.path.append(COMFY_CUSTOM_NODE_WD14_DIR)
#             cleanup = True
#
#         cls.__wd14tagger = importlib.import_module("ComfyUI-WD14-Tagger.wd14tagger")
#     finally:
#         if cleanup:
#             sys.path.remove(COMFY_CUSTOM_NODE_WD14_DIR)