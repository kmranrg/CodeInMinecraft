def on_travelled_walk():
    blocks.place(YELLOW_FLOWER, pos(1, 0, 0))
    blocks.place(OXEYE_DAISY, pos(0, 0, 0))
    blocks.place(POPPY, pos(-1, 0, 0))
player.on_travelled(WALK, on_travelled_walk)
