def on_on_chat():
    builder.move(LEFT, 5)
    builder.mark()
    for index in range(4):
        builder.move(FORWARD, 10)
        builder.turn(LEFT_TURN)
    builder.trace_path(SPRUCE_FENCE)
player.on_chat("fenceBoundary", on_on_chat)
