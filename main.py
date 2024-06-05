
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of credit cards
credit_cards = [
    {
        "card_number": "1234567890123456",
        "name": "Card A",
        "rewards": "1% cashback on all purchases",
        "fees": "No annual fee",
        "eligibility": "Good credit score (670+)"
    },
    {
        "card_number": "9876543210987654",
        "name": "Card B",
        "rewards": "2% cashback on dining and travel",
        "fees": "Annual fee of $99",
        "eligibility": "Excellent credit score (720+)"
    },
    {
        "card_number": "3456789012345678",
        "name": "Card C",
        "rewards": "3% cashback on gas and groceries",
        "fees": "Annual fee of $49",
        "eligibility": "Good credit score (670+)"
    }
]

# Root route - display the list of credit cards
@app.route("/")
def index():
    return render_template("index.html", credit_cards=credit_cards)

# Route to show details of a specific credit card
@app.route("/card-details/<card_number>")
def card_details(card_number):
    card = next((card for card in credit_cards if card["card_number"] == card_number), None)
    if card is None:
        return "Invalid card number", 404
    return render_template("card-details.html", card=card)

# Route to show the application form for a specific credit card
@app.route("/apply/<card_number>")
def apply(card_number):
    card = next((card for card in credit_cards if card["card_number"] == card_number), None)
    if card is None:
        return "Invalid card number", 404
    return render_template("application-form.html", card=card)

# Route to submit the application form
@app.route("/submit-application", methods=["POST"])
def submit_application():
    card_number = request.form.get("card_number")
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    income = request.form.get("income")

    # Validate the application data
    if not card_number or not name or not email or not phone or not income:
        return "Missing required information", 400
    
    # Submit the application to the bank or credit card provider
    # ... (this logic would typically involve sending the application data to an external API or database)

    return "Application submitted successfully", 200

if __name__ == "__main__":
    app.run(debug=True)
