from modelos.avaliacao import Evaluation

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._ative = False
        self._evaluation = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    @property
    def ative(self):
        return "ativo ⌧" if self._ative else "desativado ☐"

    @classmethod 
    def list_restaurants(cls):
        print(f"{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} |{"Status"}")
        for restaurant in cls.restaurants:
              print(f"{restaurant._name.ljust(20)} | {restaurant._category.ljust(20)} | {str(restaurant.average_evaluation).ljust(25)}  |{restaurant.ative}")

    def toggle_state(self):
        self._ative = not self._ative

    def receive_evaluation(self, client, note):
        if 0 <= note <= 5:
            evaluation = Evaluation(client, note)
            self._evaluation.append(evaluation)

    @property
    def average_evaluation(self):
        if not self._evaluation:
            return "-"
        sum_of_grades = sum(evaluation._note for evaluation in self._evaluation)
        quantity_of_notes = len(self._evaluation)
        average = round(sum_of_grades/quantity_of_notes, 1)
        return average