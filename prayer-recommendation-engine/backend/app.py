from flask import Flask, request, jsonify
from verse_recommender import get_recommended_verse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    feeling = data.get('feeling', '')
    verse = get_recommended_verse(feeling)
    return jsonify({'verse': verse})

if __name__ == '__main__':
    app.run(debug=True)
