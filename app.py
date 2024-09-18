from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Zen Quotes
zen_quotes = [
    "Simplicity is the ultimate sophistication.",
    "Wherever you go, there you are.",
    "The quieter you become, the more you can hear.",
    "Tension is who you think you should be. Relaxation is who you are.",
    "Let go or be dragged.",
]

# Compliments
compliments = [
    "You're looking great today!",
    "You're a smart cookie!",
    "You have impeccable manners.",
    "You light up the room.",
    "You are enough just as you are.",
]

# Mood Palettes
mood_palettes = {
    "happy": ["#FFD700", "#FF4500", "#FF6347", "#98FB98", "#F0E68C"],
    "calm": ["#B0E0E6", "#4682B4", "#87CEFA", "#ADD8E6", "#F0FFFF"],
    "sad": ["#708090", "#2F4F4F", "#A9A9A9", "#778899", "#696969"],
    "angry": ["#FF0000", "#8B0000", "#B22222", "#DC143C", "#CD5C5C"],
    "creative": ["#7B68EE", "#6A5ACD", "#4B0082", "#8A2BE2", "#9400D3"],
}

# Emoji Translator Dictionary
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "star": "⭐",
    "cool": "😎"
}

# Nouns, Verbs, Adjectives for Gibberish Generator
nouns = ["cat", "pizza", "cloud", "banana", "moon"]
verbs = ["eats", "jumps over", "runs to", "talks with", "flies above"]
adjectives = ["fuzzy", "delicious", "strange", "wild", "bright"]
prepositions = ["on", "under", "beside", "through", "between"]


# Routes for each mini-app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zen_timer')
def zen_timer():
    return jsonify(random.choice(zen_quotes))

@app.route('/compliment_mirror')
def compliment_mirror():
    return jsonify(random.choice(compliments))

@app.route('/mood_palette', methods=['POST'])
def mood_palette():
    mood = request.json.get('mood', 'happy')
    palette = mood_palettes.get(mood, ["#FFFFFF", "#000000"])
    return jsonify(palette)

@app.route('/emoji_translator', methods=['POST'])
def emoji_translator():
    sentence = request.json.get('sentence', '')
    words = sentence.split()
    translated_sentence = " ".join([emoji_dict.get(word, word) for word in words])
    return jsonify(translated_sentence)

@app.route('/decision_wheel', methods=['POST'])
def decision_wheel():
    options = request.json.get('options', [])
    choice = random.choice(options) if options else "No options provided"
    return jsonify(choice)

@app.route('/gibberish_generator')
def gibberish_generator():
    sentence = f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(prepositions)} the {random.choice(adjectives)} {random.choice(nouns)}."
    return jsonify(sentence)


if __name__ == '__main__':
    app.run(debug=True)
