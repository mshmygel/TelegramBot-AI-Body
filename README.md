# Telegram Bot
This is a Telegram bot built with Aiogram and Together API.

✅To test the bot, go to telegram. @mshmygeltgbot

This project is a Telegram bot that integrates with Together API for AI-based responses. The bot allows users to interact with AI, register, and use various features through simple commands.

## Features

- **AI Interaction**: Users can ask the AI by sending prompts, and the bot will respond with the AI's answer.
- **User Registration**: Users can register by sharing their contact information.
- **Media Handling**: The bot can handle photos and send media as responses.
- **Custom Keyboard**: Inline and regular keyboards for interacting with the bot.

### Commands

- `/start`: Displays the main menu and bot information.
- `/help`: Provides help information about the bot.
- **Ask AI**: Users can ask the AI by typing "🧠 Ask AI Body" and sending a prompt.
- **Register**: Users can register by pressing "📝 Register" and sharing their contact info.
- **How are you?**: Responds with a simple "OK!".
- **Get photo**: Sends a predefined image.

### Example Flow
1. **User sends** `/start`.
2. **Bot replies** with a menu of available options.
3. User can select:
   - **"🧠 Ask AI Body"** to input a prompt and get an AI response.
   - **"📝 Register"** to share contact information and register.

## Technologies Used

- **Python 3.12**: The core language used to build the bot.
- **Aiogram**: An asynchronous Python framework to interact with the Telegram Bot API.
- **Together API**: An AI service used for generating responses based on prompts.
- **Poetry**: Dependency management tool.
- **Docker**: For creating a containerized environment.
- **Railway**: Platform for deploying the bot online.
- **dotenv**: For managing environment variables securely.

## Running Locally

To run the bot locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/TelegramBot-AI-Body.git
    cd TelegramBot-AI-Body
    ```

2. **Set up the environment**:
    - Install dependencies using `Poetry`:
        ```bash
        poetry install
        ```
    - Create a `.env` file in the root directory and add your tokens:
        ```plaintext
        TOKEN=your-telegram-bot-token
        TOGETHER_API_KEY=your-together-api-key
        ```

3. **Run the bot**:
    ```bash
    poetry run python run.py
    ```

The bot will now be running locally and can be tested by sending messages to it on Telegram.

## Deploying to Railway

To deploy the bot to Railway:

1. **Create a new project** on Railway (or log in to your existing Railway account).
2. **Connect your GitHub repository** with Railway.
3. **Set environment variables** on Railway:
    - `TOKEN`
    - `TOGETHER_API_KEY`

4. **Deploy the bot** using Railway's interface.
   - Select the **Deploy** tab.
   - Railway will automatically build the bot and start it.

The bot will now be hosted and accessible via Telegram at any time.

## Troubleshooting

- **Bot is not responding**: Ensure your API keys are correctly set in the `.env` file and Railway environment variables.
- **Deployment fails**: Check the build logs in Railway for any dependency or configuration issues.

