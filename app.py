from flask import Flask, render_template, request
import config
import openai

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/recipe-generator', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        query_1 = request.form['ingredientDescription1']
        query_2 = request.form['ingredientDescription2']

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Write a recipe for {} and {}.".format(query_1, query_2),
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )

        prompt = 'AI Suggestions for {} and {} are:'.format(query_1, query_2)
        openAIAnswer = response

    return render_template('recipe-generator.html', **locals())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
