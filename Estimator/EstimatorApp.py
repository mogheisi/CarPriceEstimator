import re
from unidecode import unidecode
from sklearn import tree

from .models import Car


class Estimator:
    def __init__(self, brand, name, model, kilometer):
        self.name = name
        self.model = model
        self.brand = brand
        self.kilometer = kilometer
        x = []
        y = []

        for line in Car.objects.all():
            found = re.search(name, line.name)
            if found:
                kilometer = re.sub(',', '', unidecode(line.kilometer))
                price = re.sub(',', '', unidecode(line.price))
                x.append((unidecode(line.model), kilometer))
                y.append(price)

                clf = tree.DecisionTreeClassifier()
                clf.fit(x, y)

                model = model
                kilometers = kilometer

                new_data = [[unidecode(kilometers), unidecode(model)]]
                self.answer = clf.predict(new_data)
