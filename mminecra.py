from mcpi.minecraft import Minecraft
import picamera
from time import sleep
mc = Minecraft.create()

while True:
    chatread = mc.events.pollChatPosts()
        

    
