# 🤖 AI Voice Sales Bot

A Python-based conversational AI sales assistant that uses speech recognition and text-to-speech to have natural voice conversations with customers.

## ✨ Features

- **Voice Recognition** - Understands customer queries using Google Speech Recognition
- **Text-to-Speech** - Responds naturally with pyttsx3
- **Intent Detection** - Identifies customer needs (pricing, features, trials, purchases, support)
- **Conversation Logging** - Tracks all conversations for analysis
- **Error Handling** - Gracefully handles audio and API errors
- **Customizable Responses** - Easy to modify sales scripts and pricing

## 📋 Requirements

- Python 3.7+
- Microphone and speaker
- Internet connection (for Google Speech Recognition API)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/manojsmpr2006-debug/ai-voice-sales-bot.git
cd ai-voice-sales-bot
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

**Note for PyAudio installation:**
- **Windows**: `pip install pipwin` then `pipwin install pyaudio`
- **Mac**: `brew install portaudio` then `pip install pyaudio`
- **Linux**: `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

## 💻 Usage

Run the bot:
```bash
python main.py
```

The bot will greet you and start listening. Speak naturally about:
- **Pricing**: "What's the price?" or "How much does it cost?"
- **Features**: "What features do you offer?" or "What services?"
- **Trial**: "Do you have a free trial?" or "Can I get a demo?"
- **Purchase**: "I want to buy" or "How do I subscribe?"
- **Support**: "I need help" or "Do you have support?"

To exit, say: "bye", "exit", "quit", or "goodbye"

## 📝 Customization

### Edit Sales Responses
Open `main.py` and modify the `responses` dictionary:

```python
self.responses = {
    "price": "Your custom price message",
    "features": "Your custom features message",
    # ... etc
}
```

### Add New Intent Categories
1. Add to `responses` dictionary
2. Add keywords to `keywords` dictionary
3. The bot will automatically detect and respond

Example:
```python
self.responses["warranty"] = "We offer a 12-month warranty on all plans."
self.keywords["warranty"] = ["warranty", "guarantee", "protected"]
```

### Adjust Speech Settings
```python
self.engine.setProperty('rate', 150)  # Speed (50-200)
self.engine.setProperty('volume', 0.9)  # Volume (0.0-1.0)
```

## 📊 Conversation Logs

All conversations are logged to `sales_bot.log`:
```
2026-05-27 14:22:09 - INFO - User said: What is the price?
2026-05-27 14:22:10 - INFO - Bot response: Our premium plan starts at 499 rupees only. Would you like to know more?
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **"No module named 'pyaudio'"** | Install portaudio first (see Installation section) |
| **"No microphone detected"** | Check microphone permissions and connections |
| **"Could not understand audio"** | Speak clearly and reduce background noise |
| **"API error"** | Check internet connection for Google Speech API |
| **Bot speaks too fast/slow** | Adjust `engine.setProperty('rate', value)` |

## 🎯 Future Enhancements

- [ ] Integration with OpenAI GPT for smarter responses
- [ ] Database storage for customer data
- [ ] Email confirmation for purchases
- [ ] Multi-language support
- [ ] Sentiment analysis
- [ ] Integration with CRM systems
- [ ] Conversation analytics dashboard

## 📄 License

MIT License - Feel free to use and modify

## 👨‍💻 Author

Created by manojsmpr2006-debug

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For issues and questions, please open an issue on GitHub or contact manojsmpr2006@gmail.com

---

**Happy Selling! 🎉**
