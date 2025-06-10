crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

def chatbot():
    print("Hey there! I'm CryptoBuddy. Let's find you a green and growing crypto!")
    print("Type something like 'Which crypto is trending up?' or 'What's the most sustainable coin?'\nType 'exit' to leave the chat.\n")

    while True:
        user_query = input("You: ").lower()

        if user_query == "exit":
            print("CryptoBuddy: Stay sharp out there! Remember: Crypto is risky—always do your own research!")
            break

        elif "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: Invest in {recommend}! It's eco-friendly and has long-term potential!")

        elif "trending" in user_query or "rising" in user_query:
            trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if trending:
                print(f"CryptoBuddy: These coins are trending up: {', '.join(trending)}")
            else:
                print("CryptoBuddy: No cryptos are trending up at the moment.")

        elif "long-term" in user_query or "growth" in user_query:
            found = False
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                    print(f"CryptoBuddy: {coin} is trending up and has a top-tier sustainability score!")
                    found = True
                    break
            if not found:
                print("CryptoBuddy: None of the cryptos seem great for long-term growth right now.")

        elif "profitable" in user_query:
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] == "high":
                    print(f"CryptoBuddy: {coin} looks profitable right now!")
                    break
            else:
                print("CryptoBuddy: No clear profitable coin at the moment.")

        else:
            print("CryptoBuddy:I didn't get that. Try asking about sustainability, profitability, or growth.")

chatbot()
