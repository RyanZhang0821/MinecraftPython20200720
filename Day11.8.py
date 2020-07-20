# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:56:05 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlock(x+1,y,z,56)
mc.setBlock(x-1,y,z,56)
mc.setBlock(x,y,z+1,56)
mc.setBlock(x,y,z-1,56)
mc.setBlock(x+1,y,z+1,56)
mc.setBlock(x-1,y,z+1,56)
mc.setBlock(x+1,y,z-1,56)
mc.setBlock(x-1,y,z-1,56)