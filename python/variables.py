# -*- coding: utf8 -*-

import os

tokens = eval(os.environ['AUTH_TOKENS'])

terrains_rgb = {"Plaine":         ( 51, 204, 51 ),
                "Océan":          (  0, 102, 255),
                "Espace pavé":    (128, 128, 128),
                "Terre battue":   (153, 102, 51 ),
                "Plaine fleurie": ( 51, 153, 51 )}
