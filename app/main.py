from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def search_engine_user_interface():
    return render_template('search_engine_user_interface.html')

@app.route('/serp', methods=['POST'])
def get_result_list():
    return "Implement retrieval of result list."


if __name__ == '__main__':
    app.run(debug=True)