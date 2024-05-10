from genre import GENRE
from datetime import date

class Song:
    def __init__(self, id, name, artist, duration, release_date, genres=None):
        # Configura los valores iniciales mediante setters para validar entradas.
        self.set_id(id)
        self.set_name(name)
        self.set_artist(artist)
        self.set_duration(duration)
        self.set_release_date(release_date)
        self.set_genres(genres if genres else [])

    def get_id(self):
        # Devuelve el ID de la canción.
        return self._id

    def set_id(self, value):
        # Establece el ID de la canción con validación para asegurar que sea entero.
        if not isinstance(value, int):
            raise ValueError("El ID debe ser un entero")
        self._id = value

    def get_name(self):
        # Devuelve el nombre de la canción.
        return self._name

    def set_name(self, value):
        # Establece el nombre de la canción con validación para asegurar que sea un string.
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto")
        self._name = value

    def get_artist(self):
        # Devuelve el nombre del artista.
        return self._artist

    def set_artist(self, value):
        # Establece el nombre del artista con validación para asegurar que sea un string.
        if not isinstance(value, str):
            raise ValueError("El artista debe ser una cadena de texto")
        self._artist = value

    def get_duration(self):
        # Devuelve la duración de la canción en segundos.
        return self._duration

    def set_duration(self, value):
        # Establece la duración de la canción con validación para asegurar que sea un entero y mayor de 10 segundos.
        if not isinstance(value, int) or value < 10:
            raise ValueError("La duración debe ser un entero y al menos de 10 segundos")
        self._duration = value

    def get_release_date(self):
        # Devuelve la fecha de lanzamiento de la canción.
        return self._release_date

    def set_release_date(self, value):
        # Establece la fecha de lanzamiento con validación para asegurar que no sea una fecha futura.
        if not isinstance(value, date) or value > date.today():
            raise ValueError("La fecha de lanzamiento debe ser hoy o una fecha pasada")
        self._release_date = value

    def get_genres(self):
        # Devuelve la lista de géneros de la canción.
        return list(self._genres)  # se devuelve como lista para cumplir con los casos de prueba

    def set_genres(self, value):
        # Establece los géneros de la canción con validación para asegurar que todos sean instancias del enumerado `Genre`.
        if not all(isinstance(genre, GENRE) for genre in value):
            raise ValueError("Todos los géneros deben ser instancias del enumerado Genre")
        self._genres = set(value)

    def add_genre(self, genre):
        # Añade un género a la canción si aún no está presente.
        if isinstance(genre, GENRE):
            self._genres.add(genre)

    def __eq__(self, other):
        # Define la igualdad basada en el ID de la canción.
        return isinstance(other, Song) and self.get_id() == other.get_id()

    def __str__(self):
        # Representación en cadena de la canción.
        return f"{self.get_artist()} tocando {self.get_name()} durante {self.get_duration()} segundos."


    

  
  
    






def main():
    """Function main of the module.

    The function main of this module is used to test the Class Song.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))


    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()