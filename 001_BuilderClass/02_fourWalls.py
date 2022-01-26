def on_on_chat():
    builder.move(LEFT, 5)
    builder.mark()
    for index in range(10):
        for index2 in range(4):
            builder.move(FORWARD, 10)
            builder.turn(LEFT_TURN)
        builder.move(UP, 1)
    builder.trace_path(DIAMOND_BLOCK)
    builder.place(AIR)
player.on_chat("fourWalls", on_on_chat)
