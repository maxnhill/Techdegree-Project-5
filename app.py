from models import db, Projects, app
from flask import (render_template, url_for, request, redirect)


@app.route('/')
def home():
    return render_template('index.html')

def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        github_url = request.form['github_url']
        project = Projects(title=title, description=description, github_url=github_url)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('about.html'))
    else:
        return render_template('projectform.html')

@app.route('/pet/<id>')
def project(id):
    project = Projects.query.get_or_404(id)
    return render_template('detail.html', project=project)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Projects.query.get_or_404(id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.github_url = request.form['github_url']
        db.session.commit()
        return redirect(url_for('about.html'))
    else:
        return render_template('edit_project.html', project=project)

@app.route('/delete/<id>')
def delete_project(id):
    project = Projects.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('projects'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404

if __name__ == '__main__':
    with app.app_context():
         db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')

