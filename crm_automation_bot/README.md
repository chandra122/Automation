# CRM Automation Bot

An AI-powered automation bot for open-source CRM systems. This bot helps automate common CRM tasks and provides intelligent insights about customer interactions.

## Features

- Contact management automation
- Task creation and assignment
- AI-powered contact interaction analysis
- Scheduled automation tasks
- Integration with popular open-source CRM systems

## Prerequisites

- Python 3.8 or higher
- Access to a CRM system with API capabilities
- API credentials for the CRM system

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/crm-automation-bot.git
cd crm-automation-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the environment template and configure your settings:
```bash
cp .env.example .env
```

4. Edit the `.env` file with your CRM credentials and configuration.

## Usage

1. Start the bot:
```bash
python crm_bot.py
```

2. The bot will automatically:
   - Connect to your CRM system
   - Run scheduled tasks
   - Analyze contact interactions
   - Create and update tasks as needed

## Configuration

The bot can be configured through environment variables in the `.env` file:

- `CRM_URL`: Your CRM system's base URL
- `CRM_API_KEY`: API key for authentication
- `OPENAI_API_KEY`: API key for AI services (if using)
- `SCHEDULED_TASKS_ENABLED`: Enable/disable scheduled tasks
- `CONTACT_ANALYSIS_INTERVAL`: How often to analyze contacts (in hours)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 