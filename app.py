from flask import Flask, request, jsonify, render_template, send_from_directory
import recipe_builder
import os

app = Flask(__name__)

@app.route('/css/<path:filename>')
def serve_static(filename):
    print(filename)
    root_dir = os.path.dirname(os.getcwd())
    cssfile = os.path.join(root_dir, 'Recipe-Builder', 'templates', 'static', 'css')
    print(cssfile)
    return send_from_directory(cssfile, filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    searchreq = request.form['search-bar']
    ingredience = recipe_builder.list_create(searchreq)
    resippy = recipe_builder.readme("recipic.csv")
    print(resippy)
    res = recipe_builder.search(ingredience, resippy)
    return render_template('Recipe_builder_page2.html', recipes=res)

if __name__ == "__main__":
    app.run()

