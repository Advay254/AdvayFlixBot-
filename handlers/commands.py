from telegram import Update
   from telegram.ext import CallbackContext
   from config import ADMIN_ID, CHANNEL_ID
   from handlers.callbacks import main_menu, admin_menu

   def start_command(update: Update, context: CallbackContext):
       if is_channel_member(update.effective_user.id):
           main_menu(update, context)
       else:
           update.message.reply_text(f"Please join the public channel @channel_username to access the bot.")

   def help_command(update: Update, context: CallbackContext):
       update.message.reply_text("Here are the available commands:\n\n/start - Start the bot\n/help - Get help information")

   def admin_command(update: Update, context: CallbackContext):
       user_id = update.effective_user.id
       if user_id != ADMIN_ID:
           update.message.reply_text("You don't have permission to access the admin menu.")
           return

       admin_menu(update, context)

   def is_channel_member(user_id: int) -> bool:
       # Check if the user is a member of the public channel
       # Implement the logic to check the user's channel membership
       return True
