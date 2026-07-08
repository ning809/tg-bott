import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 从环境变量读取 Token（更安全）
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GROUP_LINK = "https://t.me/SK1fy0td4W42MGZi"
ADMIN_INFO = "@wangzai00666"

REPLY_TEXT = f"""
👥 欢迎加入我们的群组！

🔗 群链接：{GROUP_LINK}
👤 管理员：{ADMIN_INFO}

点击链接即可加入，如有疑问请联系管理员。
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REPLY_TEXT)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REPLY_TEXT)

def main():
    if not BOT_TOKEN:
        raise ValueError("请在 Render 环境变量中设置 BOT_TOKEN")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("机器人已启动...")
    app.run_polling()

if __name__ == "__main__":
    main()