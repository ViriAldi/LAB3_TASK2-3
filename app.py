from flask import Flask, render_template, request
import mapping_twitter


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        name = request.form['name']
        map_tw = mapping_twitter.last_map_creator(name)
        return map_tw

    return render_template('choser.html')


if __name__ == "__main__":
    app.run(debug=True)