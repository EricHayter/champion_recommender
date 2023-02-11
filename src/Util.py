
def transform_prop_playtime(champions: list) -> list:
    c = champions[:]
    total_mastery_points = sum(champ['championPoints'] for champ in c)
    for champion in c:
        champion['championPoints'] /= total_mastery_points

    return c