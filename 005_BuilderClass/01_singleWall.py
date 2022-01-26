def on_on_chat():
    builder.move(LEFT, 5)
    builder.mark()
    for index in range(10):
        builder.move(FORWARD, 10)
        builder.move(UP, 1)
        builder.turn(LEFT_TURN)
        builder.turn(LEFT_TURN)
    builder.trace_path(BRICKS)
    builder.place(AIR)
player.on_chat("singleWall", on_on_chat)
