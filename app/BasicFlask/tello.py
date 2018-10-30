from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    user = {'username':'Jinal'}
    posts = [
        {
            'author':{'username':'Daniel'},
            'body':'He is her lobster'
        },
        {
            'author':{'username':'Amar'},
            'body':'They don\'t know that we know they know we know'
        }
    ]
    return render_template('tmp.html',user=user,posts=posts)
        
    

if __name__ == "__main__":
    app.run(debug=True)

