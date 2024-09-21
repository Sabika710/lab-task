class Movie_Budget:
    def __init__(self):
        self.movies = [
            ("Eternal Sunshine of the Spotless Mind", 20000000),
            ("Memento", 9000000),
            ("Requiem for a Dream", 4500000),
            ("Pirates of the Caribbean: On Stranger Tides", 379000000),
            ("Avengers: Age of Ultron", 365000000),
            ("Avengers: Endgame", 356000000),
            ("Incredibles 2", 200000000)
        ]
        self.Avg_budget=0
    
    def avg_budget(self):
        budget = sum(movie[1] for movie in self.movies)
        
        self.Avg_budget = budget/len(self.movies)
        return f"average budget is  {self.Avg_budget}"
    
    def High_budget(self):
        high_budget = []
        
        for movie in self.movies:
            if movie[1] > self.Avg_budget:
                print(f"{movie[0]} is high on budget")
                high_budget.append(movie)
        
obj= Movie_Budget()
obj.avg_budget()
obj.High_budget()     