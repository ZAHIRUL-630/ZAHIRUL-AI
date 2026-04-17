import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def chat():
    # ইউজার যা লিখেছে সেটা ধরবে
    user_msg = request.args.get('text', '')
    
    # প্রশ্ন-উত্তরের লিস্ট
    if "কেমন" in user_msg:
        return "আমি ভালো আছি, জহিরুল ইসলাম ভাই!"
    elif "নাম" in user_msg:
        return "আমার নাম জহিরুল আই।"
    elif "তৈরি" in user_msg or "বানিয়েছে" in user_msg:
        return "আমাকে তৈরি করেছেন জহিরুল ইসলাম।"
    else:
        return "আমি আপনার কথা বুঝতে পারছি না, দয়া করে জহিরুল ইসলাম ভাইকে জিজ্ঞেস করুন।"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
