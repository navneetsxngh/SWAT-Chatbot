## Chatbot (Deployement via AWS)

**Step 1 -> Creating virtual Environement**
```bash
uv venv
```

**Step 2 -> Activate the Virtual Environement**
```bash
.venv/Scripts/activate
```

**Step 3 -> Creating `requirements.txt` to store all our packages**
- streamlit --> For UI
- python-dotenv --> For loading the secret credentials to main file
- google-generativeai --> This is client SDK

**Step 4 -> Installing all the packages**
```bash
uv add -r requirements.txt
```

**Step 5 -> Creating `.env` file for our credentials**

**Step 6 -> Creating `app.py` file for the chatbot layout**

**Step 7 -> Pushing everything to a Github Repo**