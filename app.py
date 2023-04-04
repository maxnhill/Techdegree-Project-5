from models import db, Projects, app
from flask import (render_template, url_for, request, redirect)
from formatdate import format_date

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'



@app.route('/')
def home():
    projects = Projects.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        skills = request.form['skills']
        description = request.form['desc']
        github_url = request.form['github']
        project = Projects(title = title, date = date, description = description, skills = skills, github_url = github_url)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('projectform.html')


@app.route('/projects/<id>')
def project(id):
    project = Projects.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Projects.query.get_or_404(id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.skills = request.form['skills']
        project.description = request.form['desc']
        project.github_url = request.form['github']
        project.date = request.form['date']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editproject.html', project=project)



@app.route('/projects/<id>/delete')
def delete_project(id):
    project = Projects.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('home'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        project_1 = Projects(title="Number Guessing Game",
                                date = format_date("December, 2022" ), 
                                description='''This project is a number guessing game where the user is 
                                asked to guess a random number between 1 and 20. The game 
                                provides feedback to the user on whether their guess is too high or too low, 
                                and how many attempts they have made. The user can choose to play the game 
                                multiple times and the program will keep track of their high score
                                (i.e. the lowest number of attempts taken to guess the correct number).''',
                                github_url="https://github.com/maxnhill/Techdegree-Project-1.git", 
                                skills="Python, Data types, Control structures, Exception handling")
        
                
        project_2 = Projects(title="Basketball Game Stats Tool" ,
                        date = format_date("December, 2022") , 
                        description='''The program is a data cleaning tool. It begins by cleaning a list of player dictionaries 
                        that contain information such as player names, guardians, experience, and height. 
                        The cleaned list is then used to create balanced teams of six players each. 
                        The program has a function that extracts player names from the teams, and another 
                        function that displays statistics for a selected team. ''',
                        github_url="https://github.com/maxnhill/Techdegree-Treehouse-Project-2.git", 
                        skills="Python, Data Cleaning, Functions")


        project_3 = Projects(title="Hangman Game",
                        date = format_date("January, 2023") , 
                        description='''This code defines a Hangman game that uses phrases as the words to be guessed. 
                                        It starts by displaying a welcome message, explaining the rules, and selecting a 
                                        random phrase from a list. The player then guesses letters to complete the phrase
                                        and the game continues until the player correctly guesses the phrase or exceeds the 
                                        maximum number of incorrect guesses. The player can choose to play again or exit the game. ''',
                        github_url="https://github.com/maxnhill/Techdegree-Project-3.git", 
                        skills="Python, Object-oriented programming (OOP), Datetime")


        project_4 = Projects(title="Store Inventory with SQLAlchemy",
                    date = format_date("February, 2023") , 
                    description='''The project is a simple inventory management system that allows users to view 
                                    and add products to a database. The code uses Python and SQLite to manage the database, 
                                    and SQLAlchemy is used as an ORM to interact with the database. ''',
                    github_url="https://github.com/maxnhill/Techdegree-Project-4.git", 
                    skills="Python, Datetime, Object-oriented programming (OOP), Structured Query Langnguage(SQL), Version control")
        
    
        my_projects = [project_1,project_2, project_3, project_4 ]
        for project in my_projects:
            existing_project = Projects.query.filter_by(title=project.title).first()
            if existing_project is None:
                db.session.add(project)
                db.session.commit()
        db.create_all()
        app.run(debug=True, port=8000, host='127.0.0.1')
        

