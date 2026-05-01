# Discord Bot Starter Structure

A simple, ready-to-extend Discord bot structure built with `discord.py`. It includes automatic cog loading, slash command syncing, YAML-based configuration, log file handling, and a starter `/ping` command so you can get a bot online quickly without rebuilding the same base setup every time.

This was originally a personal private project that I created much earlier for my own use. I have now decided to make it public because it can be beneficial for other people too. The goal is simple: save time by giving you a clean bot foundation that is already wired up and ready for custom commands, cogs, and features.

## Features

- Discord bot powered by `discord.py`
- YAML configuration through a generated `config.yml`
- Automatic loading of all files inside the `cogs/` folder
- Slash command syncing on startup
- Admin-only prefix commands for syncing, loading, unloading, and reloading cogs
- Runtime logs saved in the `Logs/` folder
- Automatic dependency check/install helper
- Example `/ping` slash command included

## Project Structure

```text
.
+-- cogs/
|   +-- ping.py              # Example slash command cog
+-- utils/
|   +-- Colors.py            # Console color constants
|   +-- PackageHandler.py    # Dependency checker/installer
|   +-- config.py            # Config loader and validator
+-- main.py                  # Bot entry point
+-- requirements.txt         # Python dependencies
+-- README.md
```

## Requirements

- Python 3.10 or newer recommended
- A Discord bot application and token
- Discord privileged intents enabled if your bot needs them

The current dependencies are listed in `requirements.txt`:

```text
discord.py==2.4.0
pyaml==24.12.1
```

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment.

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

The bot also checks for missing packages at startup and installs them from `requirements.txt` if needed, but installing requirements manually first is recommended.

## Discord Bot Setup

1. Go to the Discord Developer Portal:

```text
https://discord.com/developers/applications
```

2. Create a new application.
3. Open the **Bot** section and create a bot.
4. Copy the bot token.
5. Enable the intents your bot requires. This project currently uses `discord.Intents.all()`, so enable privileged intents if you plan to use features that need them.
6. Invite the bot to your server from the **OAuth2 > URL Generator** page.
7. Select:

- `bot`
- `applications.commands`

Recommended bot permissions depend on your own commands. For testing, you can start with Administrator in a private test server, then reduce permissions before using it publicly.

## Configuration

On first run, the bot creates `config.yml` in the project root if it does not already exist. You can then edit it to match your bot:

```yaml
# Your discord bot token get it by creating an application at https://discord.com/developers/applications
TOKEN: 'YOUR_BOT_TOKEN_HERE'

# Prefix is for the discord bot prefixed commands, such as !help
PREFIX: '!'
```

Important:

- Keep your bot token private.
- Do not commit `config.yml` if it contains a real token.
- If `config.yml` is missing or invalid, the project will create or reset it with default values.

## Running The Bot

After installing dependencies and configuring your token, run:

```bash
python main.py
```

If everything is configured correctly, the console will show that the bot is online and slash commands have been synced.

## Included Commands

### Slash Commands

| Command | Description |
| --- | --- |
| `/ping` | Shows the bot latency. |

### Prefix Commands

These commands use the prefix from `config.yml`, such as `!sync` when `PREFIX` is `!`.

| Command | Description |
| --- | --- |
| `sync` | Syncs all slash commands. Requires administrator permission. |
| `loadcog <name>` | Loads a specific cog. Requires administrator permission. |
| `loadcog` | Loads all cogs. Requires administrator permission. |
| `unloadcog <name>` | Unloads a specific cog. Requires administrator permission. |
| `unloadcog` | Unloads all cogs. Requires administrator permission. |
| `reloadcog <name>` | Reloads a specific cog. |

## Adding New Cogs

Create a new Python file inside the `cogs/` folder. For example:

```text
cogs/example.py
```

Use this basic structure:

```python
from discord.ext import commands
from discord import app_commands
import discord


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Says hello.")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")


async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
```

Restart the bot, or use the reload/load cog commands if the bot is already running.

## Logs

Logs are written to:

```text
Logs/latest.log
```

When the bot starts, an existing `latest.log` is renamed with a timestamp, and a fresh `latest.log` is created for the new session.

## Troubleshooting

### LoginFailure or wrong token error

Check that:

- `TOKEN` in `config.yml` is correct.
- The token belongs to the bot application you invited.
- The file format is valid YAML.

### Slash commands are not showing

Try:

- Running the bot again and waiting for command sync to finish.
- Using the prefix sync command, for example `!sync`.
- Confirming the bot was invited with the `applications.commands` scope.

### Cogs are not loading

Check that:

- The file is inside the `cogs/` folder.
- The file ends with `.py`.
- The cog has an `async def setup(bot)` function.
- There are no import or syntax errors in the cog.

## Notes For Public Use

This project is intentionally lightweight. It is meant to be a starting structure, not a finished all-purpose bot. You can build your own moderation commands, utility commands, database logic, API integrations, dashboards, or automation features on top of it.

Before deploying publicly, review permissions, intents, error handling, and token storage for your own use case.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
