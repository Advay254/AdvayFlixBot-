from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
   from telegram.ext import CallbackContext
   from config import ADMIN_ID, SUBSCRIPTION_PRICE

   def main_menu(update: Update, context: CallbackContext):
       keyboard = [[InlineKeyboardButton("🎬 Movies", callback_data='movies_menu'),
                   InlineKeyboardButton("📺 Anime Series", callback_data='anime_menu')],
                  [InlineKeyboardButton("🔍 Search", callback_data='search'),
                   InlineKeyboardButton("📁 Categories", callback_data='categories_menu')],
                  [InlineKeyboardButton("📩 Request Content", callback_data='request_content'),
                   InlineKeyboardButton("❓ How to Download", callback_data='how_to_download')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text("Welcome to AdvayFlix! Please select an option from the main menu:", reply_markup=reply_markup)

   def movies_menu(update: Update, context: CallbackContext):
       keyboard = [[InlineKeyboardButton("🆕 Latest Uploads", callback_data='latest_movies'),
                   InlineKeyboardButton("⭐ Popular", callback_data='popular_movies')],
                  [InlineKeyboardButton("🎭 Genres", callback_data='movie_genres'),
                   InlineKeyboardButton("📅 Year", callback_data='movie_year')],
                  [InlineKeyboardButton("↩️ Back", callback_data='main_menu')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text("Movies Menu:", reply_markup=reply_markup)

   def anime_menu(update: Update, context: CallbackContext):
       keyboard = [[InlineKeyboardButton("📺 Ongoing Series", callback_data='ongoing_anime'),
                   InlineKeyboardButton("✅ Completed Series", callback_data='completed_anime')],
                  [InlineKeyboardButton("🎬 Anime Movies", callback_data='anime_movies'),
                   InlineKeyboardButton("🎭 Anime Genres", callback_data='anime_genres')],
                  [InlineKeyboardButton("↩️ Back", callback_data='main_menu')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text("Anime Menu:", reply_markup=reply_markup)

   def categories_menu(update: Update, context: CallbackContext):
       keyboard = [[InlineKeyboardButton("🎭 Action", callback_data='action'),
                   InlineKeyboardButton("❤️ Romance", callback_data='romance')],
                  [InlineKeyboardButton("🔪 Horror", callback_data='horror'),
                   InlineKeyboardButton("🤣 Comedy", callback_data='comedy')],
                  [InlineKeyboardButton("🌟 Adventure", callback_data='adventure'),
                   InlineKeyboardButton("🎭 Drama", callback_data='drama')],
                  [InlineKeyboardButton("↩️ Back", callback_data='main_menu')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text("Categories Menu:", reply_markup=reply_markup)

   def request_content(update: Update, context: CallbackContext):
       # Implement the request content functionality
       pass

   def how_to_download(update: Update, context: CallbackContext):
       # Implement the how to download functionality
       pass
