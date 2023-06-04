from flask import Flask, render_template, request
from model import Model

app = Flask(__name__)
app.secret_key = "wjddusdlek@!!@wjddusdlek!!"

M = Model()

@app.route("/")
def index():
    print("hello")
    return render_template("base.html")


@app.route("/upload_done", methods={"GET"})
def upload_done():
    url = request.args.get("url")
    M.setUrl(url)
    input = M.subtitle()
    output = M.summarize()
    return render_template('base.html', input=input, output=output)
    # return render_template('base.html', output=output)

@app.route("/qa_done", methods={"GET"})
def qa_done():
    question = request.args.get("question")
    M.setQuestion(question)
    answer = M.QA()
    return render_template('base.html', question=question, answer=answer, input=M.input, output=M.output)
    # return render_template('base.html', output=output)

if __name__=='__main__':
    app.run(debug=True)
