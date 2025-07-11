import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

    # ✅ To delete ALL global slash commands:
    await bot.tree.sync()  # Ensure slash command cache is synced
    await bot.http.request(
        discord.http.Route("PUT", "/applications/{application_id}/commands", application_id=bot.user.id),
        json=[]
    )
    print("✅ All global slash commands removed.")

    # 🔁 Optionally: to remove GUILD slash commands only (faster to update)
    # GUILD_ID = 123456789012345678  # Replace with your guild ID
    # await bot.http.request(
    #     discord.http.Route("PUT", "/applications/{application_id}/guilds/{guild_id}/commands",
    #                        application_id=bot.user.id, guild_id=GUILD_ID),
    #     json=[]
    # )
    # print(f"✅ All guild slash commands removed from {GUILD_ID}")

bot.run("YOUR_BOT_TOKEN")
