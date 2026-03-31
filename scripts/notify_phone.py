import os
import requests

def send_shared_access_ping(game_title):
    # This script sends a push notification to your S24 Ultra
    payload = {
        "title": "🛰️ Feebz Hub: Shared Access Granted",
        "body": f"System linked to {game_title}. Optimization complete. Insert into Feebz!",
        "priority": "high"
    }
    print(f"Pushing notification for: {game_title}")

# Auto-trigger for the last added game
send_shared_access_ping("Whispering Eons #0")
