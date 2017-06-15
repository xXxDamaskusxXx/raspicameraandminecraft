from mcpi.minecraft import Minecraft
import picamera
from time import sleep
mc = Minecraft.create()
d=1
while True:
    x, y, z = mc.player.getPos()  
    input = raw_input("algo")
    if input == 'p':
        for q in range(0,60):
            x, y, z = mc.player.getPos() 
            n=1
            mc.setBlock(x, (y-1), z, 35, [n])
            n= n+1
            if n== 16:
                n=1
            sleep(0.1)
    if x==-41 and y==8 and z== -105:
        camera.awb_mode= 'incandescent'
        camera.capture('efecto.jpg')
    if input=='mimbre':
        mc.setBlocks(0,0,0,20,20,20,d,1)
        d=d+1
        if d==100:
            d=1
            
    if input == 'Teleport East':
        mc.player.setPos(x+20, y, z)

    if input == 'Teleport West':
        mc.player.setPos(x-20, y, z)

    if input == 'Teleport North':
        mc.player.setPos(x, y, z+20)

    if input == 'Teleport South':
        mc.player.setPos(x, y, z-20)

    if input == 'Tower':
        x, y, z = mc.player.getPos()  
        mc.setBlocks(x+11, y+2, z+9, x+22, y+12, z+16, 42)
        mc.setBlocks(x+12, y+3, z+10, x+21, y+11, z+15, 0)
        mc.setBlocks(x+10, y+2, z+8, x+22, y+2, z+16, 41)
        mc.setBlocks(x+9, y+1, z+7, x+23, y+1, z+17, 41)
        mc.setBlocks(x+8, y+0, z+6, x+24, y+0, z+18, 41)
        mc.setBlocks(x+7, y-1, z+5, x+25, y-1, z+19, 41)
        mc.setBlocks(x+6, y-2, z+4, x+26, y-2, z+20, 41)
        mc.setBlocks(x+5, y-3, z+3, x+27, y-3, z+21, 41)
        mc.setBlocks(x+4, y-4, z+2, x+28, y-4, z+22, 41)
        mc.setBlocks(x+16, y+3, z+16, x+17, y+4, z+16, 0)
        mc.setBlocks(x+16, y+3, z+16, x+17, y+3, z+16, 64)
        mc.setBlock(x+11, y+13, z+9, 42)
        mc.setBlock(x+13, y+13, z+9, 42)
        mc.setBlock(x+15, y+13, z+9, 42)
        mc.setBlock(x+18, y+13, z+9, 42)
        mc.setBlock(x+20, y+13, z+9, 42)
        mc.setBlock(x+22, y+13, z+9, 42)
        mc.setBlock(x+11, y+13, z+16, 42)
        mc.setBlock(x+13, y+13, z+16, 42)
        mc.setBlock(x+15, y+13, z+16, 42)
        mc.setBlock(x+18, y+13, z+16, 42)
        mc.setBlock(x+20, y+13, z+16, 42)
        mc.setBlock(x+22, y+13, z+16, 42)
        mc.setBlock(x+11, y+13, z+11, 42)
        mc.setBlock(x+22, y+13, z+11, 42)
        mc.setBlock(x+11, y+13, z+14, 42)
        mc.setBlock(x+22, y+13, z+14, 42)
