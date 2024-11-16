class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
movie = Movie("Super Mario", 2023, False, 10.0, 120)
print(f"Filme {movie.name} é de {movie.yearLaunch} e possui nota {movie.note}")


class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}" ' ' f"Ano:{self.yearLaunch}"

movie = Movie("Super Mario", 2023, False, 10.0, 120)
print(movie)
print(f"Filme {movie.name} é de {movie.yearLaunch} e possui nota {movie.note}")
print(movie)