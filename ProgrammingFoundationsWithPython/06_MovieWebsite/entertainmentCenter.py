import media
import fresh_tomatoes


big_hero_6 = media.Movie("Big Hero 6", "A story of a young robotics prodigy named Hiro Hamada who forms a superhero team to combat a masked villain", "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg", "https://www.youtube.com/watch?v=rD5OA6sQ97M")
serenity = media.Movie("Serenity", "Set in 2517, Serenity is the story of the captain and crew of Serenity, a \"Firefly-class\" spaceship. The captain and first mate are veterans of the Unification War, having fought on the losing side. Their lives of petty crime are interrupted by a psychic passenger who harbors a dangerous secret.", "http://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg", "https://www.youtube.com/watch?v=JY3u7bB7dZk")
pokemon_the_first_movie = media.Movie("Pokemon: The First Movie", "A three part film about Pikachu's vacation, Mewtwo's origin, and Mewtwo striking back", "http://upload.wikimedia.org/wikipedia/en/f/f2/Pok%C3%A9mon_The_First_Movie.jpg", "https://www.youtube.com/watch?v=iJjaJjJLfXE")
wreck_it_ralph = media.Movie("Wreck It Ralph", "The film tells the story of the eponymous arcade game villain who rebels against his role and dreams of becoming a hero. He travels between games in the arcade, and ultimately must eliminate a dire threat that could affect the entire arcade, and one that Ralph himself inadvertently started.", "http://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg", "https://www.youtube.com/watch?v=87E6N7ToCxs")
ip_man = media.Movie("Ip Man", "he film focuses on events in Ip's life that supposedly took place in the city of Foshan during the Sino-Japanese War.", "http://upload.wikimedia.org/wikipedia/en/2/2f/Ipmanposter02.jpg", "https://www.youtube.com/watch?v=1AJxXQ7xojE")
shanghai_noon = media.Movie("Shanghai Noon", "A Chinese man who travels to the Wild West to rescue a kidnapped princess. After teaming up with a train robber, the unlikely duo takes on a Chinese traitor and his corrupt boss.", "http://upload.wikimedia.org/wikipedia/en/e/ee/ShanghaiNoon_Poster.jpg", "https://www.youtube.com/watch?v=yE9VSEgV90Y")

movies = [big_hero_6, serenity, pokemon_the_first_movie, wreck_it_ralph, ip_man, shanghai_noon]

# fresh_tomatoes.open_movies_page(movies)
print("module: " + big_hero_6.__module__)
print("name: " + media.Movie.__name__)