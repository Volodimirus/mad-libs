"""Класс истории"""
import History


class MadLibs:
    """Класс для методов и значений игры"""

    def __init__(self) -> None:
        self._answers: list = []
        self._questions: tuple = [
            "Кто? x1",
            "Кто? x2",
            "Кто? x3",
            "Где?",
            "Кого? (мн.ч)",
        ]
        self._current_history: History = {}
        self._histories: list[History] = [
            {
                "id": 0,
                "title": "Я люблю кошек!",
                "text": "Кошки такие добрые и игривые. В нашей семье есть три кошки. Мы живем $word5$. Первую зовут $word1$, вторую - $word2$, третью - $word3$. Моя любимая кошка - $word1$, после неё идет $word2$, которая любит кусаться, и последняя - $word3$, но она все время спит.Я люблю моих $word4$ и знаю что они любят меня!",
            },
            {
                "id": 1,
                "title": "Youtube kids",
                "text": "Детей $word1$ а потом $word2$ и еще $word3 а так же не помешает $word4$. А вообще $word5$",
            },
            {
                "id": 2,
                "title": "Youtube kids",
                "text": "Детей $word1$ а потом $word2$ и еще $word3 а так же не помешает $word4$. А вообще $word5$",
            },
            {
                "id": 3,
                "title": "Youtube kids",
                "text": "Детей $word1$ а потом $word2$ и еще $word3 а так же не помешает $word4$. А вообще $word5$",
            },
        ]

    def ask_questions(self) -> None:
        """Сохраняет ответы на вопросы в список слов"""

        questions = self.get_questions()
        answers = []

        for question in questions:
            text = input(f"{question} ")
            answers.append(text)

        self.set_answers(answers)

    def get_questions(self) -> list:
        """Получить список ответов"""

        return self._questions

    def make_history(self, title: str, text: str, identificator: int) -> History:
        """Возвращает готовую историю"""

        return {
            "id": identificator + 1,
            "title": title,
            "text": text,
        }

    def add_history_to_list(self, history: list) -> None:
        """Добавляет историю в список"""

        self._histories.append(history)

    def replace_pacifiers(self, history_text: str) -> str:
        """Замена пустышек на ответы"""

        words = self.get_answers()

        # Нужен рефакторинг
        formated_text = (
            history_text.replace("$word1$", words[0])
            .replace("$word2$", words[1])
            .replace("$word3$", words[2])
            .replace("$word4$", words[3])
            .replace("$word5$", words[4])
        )

        return formated_text

    def get_answers(self) -> list:
        """Возвращает список слов"""

        return list(self._answers)

    def set_answers(self, answers: list) -> None:
        """Устанавливает список ответов"""

        self._answers = answers

    def get_histories_list(self) -> list:
        """Возвращает список всех историй"""

        histories_list = self._histories

        return histories_list

    def get_histories_count(self) -> int:
        """Возвращает количество историй"""

        histories_count = len(self._histories)

        return histories_count

    def get_current_history(self) -> History:
        """Получить текущую историю"""

        current_history = self._current_history

        return current_history

    def set_current_history(self, his_id: int) -> None:
        """Установить текущую историю"""

        histories = self.get_histories_list()

        for history in histories:
            if history.get("id") == his_id:
                self._current_history = history

    def get_title(self, history: dict) -> str:
        """Возвращает название истории"""

        history_title = history.get("title")

        return history_title

    def get_text(self, history: dict) -> str:
        """Возвращает текст истории"""

        text = history.get("text")
        text = self.replace_pacifiers(text)

        return text

    def get_history_text(self) -> str:
        """Возвращает текст истории с названием"""

        history = self.get_current_history()
        formated_history = self.get_title(history) + "\n" + self.get_text(history)

        return formated_history


a = MadLibs()
a.ask_questions()
a.set_current_history(0)
print(a.get_history_text())

# a.ask_questions()
# a.set_current_history(0)
# a.replace_pacifiers(
#     "Кошки такие добрые и игривые. В нашей семье есть три кошки. Мы живем $word5$. Первую зовут $word1$, вторую - $word2$, третью - $word3$. Моя любимая кошка - $word1$, после неё идет $word2$, которая любит кусаться, и последняя - $word3$, но она все время спит.Я люблю моих $word4$ и знаю что они любят меня!"
# )
