from flask import Flask, render_template, request
import backend

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def results():
    query = request.form['query']
    # query = query.capitalize()
    pos_per, neg_per, neg_tweets, pos_tweets = backend.main(query)

    query = query.capitalize()
    try:
        neut_per = 100 - (pos_per+neg_per)
    except TypeError:
        neut_per = "Not Available"
    if len(pos_tweets)== 0:
        pos_tweets = "Not Available"
    if len(neg_tweets)==0:
        neg_tweets= "Not Available"
    return render_template('results.html',query=query, pos_tweets = pos_tweets,neg_tweets=neg_tweets,
                           pos_per=pos_per,neg_per=neg_per,neut_per=neut_per)

if __name__ == '__main__':
    app.run()
