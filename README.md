## Flask Application Design for Credit Card Comparison and Application

### HTML Files

- **index.html:** Main page for comparing credit cards, displaying a list of cards with their features and benefits.
- **card-details.html:** Page for viewing the details of a specific credit card, including its rewards, fees, and eligibility criteria.
- **application-form.html:** Page for submitting an application for a selected credit card, collecting necessary personal and financial information.

### Routes

- **`/`**: Renders the `index.html` page, displaying the comparison of credit cards.
- **`/card-details/<card_number>`**: Renders the `card-details.html` page, passing the specified `card_number` as a parameter to display details of that particular card.
- **`/apply/<card_number>`**: Renders the `application-form.html` page, passing the specified `card_number` as a parameter to prefill the form with the selected card's information.
- **`/submit-application`**: Receives the submitted application data from the `application-form.html` page, validates the data, and initiates the application process by sending the information to the bank or credit card provider for review.