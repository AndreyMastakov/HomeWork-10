import json


def load_candidates():
    """Открытие списка кандидатов и преобразование его в словарь"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i
    return candidates
