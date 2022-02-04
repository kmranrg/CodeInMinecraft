def on_on_chat():
    gameplay.time_set(gameplay.time(NIGHT))
    sparklingBorders()
    buildPool()
    glassPlatform()
    player.teleport(pos(0, 115, 0))
    gameplay.set_game_mode(SURVIVAL, mobs.target(ALL_PLAYERS))
    gameplay.title(mobs.target(ALL_PLAYERS), "Leap of Faith", "by Anurag")
player.on_chat("lof", on_on_chat)

def sparklingBorders():
    blocks.fill(SEA_LANTERN,
        pos(-3, -4, -3),
        pos(3, -1, 3),
        FillOperation.REPLACE)
def glassPlatform():
    blocks.fill(GLASS,
        pos(-1, 114, -1),
        pos(1, 114, 1),
        FillOperation.REPLACE)
def buildPool():
    blocks.fill(WATER, pos(-2, -3, -2), pos(2, -1, 2), FillOperation.REPLACE)