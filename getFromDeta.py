from deta import Deta
import dotenv
import os

def getFromDetabase():
    dotenv.load_dotenv()

    # initialize with a project key
    deta = Deta(os.getenv("YOUR_PROJECT_KEY"))

    photos = deta.Drive("podcasts")

    name_of_podcast = "BryanJohnson(#388).mp3"

    large_file = photos.get(name_of_podcast)

    with open(name_of_podcast, "wb+") as f:
      for chunk in large_file.iter_chunks(4096):
          f.write(chunk)
      large_file.close()


