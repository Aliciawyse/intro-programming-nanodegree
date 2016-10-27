# Assignment: Create instances of the class Movie 
import fresh_tomatoes
import media


#Create a new instance the class movie. This calss is called toy story
toy_story = media.Movie('Toy Story', 'Story about a boy and his toys', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie("Avatar", "A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

arrival = media.Movie('Arrival', 'A linguistics expert talks to aliens', 'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg', 'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

robo_cop = media.Movie('Robo Cop', 'A human cop becomes a robot cop', 'https://upload.wikimedia.org/wikipedia/en/thumb/1/16/RoboCop_%281987%29_theatrical_poster.jpg/220px-RoboCop_%281987%29_theatrical_poster.jpg', 'https://www.youtube.com/watch?v=FnRJ0r0eivk')

martian = media.Movie('The Martian', 'A man gets left behind on mars.', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg', 'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

mummy = media.Movie('The Mummy', 'An ancient egyptian priest is accidently resurrected', 'https://upload.wikimedia.org/wikipedia/en/thumb/6/68/The_mummy.jpg/220px-The_mummy.jpg', 'https://www.youtube.com/watch?v=h3ptPtxWJRs')

#print(toy_story.storyline)
#print avatar.storyline
#avatar.show_trailer()
#print arrival.storyline

#movies = [toy_story, avatar,arrival, robo_cop, martian, mummy]
#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS