from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "about": "Aspiring full-stack developer with hands-on experience in React, Django, and cloud platforms.",
        "skills": [
            "Python", "C++", "JavaScript (ES6+)", "HTML5", "CSS3", "SCSS",
            "Django", "Tailwind", "React.js", "MongoDB", "SQL",
            "Git", "AWS", "Firebase", "Figma"
        ],
        "projects": [
            {
                "title": "Myntra Review Project",
                "description": "Web app to analyze Myntra reviews using Python, Selenium, and Streamlit dashboards."
            },
            {
                "title": "Sensor Fault Detection",
                "description": "Implemented sensor data validation and diagnostics with Python, enhancing performance."
            }
        ],
        "education": [
            {
                "degree": "B.Tech, Computer Science Engineering",
                "institution": "Maharishi Markandeshwar University",
                "year": "2022 - 2026"
            }
        ],
        "certifications": [
            "Adobe GenSolve Hackathon Round 1 Qualified",
            "GeeksforGeeks: 250+ Problems Solved | 4th Institute Rank"
        ],
        "contact": {
            "email": "sagar@example.com",
            "phone": "+91-9122694325",
            "github": "https://github.com/SagarKumarSah923",
            "linkedin": "https://www.linkedin.com/in/sagar-kumar-sah-36a8a4277/"
        }
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
