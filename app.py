from models import db, Projects, app
from flask import (render_template, url_for, request, redirect)

@app.route('/')
def home():
    projects = Projects.query.all()
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about.html')



@app.route('/projects/new', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        github_url = request.form['github_url']
        project = Projects(title=title, description=description, github_url=github_url)
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
        project.date == request.form['date']
        project.description = request.form['description']
        project.github_url = request.form['github_url']
        db.session.commit()
        return redirect(url_for('project', id=id))
    else:
        return render_template('projectform.html', project=project)

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
        Project_1 = Projects(title="Number Guessing Game",
                            date = " December, 2022"  , 
                            description='''This project is a number guessing game where the user is 
                            asked to guess a random number between 1 and 20. The game 
                            provides feedback to the user on whether their guess is too high or too low, 
                            and how many attempts they have made. The user can choose to play the game 
                            multiple times and the program will keep track of their high score
                            (i.e. the lowest number of attempts taken to guess the correct number).''',
                            github_url="https://github.com/maxnhill/Techdegree-Project-1.git", 
                            skills="Python profiency: data types, control structures and exception handling")
        db.session.add(Project_1)
        db.session.commit()
            
        Project_2 = Projects(title="Basketball Game Stats Tool",
                            date = "December, 2022"  , 
                            description='''The program is a data cleaning tool.It begins by cleaning a list of player dictionaries 
                            that contain information such as player names, guardians, experience, and height. 
                            The cleaned list is then used to create balanced teams of six players each. 
                            The program has a function that extracts player names from the teams, and another 
                            function that displays statistics for a selected team. ''',
                            github_url="https://github.com/maxnhill/Techdegree-Treehouse-Project-2.git", 
                            skills="Python profiency: data types, functions, and command-line interfaces")
        db.session.add(Project_2)
        db.session.commit()
        
        Project_3 = Projects(title="Hangman Game",
                            date = " January, 2023"  , 
                            description='''This code defines a Hangman game that uses phrases as the words to be guessed. 
                                            It starts by displaying a welcome message, explaining the rules, and selecting a 
                                            random phrase from a list. The player then guesses letters to complete the phrase
                                            and the game continues until the player correctly guesses the phrase or exceeds the 
                                            maximum number of incorrect guesses. The player can choose to play again or exit the game. ''',
                            github_url="https://github.com/maxnhill/Techdegree-Project-3.git", 
                            skills='''Python profiency: data types, functions, and control structures.
                                        Object-oriented programming (OOP)''')
        db.session.add(Project_3)
        db.session.commit()

        Project_4 = Projects(title="Store Inventory with SQLAlchemy",
                            date = " February, 2023"  , 
                            description='''The project is a simple inventory management system that allows users to view 
                                            and add products to a database. The code uses Python and SQLite to manage the database, 
                                            and SQLAlchemy is used as an ORM to interact with the database. ''',
                            github_url="https://github.com/maxnhill/Techdegree-Project-4.git", 
                            skills='''Python profiency, Object-Oriented Programming (OOP), 
                                        SQL, Database management, Data cleaning, and Version control ''')
        db.session.add(Project_4)
        db.session.commit()
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')

