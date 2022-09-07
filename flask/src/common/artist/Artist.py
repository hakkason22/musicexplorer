class Artist:
    """アーティストのエンティティ
    """
    def __init__(self,artist) -> None:
        self.__id = artist['id']
        self.name = artist['name']
        self.image = artist['images']

    def get_id(self):
        return self.__id