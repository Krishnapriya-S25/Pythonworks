class Movie:
    title:str
    rating:int
    run_time:int
    director:str
    genre:str

    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre
    def display_movie(self):
        
        print(self.title,self.rating,self.run_time,self.director,self.genre)

        
movie_instance1=Movie()

movie_instance2=Movie()

movie_instance1.set_movie("ARM",9.5,"2h30m","ACBN","mystery")

movie_instance2.set_movie("KGF",10,"2h30m","vbnc","Action")

movie_instance1.display_movie()

movie_instance2.display_movie()



