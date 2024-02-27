#4. Develop a recommendation system using Flask that suggests content to users based on their preferences.

from flask import Flask, render_template, request

app = Flask(__name__)

# Sample content data
content_data = {
    'article1': {'title': 'Article 1', 'tags': ['technology', 'python']},
    'article2': {'title': 'Article 2', 'tags': ['science', 'data']},
    'article3': {'title': 'Article 3', 'tags': ['technology', 'machine learning']}
}

def get_recommendations(user_preferences):
    # Simple content-based filtering
    recommendations = []
    for content_id, content_info in content_data.items():
        if any(tag in user_preferences for tag in content_info['tags']):
            recommendations.append(content_info)
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_preferences = request.form.getlist('preferences')
    recommendations = get_recommendations(user_preferences)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
