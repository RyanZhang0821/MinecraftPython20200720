# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:36:14 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=12.45
y=211.1
z=1.15

mc.player.setPos(x,y,z) 