#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Funciones auxiliares.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os

import matplotlib.pyplot as plt


def add_labels_to_geodataframe(ax, gdf, label_column, round_decimals=None,
                               fontsize=12, color="white"):

    # crea los centroides
    gdf["centroid"] = gdf["geometry"].centroid
    gdf_points = gdf.copy()
    gdf_points.set_geometry("centroid", inplace=True)

    texts = []
    if round_decimals:
        labels = gdf_points[label_column].round(round_decimals)
    else:
        labels = gdf_points[label_column]
    for x, y, label in zip(gdf_points.geometry.x,
                           gdf_points.geometry.y,
                           labels):
        texts.append(plt.text(x, y, label, fontsize=fontsize, color=color))
