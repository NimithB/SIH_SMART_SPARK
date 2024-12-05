from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="Google api key")
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_input():
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""{request.form.get("user_input")} Give precise and small answers."""
    genairesponse = model.generate_content(prompt)

    response = f"{genairesponse.text}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)