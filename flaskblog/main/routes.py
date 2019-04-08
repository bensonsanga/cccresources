from flask import render_template, request, Blueprint
from flaskblog.models import Post
from .data import *

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/entourage")
def entourage():
    return render_template('entourage.html', title='Entourage', articles=articles)


@main.route("/new_article")
def new_article():
    return render_template('new_article.html', title='New Article')


@main.route("/tutorials")
def tutorials():
    return render_template('tutorials.html', title='Tutorials', videos=videos)


@main.route("/tutorial001")
def tutorial001():
    return render_template('001.html', title='Tutorial001')


@main.route("/new_tutorials")
def new_tutorials():
    return render_template('new_tutorials.html', title='New Tutorials')


@main.route("/dwg")
def dwg():
    return render_template('dwg.html', title='Dwg')


@main.route("/new_dwg")
def new_dwg():
    return render_template('new_dwg.html', title='New File')


@main.route("/scripts")
def scripts():
    return render_template('scripts.html', title='Scripts')


@main.route("/models")
def models():
    return render_template('models.html', title='Models')


@main.route("/search")
def search():
    return render_template('search.html', title='Search')


@main.route("/search1")
def search1():
    return render_template('search1.html', title='Search1')


@main.route("/search2")
def search2():
    return render_template('search2.html', title='Search2')


@main.route("/icons")
def icons():
    return render_template('icons.html', title='Projects')


@main.route("/new_project")
def new_project():
    return render_template('new_project.html', title='New Project')


@main.route("/maps")
def maps():
    return render_template('maps.html', title='Maps')


@main.route("/map1")
def map1():
    return render_template('map.html', title='Brzezin')


@main.route("/map2")
def map2():
    return render_template('map2.html', title='lodz botanic garden')


@main.route("/map3")
def map3():
    return render_template('map3.html', title='lodz Piotrkowska Street')


@main.route("/sketchmap")
def sketchmap():
    return render_template('sketchmap.html', title='Map Sketch')


@main.route("/sketch3d")
def sketch3d():
    return render_template('sketch3d.html', title='3D Map Sketch')


@main.route("/map01")
def map01():
    return render_template('arcgis/map01.html', title='Map 3D')


@main.route("/map4")
def map4():
    return render_template('map4.html', title='Piotrkowska Street')
