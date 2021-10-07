import requests

parameters = {
    "amount": 20,
    "type": "boolean",
    # "difficulty": "medium",
    "category": 18
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]

# Difficulties: "easy", "medium", "hard"

# Categories: 9-General Knowledge, 10-Books, 11-Films, 12-Music,
# 13-Musicals/Theatre, 14-TV, 15-Video Games, 16-Board Games,
# 17-Science&Nature, 18-Computers, 19-Mathematics, 20-Mythology,
# 21-Sports, 22-Geography, 23-History, 24-Politics, 25-Art,
# 26-Celebrities, 27-Animals, 28-Vehicles, 29-Comics, 30-Gadgets,
# 31-Anime/Manga, 32-Cartoon/Animation