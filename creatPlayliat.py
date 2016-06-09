import os
'''
this python script get all the mp3 file names and list it in an 'm3u8' file to be used as a playlist for most music plyers

this is my favorite way to mange my songs and playlists, I put the files in folders and use this to create the m3u8 file
'''

s = ""
for file in os.listdir(os.getcwd()):
    if file.endswith('.mp3'):
        s+= file + "\n"

playlist = open('playlistName.m3u8', 'w')

playlist.write(s)



