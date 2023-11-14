
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag': [300, 350, 425, 400, 360],
    'sourav': [180, 250, 200, 350, 150],
    'laxman': [345, 300, 200, 150, 190],
    'yuvraj': [190, 150, 120, 250, 275]
}

print(f"players: {players}")
print("-" * 60)

print(f"players['sachin'] :{players['sachin']}")
print(f"sum(players['sachin']) :{sum(players['sachin'])}")
print("-" * 60)

plyr_scr = {k: sum(v) for k, v in players.items()}
print(plyr_scr)
print("-" * 60)

plyr_scr = {name: (lambda score: sum(score) / len(score))(v)
            for name, v in players.items()}
print(plyr_scr)
print("-" * 60)

plyr_scr = [score for score in players.values()]
print(plyr_scr)
print("-" * 60)

plyr_scr = [scr for score in players.values() for scr in score]
print(plyr_scr)

# print runs of each player where it is greater than or equal to 200
