from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
     from handlers.commands import start_command, help_command, admin_command
     from handlers.callbacks import main_menu, movies_menu, anime_menu, categories_menu, request_content, how_to_download
     from handlers.files import handle_file
     from config import Config

     def main():
         updater = Updater(Config.BOT_TOKEN, use_context=True)
         dp = updater.dispatcher

         # Command handlers
         dp.add_handler(CommandHandler("start", start_command))
         dp.add_handler(CommandHandler("help", help_command))
         dp.add_handler(CommandHandler("admin", admin_command))

         # Callback query handlers
         dp.add_handler(CallbackQueryHandler(main_menu, pattern='^main_menu$'))
         dp.add_handler(CallbackQueryHandler(movies_menu, pattern='^movies_menu$'))
         dp.add_handler(CallbackQueryHandler(anime_menu, pattern='^anime_menu$'))
         dp.add_handler(CallbackQueryHandler(categories_menu, pattern='^categories_menu$'))
         dp.add_handler(CallbackQueryHandler(request_content, pattern='^request_content$'))
         dp.add_handler(CallbackQueryHandler(how_to_download, pattern='^how_to_download$'))

         # Message handlers
         dp.add_handler(MessageHandler(Filters.document | Filters.video, handle_file))

         updater.start_polling()
         updater.idle()

     if __name__ == '__main__':
         main()
