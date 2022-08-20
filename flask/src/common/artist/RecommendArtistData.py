class RecommendArtistData:
    """返却するおすすめアーティストのデータ
    """
    def __init__(self,artist) -> None:
        self.id = artist.get_id()
        self.name = artist.name
        self.image = artist.image[1]