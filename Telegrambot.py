from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler, MessageHandler, ContextTypes, filters

BOT_KEY = "8517783536:AAFowIeR_l7SapE6tIAzW9yxNJHa_K_eqI4"



class Movie:
    def __init__(self, name: str, year: str, genre: str, rating: str, director: str,):
        self.name = name
        self.year = year
        self.genre = genre
        self.rating = rating
        self.director = director
    def __str__(self):
        return f"🎬Movie: {self.name}\n📅Year: {self.year}\n🎞️Genre: {self.genre}\n🍿Rating: {self.rating}\n🎥Director: {self.director}"

DATA = {
    "avengers endgame": Movie("Avengers: Endgame", "2019", "Action, Adventure, Sci-Fi", "8.4/10", "Anthony Russo, Joe Russo"),
    "avengers infinity war": Movie("Avengers: Infinity War", "2018", "Action, Adventure, Sci-Fi", "8.4/10", "Anthony Russo, Joe Russo"),
    "iron man": Movie("Iron Man", "2008", "Action, Sci-Fi", "7.9/10", "Jon Favreau"),
    "captain america": Movie("Captain America: The First Avenger", "2011", "Action, Adventure, Sci-Fi", "6.9/10", "Joe Johnston"),
    "thor": Movie("Thor", "2011", "Action, Adventure, Fantasy", "7.0/10", "Kenneth Branagh"),
    "spider man": Movie("Spider-Man", "2002", "Action, Adventure, Sci-Fi", "7.4/10", "Sam Raimi"),
    "spider man no way home": Movie("Spider-Man: No Way Home", "2021", "Action, Adventure, Sci-Fi", "8.2/10", "Jon Watts"),
    "batman": Movie("The Batman", "2022", "Action, Crime, Drama", "7.8/10", "Matt Reeves"),
    "joker": Movie("Joker", "2019", "Crime, Drama, Thriller", "8.3/10", "Todd Phillips"),
    "avatar": Movie("Avatar", "2009", "Action, Adventure, Fantasy", "7.9/10", "James Cameron"),
    "avatar way of water": Movie("Avatar: The Way of Water", "2022", "Action, Adventure, Fantasy", "7.5/10", "James Cameron"),
    "titanic": Movie("Titanic", "1997", "Drama, Romance", "7.9/10", "James Cameron"),
    "jurassic park": Movie("Jurassic Park", "1993", "Adventure, Sci-Fi", "8.2/10", "Steven Spielberg"),
    "transformers": Movie("Transformers", "2007", "Action, Sci-Fi", "7.0/10", "Michael Bay"),
    "mission impossible": Movie("Mission: Impossible", "1996", "Action, Thriller", "7.2/10", "Brian De Palma"),
    "top gun maverick": Movie("Top Gun: Maverick", "2022", "Action, Drama", "8.2/10", "Joseph Kosinski"),
    "fast and furious": Movie("The Fast and the Furious", "2001", "Action, Crime", "6.8/10", "Rob Cohen"),
    "john wick": Movie("John Wick", "2014", "Action, Thriller", "7.4/10", "Chad Stahelski"),
    "the matrix": Movie("The Matrix", "1999", "Action, Sci-Fi", "8.7/10", "Lana Wachowski, Lilly Wachowski"),
    "inception": Movie("Inception", "2010", "Action, Sci-Fi, Thriller", "8.8/10", "Christopher Nolan"),
    "interstellar": Movie("Interstellar", "2014", "Adventure, Drama, Sci-Fi", "8.7/10", "Christopher Nolan"),
    "oppenheimer": Movie("Oppenheimer", "2023", "Biography, Drama, History", "8.2/10", "Christopher Nolan"),
    "the dark knight": Movie("The Dark Knight", "2008", "Action, Crime, Drama", "9.0/10", "Christopher Nolan"),
    "home alone": Movie("Home Alone", "1990", "Comedy, Family", "7.7/10", "Chris Columbus"),
    "toy story": Movie("Toy Story", "1995", "Animation, Adventure, Comedy", "8.3/10", "John Lasseter"),
    "finding nemo": Movie("Finding Nemo", "2003", "Animation, Adventure, Comedy", "8.2/10", "Andrew Stanton"),
    "the lion king": Movie("The Lion King", "1994", "Animation, Adventure, Drama", "8.5/10", "Roger Allers, Rob Minkoff"),
    "frozen": Movie("Frozen", "2013", "Animation, Adventure, Comedy", "7.4/10", "Chris Buck, Jennifer Lee"),
    "coco": Movie("Coco", "2017", "Animation, Adventure, Family", "8.4/10", "Lee Unkrich"),
    "kung fu panda": Movie("Kung Fu Panda", "2008", "Animation, Action, Adventure", "7.6/10", "Mark Osborne, John Stevenson"),
    "the hangover": Movie("The Hangover", "2009", "Comedy", "7.7/10", "Todd Phillips"),
    "home alone 2": Movie("Home Alone 2: Lost in New York", "1992", "Comedy, Family", "6.9/10", "Chris Columbus"),
    "spider man": Movie("Spider-Man", "2002", "Action, Adventure, Sci-Fi", "7.4/10", "Sam Raimi"),
    "spider man 2": Movie("Spider-Man 2", "2004", "Action, Adventure, Sci-Fi", "7.5/10", "Sam Raimi"),
    "spider man 3": Movie("Spider-Man 3", "2007", "Action, Adventure, Sci-Fi", "6.3/10", "Sam Raimi"),
    "the amazing spider man": Movie("The Amazing Spider-Man", "2012", "Action, Adventure, Sci-Fi", "6.9/10", "Marc Webb"),
    "the amazing spider man 2": Movie("The Amazing Spider-Man 2", "2014", "Action, Adventure, Sci-Fi", "6.6/10", "Marc Webb"),
    "spider man homecoming": Movie("Spider-Man: Homecoming", "2017", "Action, Adventure, Sci-Fi", "7.4/10", "Jon Watts"),
    "spider man far from home": Movie("Spider-Man: Far From Home", "2019", "Action, Adventure, Sci-Fi", "7.4/10", "Jon Watts"),
    "spider man no way home": Movie("Spider-Man: No Way Home", "2021", "Action, Adventure, Sci-Fi", "8.2/10", "Jon Watts"),
    "spider man brand new day": Movie("Spider-Man: Brand New Day", "2026", "Action, Adventure, Sci-Fi", "N/A", "Destin Daniel Cretton"),
    "taxi driver": Movie("Taxi Driver", "1976", "Crime, Drama", "8.2/10", "Martin Scorsese"),
    "scarface": Movie("Scarface", "1983", "Crime, Drama", "8.3/10", "Brian De Palma"),
    "the godfather": Movie("The Godfather", "1972", "Crime, Drama", "9.2/10", "Francis Ford Coppola"),
    "the godfather part 2": Movie("The Godfather Part II", "1974", "Crime, Drama", "9.0/10", "Francis Ford Coppola"),
    "the godfather part 3": Movie("The Godfather Part III", "1990", "Crime, Drama", "7.6/10", "Francis Ford Coppola"),
    "goodfellas": Movie("Goodfellas", "1990", "Biography, Crime, Drama", "8.7/10", "Martin Scorsese"),
    "barbie": Movie("Barbie", "2023", "Adventure, Comedy, Fantasy", "6.8/10", "Greta Gerwig"),
} 
async def starts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬Hello, Welcome to Bunheng Movie bot!!!\nPlease enter your movie name.")
    
         
async def reply_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = update.message.text.strip().lower()
    info = DATA.get(movie)

    if info:
        await update.message.reply_text(str(info))
    else :
        await update.message.reply_text(f"❌ Sorry the movie {update.message.text} may not be in our data.")

app = ApplicationBuilder().token(BOT_KEY).build()
app.add_handler(CommandHandler("start", starts))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_movie))
app.run_polling()