# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:30:53 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getTilePos()


t=0
while True:
    t=t+1
    mc.setBlock(x,y+t,z,169)
    time.sleep(1)
    