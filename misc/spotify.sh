# dbus-send  --print-reply --session --type=method_call --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri "string:spotify:album:4sb0eMpDn3upAFfyi4q2rw" 
# dbus-send  --print-reply --session --type=method_call --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri "string:spotify:track:03bYLN5H3OjZ6CIpBcd4W3#0:0.01" 

#https://open.spotify.com/playlist/37i9dQZF1E8RBUeV6TqpJT?si=2d9cc42731d542fc
#https://open.spotify.com/track/7FGho3Adev1y2hTB949PGv?si=1ad06816eb154a9a

# uri=spotify:playlist/37i9dQZF1E8RBUeV6TqpJT?si=2d9cc42731d542fc # We are going to use this variable to access the metadata for the album.
# song=$(curl -G "http://ws.spotify.com/lookup/1/?uri=$uri&extras=track" | grep -E -o "spotify:track:[a-zA-Z0-9]+" -m 1) # Get the first track of the Album. We are going to use this variable in next line.
# dbus-send  --print-reply --session --type=method_call --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause && dbus-send  --print-reply --session --type=method_call --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri "string:spotify:episode:0yzeKEXLEf3MUqXxEeGa5F?si=334676ef5b914999#0:0.01" # Pause the player and the play the first song of the album

#https://open.spotify.com/show/1OLcQdw2PFDPG1jo3s0wbp?si=c5f2c4cf8d754689

# http://ws.spotify.com/lookup/1/?uri=spotify:show:1OLcQdw2PFDPG1jo3s0wbp?si=c5f2c4cf8d754689&extras=track

# https://open.spotify.com/episode/0yzeKEXLEf3MUqXxEeGa5F?si=334676ef5b914999
# dbus-send  --print-reply --session --type=method_call --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri "string:spotify:episode:0yzeKEXLEf3MUqXxEeGa5F?si=334676ef5b914999#0:0.10" 

# qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri spotify:show:1OLcQdw2PFDPG1jo3s0wbp #festundflauschig
# qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri spotify:playlist:37i9dQZF1E8RBUeV6TqpJT #playlist
qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.OpenUri spotify:show:4eYPgoQH9VLTfgAxIbwHqs #nachrichten
# https://open.spotify.com/episode/0yzeKEXLEf3MUqXxEeGa5F?si=0f90d9dbc5744e9e