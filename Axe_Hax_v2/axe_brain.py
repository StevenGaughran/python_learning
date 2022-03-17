# ~~~~ THIS IS WHERE WE STORE MOST OF THE FUNCTIONS THAT MAKE THIS APP RUN ~~~~
from hero_id import hero_id_numbers


def axe_win_rate_casual(stats):
    picks = stats[1]["1_pick"] \
            + stats[1]["2_pick"] \
            + stats[1]["3_pick"] \
            + stats[1]["4_pick"] \
            + stats[1]["5_pick"]
    wins = stats[1]["1_win"]\
           + stats[1]["2_win"] \
           + stats[1]["3_win"] \
           + stats[1]["4_win"] \
           + stats[1]["5_win"]
    return round((wins / picks) * 100)


def axe_win_rate_pro(stats):
    picks = stats[1]["pro_pick"]
    wins = stats[1]["pro_win"]
    return round((wins / picks) * 100)


def axe_victims(stats):
    win_rate = 0
    name = ""
    for i in stats:
        wins = i["wins"]
        games = i["games_played"]
        w_r = wins / games * 100
        if w_r >= win_rate:
            win_rate = w_r
            for x in hero_id_numbers:
                if i["hero_id"] == x["id"]:
                    name = x["localized_name"]
    victim = f"{name} ({round(win_rate)}% win rate)"
    return victim


def axe_bully(stats):
    win_rate = 100
    name = ""
    for i in stats:
        wins = i["wins"]
        games = i["games_played"]
        w_r = wins / games * 100
        if w_r <= win_rate:
            win_rate = w_r
            for x in hero_id_numbers:
                if i["hero_id"] == x["id"]:
                    name = x["localized_name"]
    bully = f"{name} ({round(win_rate)}% win rate)"
    return bully
