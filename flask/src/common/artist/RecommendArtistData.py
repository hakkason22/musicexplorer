class RecommendArtistData:
    """返却するおすすめアーティストのデータ
    """
    def __init__(self,artist) -> None:
        self.id = artist.get_id()
        self.name = artist.name
        if not artist.image:
            self.image = artist.image
        else:
            self.image = artist.image[1]