import discord
from dhooks import Webhook


print("enter webhook URL: ")
webhook = input("")

hook = Webhook(webhook)

print("enter your message: ")
message = input("")

hook.send(f"{message}")

print("your message has been send, press enter to exit...")
input("")
