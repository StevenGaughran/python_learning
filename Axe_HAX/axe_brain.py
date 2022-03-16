# ~~~~ WIN RATES ~~~~

def axe_win_rate_casual(stats):
    picks = stats[1]["1_pick"] \
            + stats[1]["2_pick"] \
            + stats[1]["3_pick"] \
            + stats[1]["4_pick"] \
            + stats[1]["5_pick"]
    wins = stats[1]["1_win"] \
            + stats[1]["2_win"] \
            + stats[1]["3_win"] \
            + stats[1]["4_win"] \
            + stats[1]["5_win"]
    return round((wins / picks) * 100)


def axe_win_rate_pro(stats):
    picks = stats[1]["pro_pick"]
    wins = stats[1]["pro_win"]
    return round((wins / picks) * 100)

# ~~~~ MATCHUPS (a work in progress, obviously) ~~~~
# def axe_matchups():
#     response = requests.get("https://api.opendota.com/api/heroes/2/matchups")
#     response.raise_for_status()
#     data = response.json()
#     print(data)
#     for r in data:
#         matchups = []
#         names = []
#         wins = r["wins"]
#         g_p = r["games_played"]
#         if wins/g_p >= 0.3:
#             matchups.append(r["hero_id"])
#     print(matchups)
#
#
# axe_matchups()
