from deta import Deta
import dotenv
import os


def uploadToDeta():
    dotenv.load_dotenv()

    # initialize with a project key
    deta = Deta(os.getenv("YOUR_PROJECT_KEY"))

    photos = deta.Drive("podcasts")

    name_of_podcast = "BryanJohnson(#388).mp3"

    # where you store your music files
    path = "music/BryanJohnson(#388).mp3"

    photos.put("BryanJohnson(#388).mp3", path=path)

    print("Finished Uploading")


