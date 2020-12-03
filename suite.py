def show_track(playlist):
    """This function is used for show all track in playlist
    :parameter
    playlist : enter your playlist name (string)
    :version
    --------
    specification : Manu Van Hoofstadt (v1 10/11/2020)
    implementation: Manu V.H , Xantin Preser
    """
    playlist_name = './playlist/' + playlist + '.txt'
    playlist = reader(playlist)

    print('Your playlist contains %s music ' + 's' if len(playlist) != 1 + ' : \n' % len(playlist))

    for counter, music in enumerate(playlist):
        music = music.split('/')
    print('%s: %s ' % (counter + 1, music[len(music) - 1][:-len('.mp3')]))