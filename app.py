from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    q = request.json["question"]

    if "html" in q.lower():
        answer = "HTML هي لغة تستخدم لبناء صفحات الويب 🌐"
    elif "tag" in q.lower():
        answer = "الـ Tag هو عنصر زي <p> أو <div>"
    else:
        answer = "اسألني عن HTML 😊"

    return jsonify({"answer": answer})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)