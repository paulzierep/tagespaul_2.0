script_path = os.path.dirname(os.path.realpath(__file__))
sounds_folder = os.path.join(script_path, "sounds")

###########################
# Download news podcast on startup
###########################


def download_news():
    tpaul_path = os.path.join(sounds_folder, "tagespaul")
    with open(os.path.join(script_path, "youtube_dl_out.txt"), "w") as outfile:
        player = subprocess.Popen(
            [
                "youtube-dl",
                "https://www.deutschlandfunk.de/nachrichten-108.xml",
                "--playlist-items",
                "1",
                "-o",
                f"{tpaul_path}/news.mp3",
            ],
            # stdin=subprocess.PIPE,
            stdout=outfile,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid,  # add id
        )


download_news()
