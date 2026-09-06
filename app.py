from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# -----------------------------
# 100 Travel Questions
# -----------------------------
qa_pairs = {

"best places in india": "Top places in India include Goa, Manali, Kerala, Jaipur, and Ladakh.",
"best beaches in india": "Popular beaches are Baga Beach, Calangute, Radhanagar Beach, and Marina Beach.",
"best hill stations in india": "Shimla, Manali, Ooty, Darjeeling, and Munnar are famous hill stations.",
"places to visit in goa": "Baga Beach, Fort Aguada, Dudhsagar Falls, and Anjuna Beach.",
"places to visit in manali": "Solang Valley, Rohtang Pass, Hadimba Temple.",
"places to visit in mumbai": "Gateway of India, Marine Drive, Elephanta Caves.",
"places to visit in delhi": "Red Fort, India Gate, Qutub Minar, Lotus Temple.",
"places to visit in jaipur": "Hawa Mahal, Amber Fort, City Palace.",
"places to visit in kerala": "Munnar, Alleppey, Thekkady, Kovalam.",
"places to visit in ladakh": "Pangong Lake, Nubra Valley, Magnetic Hill.",

"best international destinations": "Dubai, Bali, Singapore, Thailand, Maldives.",
"best time to visit dubai": "November to March is ideal for Dubai.",
"best time to visit bali": "April to October is best.",
"cheapest countries to travel": "Thailand, Vietnam, Nepal, Sri Lanka are affordable.",
"how to apply passport": "Apply online through Passport Seva website and schedule appointment.",
"how to apply visa": "Apply through respective country embassy or online visa portal.",
"budget trip to maldives": "Book early flights and stay in guesthouses.",
"visa for thailand": "Indian citizens can get visa on arrival in Thailand.",
"is singapore expensive": "Yes, Singapore is relatively expensive compared to India.",
"best places in europe": "Paris, Rome, Switzerland, Amsterdam.",

"how to book cheap flights": "Book early, compare prices and travel off-season.",
"cheapest way to travel": "Use public transport and budget airlines.",
"how to plan budget trip": "Set budget, compare hotels, and avoid peak season.",
"best time to book flights": "Book 1-2 months before travel.",
"student travel discounts": "Many airlines and railways offer student discounts.",
"how to save money while travelling": "Stay in hostels and use public transport.",
"is train cheaper than flight": "Generally yes for short distances.",
"travel during off season benefits": "Lower prices and fewer crowds.",
"hotel discount tips": "Use comparison websites and promo codes.",
"best flight booking websites": "MakeMyTrip, Goibibo, Skyscanner.",

"what to pack for trip": "Clothes, ID proof, charger, medicines and toiletries.",
"what to pack for beach": "Sunscreen, swimwear, sunglasses, hat.",
"what to pack for hill station": "Warm clothes, gloves, jackets.",
"travel essentials": "Passport, wallet, charger, tickets.",
"documents required for travel": "Aadhar card, passport for international.",
"luggage weight limit": "Usually 15-25kg depending on airline.",
"how to avoid overpacking": "Pack only essentials and mix-match clothes.",
"international travel checklist": "Passport, visa, forex, tickets.",
"travel backpack tips": "Choose lightweight and waterproof backpack.",
"how much cash to carry": "Carry limited cash and use cards."
}

# -----------------------------
# CLEAN USER TEXT
# -----------------------------
def clean_text(text):

    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    ignore = ["what","is","are","the","tell","me","about","please","can","you"]

    words = text.split()
    words = [w for w in words if w not in ignore]

    return words

# -----------------------------
# FIND BEST MATCH
# -----------------------------
def find_best_match(user_words):

    best_score = 0
    best_answer = None

    for question, answer in qa_pairs.items():

        q_words = question.split()

        score = 0

        for word in q_words:
            if word in user_words:
                score += 1

        if score > best_score:
            best_score = score
            best_answer = answer

    return best_answer, best_score


# -----------------------------
# FLASK ROUTES
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html").read()


@app.route("/get", methods=["POST"])
def chatbot_response():

    user_message = request.form["msg"]

    user_words = clean_text(user_message)

    answer, score = find_best_match(user_words)

    if score > 0:
        return jsonify(answer)

    return jsonify("Sorry, I don't have information about that.")


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
