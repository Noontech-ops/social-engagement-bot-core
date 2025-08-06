# Social Engagement Bot Core

Automate your social media engagement!  
This Python backend monitors Twitter or LinkedIn (with API), drafts tone-aware replies using OpenAI GPT, flags high-priority messages, and exposes all data for dashboard visualization.

## Features

- Polls Twitter (Tweepy) or LinkedIn for mentions, DMs.
- Drafts personalized responses via GPT (OpenAI API).
- Flags high-priority messages (simple ML/rules).
- Stores thread/message status in MongoDB.
- Event-driven: easy to deploy on AWS Lambda + Step Functions.
- REST API for dashboard data.

## Architecture

```
[Twitter/LinkedIn] 
   ↓
[Python Agent: main.py]
   ↔ [MongoDB: state_manager.py]
   ↓
[OpenAI GPT: gpt_drafter.py]
   ↓
[API: FastAPI in main.py]
   ↓
[Dashboard (React)]
```

## Setup

1. `git clone https://github.com/yourhandle/social-engagement-bot-core.git`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in your secrets.
4. Run locally: `python src/main.py`
5. Deploy to AWS with `aws/` templates (Lambda, Step Functions).

## Configuration

- `.env`:  
  - TWITTER_API_KEY, TWITTER_API_SECRET
  - LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET
  - OPENAI_API_KEY
  - MONGODB_URI

## Contributing

Open source, modular, privacy-first. PRs welcome!

## License

MIT
