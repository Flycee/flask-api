from flask import Flask, render_template, request, redirect

app = Flask(__name__)

con_list = []


@app.route("/", methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        content = request.form['i_text']
        con_list.append(content)
        return redirect('/')
    else:
        return render_template("index.html", list=con_list)

@app.route("/delete")
def del_list():
    con_list.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
