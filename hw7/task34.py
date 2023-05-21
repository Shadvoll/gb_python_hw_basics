# фраза разделяются пробелами
# число слогов в каждой фразе одинаково
# число слогов равно числу гласных

# phrases = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.lower().strip().split()
phrases = input("Стихотворение Винни: ").lower().strip().split()
vowel_letters = 'УЕАОЭЯИЮЁ'.lower()
syllables = [0] * len(phrases)
for idx, phrase in enumerate(phrases):
    for vowel_letter in vowel_letters:
        syllables[idx] += phrase.count(vowel_letter)
if all([phrase_syllable == syllables[0] for phrase_syllable in syllables]):
    print("Парам пам-пам")
else:
    print("Пам парам")

