def show_track(playlist):
    """..."""
    playlist_1 = {"nom":"Wayne","nom":"Georges", "nom":"Bruce"}
    playlist_2 = {"nom":"Waine","nom":"charles"}
    numb1 = playlist_1
    numb2 = playlist_2
    if playlist == numb1:
        return playlist_1["nom"]
    elif playlist == numb2:
        return playlist_2["nom"]
show_track('numb1')