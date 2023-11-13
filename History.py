class History:
    """Класс для методов и информации о истории"""

    def __init__(self, his_id: int, title: str, text: str):
        self._id = his_id
        self._title = title
        self._text = text

    def get_id(self):
        "Получить ID истории"

        return self._id

    def get_title(self):
        """Получить название истории"""

        return self._title

    def get_text(self):
        """Получить содержание истории"""

        return self._text

    def get_history(self):
        """Получить объект с информацией о истории"""

        return {"id": self.get_id(), "title": self.get_title(), "text": self.get_text()}
