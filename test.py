import numpy as np
import torch


class TestNode:

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required" : {
                "image" : ("IMAGE",),
                "scale" : ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01},),
            }
        }
    
    CATEGORY = "Test Nodes"
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ["image"]

    FUNCTION = "render_effect"

    def render_effect(self, image, scale):
        image = (1 - image) * scale
        image = torch.clamp(image, 0, 1)
        return (image, )
