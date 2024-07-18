from flask import Flask, render_template, request
import argparse
import csv
from query_processing import get_result_list


app = Flask(__name__)


@app.route('/')
def search_engine_user_interface():
    return render_template('search_engine_user_interface.html')

@app.route('/serp', methods=['POST'])
def show_result_list():#
    try:
        query = request.form.get('query')
    except:
        query = request.get_json().query
    result_list = get_result_list(query)
    print(result_list[0])
    return render_template('serp.html', result_list=result_list, query=query)


def batch_result_list(input_path="queries.txt", output_path="results.txt"):
    output=[]
    with open(input_path, mode="r") as input_file:
        reader = csv.reader(input_file, delimiter="\t")
        for row in reader:
            query = row[1]
            result_list = get_result_list(query)
            for result in result_list:
                output.append({
                    "query_number": row[0],
                    "rank": result["rank"],
                    "link": result["link"],
                    "score": result["score"]
                })

    with open(output_path, mode="w") as output_file:
        writer = csv.writer(output_file, delimiter="\t")
        for o in output:
            writer.writerow([o[
                "query_number"],
                o["rank"],
                o["link"],
                o["score"]
            ])


def main(args=None):
    if args.batchfile:
        batch_result_list()
    else:
        app.run(debug=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--batchfile", action="store_true")
    args = parser.parse_args()
    main(args)