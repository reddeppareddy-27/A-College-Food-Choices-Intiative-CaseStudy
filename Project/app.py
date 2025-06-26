# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    """
    Renders the home page of the website.
    This page introduces the 'College Food Choices Case Study' project.
    """
    return render_template('index.html')

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    """
    Renders the dashboard page.
    This page serves as a placeholder for an embedded Tableau dashboard,
    explaining how a real dashboard would be integrated and its potential content.
    """
    return render_template('dashboard.html')

# Route for the story page
@app.route('/story')
def story():
    """
    Renders the story page.
    This page serves as a placeholder for an embedded Tableau story,
    describing the narrative flow and types of insights a story would present.
    """
    return render_template('story.html')

# Route for the scenarios page
@app.route('/scenarios')
def scenarios():
    """
    Renders the scenarios page.
    This page details the three main scenarios (Monitoring Nutritional Intake,
    Addressing Dietary Deficiencies, Predictive Analysis) where the data
    analysis from the project would be applied.
    """
    return render_template('scenarios.html')

# Route for the about page
@app.route('/about')
def about():
    """
    Renders the About Us page, providing information about the project's mission and goals.
    """
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    """
    Renders the Contact page, including placeholder contact details and a form.
    """
    return render_template('contact.html')


# Standard boilerplate for running the Flask app
if __name__ == '__main__':
    # Run the Flask app in debug mode.
    # Set debug=True for development to enable auto-reloading and better error messages.
    # In a production environment, debug should be set to False.
    app.run(debug=True)

