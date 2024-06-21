from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def search_engine_user_interface():
    return render_template('search_engine_user_interface.html')

@app.route('/serp', methods=['POST'])
def get_result_list():#
    query = request.form.get('query')
    print(query)
    result_list = [{"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de. Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de. Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
                   {"link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "title": "ILIAS Uni Tübingen", "content": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},]
    return render_template('serp.html', result_list=result_list, query=query)


if __name__ == '__main__':
    app.run(debug=True)