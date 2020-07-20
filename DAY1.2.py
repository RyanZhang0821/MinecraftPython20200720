# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:59:49 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=53.6
y=100
z=120

mc.player.setTilePos(x,y,z)
