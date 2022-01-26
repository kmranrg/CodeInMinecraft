def on_on_chat():
    gameplay.time_set(gameplay.time(DAY))
    for index in range(20):
        mobs.spawn(HORSE, pos(0, 10, 0))
player.on_chat("animalRain", on_on_chat)
