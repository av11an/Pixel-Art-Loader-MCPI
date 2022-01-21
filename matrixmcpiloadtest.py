
from turtle import width
from mcpi.minecraft import Minecraft
from mcpi import block
from pixelartClass import *
import time


def clearAir(mc,x,y,z):
  mc.setBlocks(x-50,y-50,z-50,x+50,y+50,z+50,0)
 

def matrix(mc,x,y,z,X,w,l):
	y1 = w
	for h in range (0,w):
		x1 = l
		for k  in range (0,l):
			theBlock = X[h][k]
			if (theBlock == '0'):
				mc.setBlock(x1-x,y1+y,z,35,0)
			elif (theBlock == '1'):
				mc.setBlock(x1-x,y1+y,z,35,1)
			elif (theBlock == '2'):
				mc.setBlock(x1-x,y1+y,z,35,2)
			elif (theBlock == '3'):
				mc.setBlock(x1-x,y1+y,z,35,3)
			elif (theBlock == '4'):
				mc.setBlock(x1-x,y1+y,z,35,4)
			elif (theBlock == '5'):
				mc.setBlock(x1-x,y1+y,z,35,5)
			elif (theBlock == '6'):
				mc.setBlock(x1-x,y1+y,z,35,6)
			elif (theBlock == '7'):
				mc.setBlock(x1-x,y1+y,z,35,7)
			elif (theBlock == '8'):
				mc.setBlock(x1-x,y1+y,z,35,8)
			elif (theBlock == '9'):
				mc.setBlock(x1-x,y1+y,z,35,9)
			elif (theBlock == 'A'):
				mc.setBlock(x1-x,y1+y,z,35,10)
			elif (theBlock == 'B'):
				mc.setBlock(x1-x,y1+y,z,35,11)
			elif (theBlock == 'C'):
				mc.setBlock(x1-x,y1+y,z,35,12)
			elif (theBlock == 'D'):
				mc.setBlock(x1-x,y1+y,z,35,13)
			elif (theBlock == 'E'):
				mc.setBlock(x1-x,y1+y,z,35,14)
			elif (theBlock == 'F'):
				mc.setBlock(x1-x,y1+y,z,35,15)
			x1 = x1 - 1
		y1 = y1 - 1
		print()
    
def loadArt(pA, ip):
  loadart = pA
  loadart_array = loadart.get_array()
  loadart_width = loadart.get_size()[1]
  loadart_length = loadart.get_size()[0]
  mc = Minecraft.create(ip, 4711)
  x,y,z = mc.player.getPos()
  mc.player.setPos(x,y-20,z-5)
  clearAir(mc,x,y,z)
  matrix(mc,x,y-20,z+5,loadart_array,loadart_width,loadart_length)
  print("Done")


# main

if __name__ == "__main__":
	loadArt()



	   
		
