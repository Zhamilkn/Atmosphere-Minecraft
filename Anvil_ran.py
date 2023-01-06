from mcpi.minecraft import Minecraft
import time
import random

# подключаемся к серверу
mc = Minecraft.create()
def Sus(size,count):
    blocks = []
    x_start, y_start, z_start = mc.player.getTilePos()
    for x in range(size):
        blocks.append([])
        for z in range(size):
            blocks[x].append((35, random.randint(0, 15)))

    for x in range(size):
        for z in range(size):
            mc.setBlock(x_start + x, 115, z_start +
                        z, blocks[x][z][0], blocks[x][z][1])
            z += 1
        x += 1

    mc.player.setTilePos(x_start + x // 2, 116, z_start + z // 2)


    x_end, y_end, z_end = x_start+len(blocks), y_start+len(blocks), z_start+len(blocks)

    mc.player.setTilePos(x_start+3, y_start+2, z_start+3)

    # пробегаемся по двумерному массиву
    # устанавливаем бл
    start_x = x
    x_start_podium = x_start
    z_start_podium = z_start

    for row in blocks:
        for color in row:
            mc.setBlock(x_start_podium, y_start, z_start_podium, 35, color)

            x_start_podium += 1
        z_start_podium += 1
        x_start_podium = start_x

    for number in range(count):
        x_random = random.randint(x_start,x_end)
        y_random = random.randint(y_start,y_end)
        z_random = random.randint(z_start,z_end)

        mc.setBlock(x_random, y_random+10,z_random, 145)
        time.sleep(0.3)

if __name__ == "__main__":
    Sus(15,50)