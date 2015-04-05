def winter_is_coming(seasons):
    counter = 0
    winter_is_coming = False
    for season in seasons:
        if season == "winter":
            counter = 0
        else:
            counter += 1
    if counter >= 5:
        winter_is_coming = True
    return winter_is_coming
