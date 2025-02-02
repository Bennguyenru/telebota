# Telegram Transaction Dashboard

## Features
- Upload a CSV of transactions
- Get a real-time summary (deposits, withdrawals, balance, processing time)

## Setup
```bash
pip install -r requirements.txt
python app.py
```

## Deployment (Heroku)
```bash
git init
git add .
git commit -m "Initial commit"
heroku create
heroku git:remote -a your-app-name
git push heroku main
```

Your app will be live at `https://your-app-name.herokuapp.com`.
