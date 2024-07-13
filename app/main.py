from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def search_engine_user_interface():
    return render_template('search_engine_user_interface.html')

@app.route('/serp', methods=['POST'])
def get_result_list():#
    try:
        query = request.form.get('query')
    except:
        query = request.get_json().query
    print(query)
    result_list = [{"link": "https://d3rlpy.readthedocs.io/en/v2.5.0/", "title": "d3rlpy - An offline deep reinforcement learning library", "content": "d3rlpy provides state-of-the-art offline deep reinforcement learning algorithms through out-of-the-box scikit-learn-style APIs. Unlike other RL libraries, the provided algorithms can achieve extremely powerful performance beyond their papers via several tweaks."},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de. Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de. Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},]
    return render_template('serp.html', result_list=result_list, query=query)


if __name__ == '__main__':
    app.run(debug=True)