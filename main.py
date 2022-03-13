from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_candidates()


@app.route("/")
def page_index():
    """Создания списка кандидатов для роута в формате (тег <pre>)"""
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f'{candidate["name"]} \n{candidate["position"]} \n{candidate["skills"]} \n\n'
    str_candidates += '</pre>'
    return str_candidates


@app.route("/candidates/<int:id>")
def profile(id):
    """Создание отдельной страницы для каждого кандидата с изображением"""
    candidate = candidates[id]
    str_candidates = f'<img src={candidate["picture"]}></img> <br><br>{candidate["name"]} <br>{candidate["position"]}' \
                     f' <br>{candidate["skills"]} <br><br>'
    return str_candidates


@app.route("/skills/<skill>")
def skills(skill):
    """Поиск кандидатов по их навыкам"""
    str_candidates = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_candidates += f'{candidate["name"]} \n{candidate["position"]} \n{candidate["skills"]} \n\n'
    str_candidates += '</pre>'
    return str_candidates


app.run()
