from .test import TestNode

NODE_CLASS_MAPPINGS = {
    "ZZ-Test-Node" : TestNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZZ-Test-Node" : "ZZ Test Node",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']