class VideoItem:

    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:

    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if rating < 0 or rating > 5 or not isinstance(rating, int):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = rating
