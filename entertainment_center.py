import media
import fresh_tomatoes

if __name__ == "__main__":
  #Create a few movie objects
  toy_story = media.Movie("Toy Stroy",
  			"toy story",
  			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  			"https://www.youtube.com/watch?v=vwyZH85NQC4")

  hunger_games = media.Movie("hunger game", 
                             "hunger_games", 
                             "http://img1.wikia.nocookie.net/__cb20150109223445/thehungergames/images/0/09/Mockingjay_part_1_poster_2.jpg",
                             "https://youtu.be/ZL_td1j3BQs")

  se7en = media.Movie("Se7en",
                      "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi.",
                      "http://ia.media-imdb.com/images/M/MV5BMTQwNTU3MTE4NF5BMl5BanBnXkFtZTcwOTgxNDM2Mg@@._V1_SX214_AL_.jpg",
                      "https://youtu.be/J4YV2_TcCoE")

  godFather = media.Movie("The Godfather",
                          "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                          "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
                          "https://youtu.be/sY1S34973zA")

  movies = [toy_story, hunger_games, se7en, godFather]
  fresh_tomatoes.open_movies_page(movies)

