# Read the file and count the frequency of each word
with open("30 days/days19/obama_speech.txt", "r") as f:
    data = f.read()
words = data.split()
word_count = {}
print(words)    
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)      

#finds the ten most spoken languages
import json
with open("30 days/days19/countries_data.json", "r") as f:
    countries = json.load(f)
language_count = {}
for country in countries:
    for language in country["languages"]:
        language_count[language] = language_count.get(language, 0) + 1
most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Most spoken languages:")
for language, count in most_spoken:
    print(f"- {language}: {count}")

#finds the ten most populated countries
most_populated = sorted(countries, key=lambda x: x["population"], reverse=True)[:10]
populated_countries = [(country["name"], country["population"]) for country in most_populated]
print("Top 10 most populated countries:")
for name, population in populated_countries:
    print(f"- {name}: {population}")
