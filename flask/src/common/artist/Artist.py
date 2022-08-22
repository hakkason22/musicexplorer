class Artist:
    """アーティストのエンティティ
    """
    def __init__(self,id,name,image) -> None:
        self.__id = id
        self.name = name
        self.image = image

    def get_id(self):
        return self.__id