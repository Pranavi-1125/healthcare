import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

# Your website information
website_info = """
The virtual health assistant powered by AI is a comprehensive platform designed to cater to both physical and mental healthcare needs for patients, caregivers, and medical professionals. This website provides an intuitive and interactive interface to help users efficiently manage their health by tracking vital health metrics, setting medication reminders, scheduling appointments, and accessing mental health support. Alongside routine healthcare management, the platform includes features such as mindfulness exercises, stress management techniques, mood tracking, and access to virtual counseling or mental health resources. These tools ensure users can address their emotional well-being alongside physical health.

For caregivers, the assistant automates reminders and progress monitoring, while medical professionals can efficiently manage patient records, appointment scheduling, and therapy plans. With a strong emphasis on holistic care, secure data handling, and personalized recommendations, the virtual health assistant is an all-in-one solution to promote better health outcomes, both physically and mentally.
"""

# Function to get chatbot response
def chatbot_response(user_query):
    # Use the `website_info` variable in the prompt
    prompt = f"You are a chatbot that answers questions based on this information: {website_info} User question: {user_query}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# API endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
