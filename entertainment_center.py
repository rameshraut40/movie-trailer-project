import fresh_tomatoes
import media

the_dark_knight_rises = media.Movie ("The Dark Knight Rises",
                         "A fire will rise",
                         "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                         "https://www.youtube.com/watch?v=GokKUqLcvD8" )
#print(the_dark_knight_rises.storyline)

how_to_train_your_dragon = media.Movie ("How to Train Your Dragon",
                      "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself and learns there may be more to the creatures than he assumed",
                      "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                      "https://www.youtube.com/watch?v=i1p51ekrdtI" )

numero_9 = media.Movie ("numero_9",
                        "A rag doll that awakens in a postapocalyptic future holds the key to humanity's salvation.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c9/9posterfinal.jpg",
                        "https://www.youtube.com/watch?v=_qApXdc1WPY")

the_green_mile = media.Movie("The Green Mile", "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.",
                             "https://upload.wikimedia.org/wikipedia/en/c/ce/Green_mile.jpg",
                             "https://www.youtube.com/watch?v=ctRK-4Vt7dA")

goal = media.Movie ("Goal", "The extremely talented Santiago Munez is given a chance at professional football, after being spotted by a scout who has ties with Newcastle United.",
                    "https://upload.wikimedia.org/wikipedia/en/4/47/Goal%212.JPG",
                    "https://www.youtube.com/watch?v=JC5oaVR9QYA")


ace_ventura_pet_detective = media.Movie ("Ace Ventura: Pet Detective",
                                         "A goofy detective specializing in animals goes in search of the missing mascot of the Miami Dolphins.",
                                         "https://upload.wikimedia.org/wikipedia/en/8/84/Ace_ventura_pet_detective.jpg",
                                         "https://www.youtube.com/watch?v=cXcH0f2B2vA",)

movies = [the_dark_knight_rises, how_to_train_your_dragon, numero_9, the_green_mile, goal, ace_ventura_pet_detective]
fresh_tomatoes.open_movies_page(movies)
