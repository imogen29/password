import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

passwords = {
    "黎檼": "0625", "赫紃": "0625", "岳絚": "0625", "項譎": "0625",
    "陖錚": "1129", "溫瀿": "1129", "李昶": "1129", "沈塱": "1129", "願懷": "1129", "凌諽": "1129",
    "鞠宥": "6035", "瀤裫": "6035",
}

@bot.event
async def on_ready():
    print(f"✅ Bot 已上線：{bot.user}")

@bot.command()
async def 密碼(ctx, 角色名: str):
    password = passwords.get(角色名)
    if password:
        try:
            await ctx.author.send(f"🔐 **{角色名}** 的密碼是：`{password}`")
            await ctx.message.add_reaction("📬")
        except discord.Forbidden:
            await ctx.send("❌ 我無法私訊你，請開啟伺服器成員私訊。")
    else:
        await ctx.send(f"❓ 查無「{角色名}」的密碼。")

bot.run("MTM4ODk0MTkxNjA3ODM0NjQ2Mg.GYr816.DtSp0CBtCOcoI823S5wPoO9QGH580Yp-EhP6UQ")
print(f"Token: {token}")  # 測試有沒有拿到token

keep_alive.keep_alive()
bot.run(token)
