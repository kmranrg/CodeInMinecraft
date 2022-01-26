def buildRoof():
    for index in range(11):
        if index % 2 == 0:
            builder.move(FORWARD, 10)
            builder.move(LEFT, 1)
            builder.turn(LEFT_TURN)
            builder.turn(LEFT_TURN)
        else:
            builder.move(FORWARD, 10)
            builder.move(RIGHT, 1)
            builder.turn(RIGHT_TURN)
            builder.turn(RIGHT_TURN)

def on_on_chat():
    builder.move(LEFT, 5)
    builder.mark()
    for index2 in range(10):
        for index3 in range(4):
            builder.move(FORWARD, 10)
            builder.turn(LEFT_TURN)
        builder.move(UP, 1)
    buildRoof()
    builder.trace_path(FARMLAND)
    builder.place(AIR)
player.on_chat("animalHouse", on_on_chat)
