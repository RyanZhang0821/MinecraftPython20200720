# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:13:08 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You're now at X:"+str(x)+"Y:"+str(y)+"Z:"+str(z))