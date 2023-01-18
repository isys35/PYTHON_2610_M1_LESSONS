def avg(ranks):
    assert len(ranks) != 0, "Список не может быть пустым"
    return round(sum(ranks) / len(ranks), 2)


ranks = [62, 65, 75]
print("Среднее значение:", avg(ranks))
