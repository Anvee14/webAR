from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict = {
                "1": ["Black", "Gorilla", "Dancing", "Madagascar", "Nice", "White", "Tigers", "Move"],
                "2": ["Sunday", "Aunt", "Dog", "Burgers", "Soft Drinks", "Nice", "Cards"],
                "3": ["Smelly", "Cat", "California", "Cat", "Blue", "3", "Fishes", "Dance", "Songs", "Sad", "Childishly", "Happy"]
        }

stories = [
    {
        "inputs": 8,
        "title": "Let's Go to the Zoo",
        "story": 'Today we went to the zoo! The first thing we saw was a <span class="rep_input">_____</span> <span class="rep_input">_____</span> <span class="rep_input">_____</span>. The zookeeper told us that was normal, except in <span class="rep_input">_____</span>. I had a <span class="rep_input">_____</span> time! Next time, I will remember that if I ever see <span class="rep_input">_____</span> <span class="rep_input">_____</span>, I should <span class="rep_input">_____</span> the other way.',
        "words": ["Black", "Gorilla", "Dancing", "Madagascar", "Nice", "White", "Tigers", "Move"],
        "story_id": "1"
    },
    {
        "inputs": 7,
        "title": "Picnic Time",
        "story": 'On <span class="rep_input">_____</span> we are going on a picnic! I\'m going with my <span class="rep_input">_____</span> and my favourite pet <span class="rep_input">_____</span>. For lunch, we will eat <span class="rep_input">_____</span> and drink <span class="rep_input">_____</span>. We will end the day with a <span class="rep_input">_____</span> game of <span class="rep_input">_____</span>.',
        "words": ["Sunday", "Aunt", "Dog", "Burgers", "Soft Drinks", "Nice", "Cards"],
        "story_id": "2"
    },
    {
        "inputs": 12,
        "title": "Silly Animal Tale",
        "story": 'There once was a <span class="rep_input">_____</span> <span class="rep_input">_____</span> from <span class="rep_input">_____</span>. Nobody knew he was a <span class="rep_input">_____</span> because he had <span class="rep_input">_____</span> fur and ate <span class="rep_input">_____</span> <span class="rep_input">_____</span> each day. He liked to <span class="rep_input">_____</span> and sing <span class="rep_input">_____</span>. Whenever he was <span class="rep_input">_____</span>, he would start speaking <span class="rep_input">_____</span>. Then he would feel <span class="rep_input">_____</span>.',
        "words": ["Smelly", "Cat", "California", "Cat", "Blue", "3", "Fishes", "Dance", "Songs", "Sad", "Childishly", "Happy"],
        "story_id": "3"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-story")
def get_story():
    return jsonify({
        "status": "success",
        "story": random.choice(stories)
    })

@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer_dict.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)