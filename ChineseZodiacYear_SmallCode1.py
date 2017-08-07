"""
ChineseZodiacYear_SmallCode1.py

To come up with a solution to display a list of numbers from a tuple in written format using commas and "and".

For testing, input numbers from 0 to 11. Use 10 for longer output.
"""

animals = [
    ("monkey",
     {"description" : "Those born under the Chinese Zodiac sign of the Monkey thrive on having fun. \
They’re energetic, upbeat, and good at listening but lack self-control. They like being active and \
stimulated and enjoy pleasing self before pleasing others. They’re heart-breakers, not good at long-term \
relationships, morals are weak. Compatible with Rat or Dragon.",
      "luckynumbers" : (1, 7, 8),
      "unluckynumbers" : (2, 5, 9)}),  
    ("rooster",
     {"description" : "Those born under the Chinese Zodiac sign of the Rooster are practical, resourceful, \
observant, analytical, straightforward, trusting, honest, perfectionists, neat and conservative. Compatible \
with Ox or Snake.",
      "luckynumbers" : (5, 7, 8),
      "unluckynumbers" : (1, 3, 9)}),  
    ("dog",
     {"description" : "Those born under the Chinese Zodiac sign of the Dog are loyal, \
faithful, honest, distrustful, often guilty of telling white lies, temperamental, prone \
to mood swings, dogmatic, and sensitive. Dogs excel in business but have trouble finding mates. \
Compatible with Tiger or Horse.",
      "luckynumbers" : (3, 4, 9),
      "unluckynumbers" : (1, 6, 7)}),  
    ("boar",
     {"description" : "Those born under the Chinese Zodiac sign of the Pig are extremely nice, good-mannered \
and tasteful. They’re perfectionists who enjoy finer things but are not perceived as snobs. They enjoy helping \
others and are good companions until someone close crosses them, then look out! They’re intelligent, always \
seeking more knowledge, and exclusive. Compatible with Rabbit or Goat.",
      "luckynumbers" : (2, 5, 8),
      "unluckynumbers" : (1, 3, 9)}),  
    ("mouse",
     {"description" : "Those born under the Chinese Zodiac sign of the Rat are quick-witted, clever, charming, \
sharp and funny. They have excellent taste, are a good friend and are generous and loyal to others considered part \
of its pack. Motivated by money, can be greedy, is ever curious, seeks knowledge and welcomes challenges. Compatible \
with Dragon or Monkey.",
      "luckynumbers" : (2, 3),
      "unluckynumbers" : (5, 9)}),  
    ("ox",
     {"description" : "Another of the powerful Chinese Zodiac signs, the Ox is steadfast, solid, a goal-oriented \
leader, detail-oriented, hard-working, stubborn, serious and introverted but can feel lonely and insecure. Takes \
comfort in friends and family and is a reliable, protective and strong companion. Compatible with Snake or Rooster.",
      "luckynumbers" : (1, 9),
      "unluckynumbers" : (3, 4)}),  
    ("tiger",
     {"description" : "Those born under the Chinese Zodiac sign of the Tiger are authoritative, self-possessed, \
have strong leadership qualities, are charming, ambitious, courageous, warm-hearted, highly seductive, moody, \
intense, and they’re ready to pounce at any time. Compatible with Horse or Dog.",
      "luckynumbers" : (1, 3, 4),
      "unluckynumbers" : (6, 7, 8)}),  
    ("hare",
     {"description" : "Those born under the Chinese Zodiac sign of the Rabbit enjoy being surrounded by family \
and friends. They’re popular, compassionate, sincere, and they like to avoid conflict and are sometimes seen as \
pushovers. Rabbits enjoy home and entertaining at home. Compatible with Goat or Pig.",
      "luckynumbers" : (3, 4, 9),
      "unluckynumbers" : (1, 7, 8)}),  
    ("dragon",
     {"description" : "A powerful sign, those born under the Chinese Zodiac sign of the Dragon are energetic and \
warm-hearted, charismatic, lucky at love and egotistic. They’re natural born leaders, good at giving orders and \
doing what’s necessary to remain on top. Compatible with Monkey and Rat.",
      "luckynumbers" : (1, 6, 7),
      "unluckynumbers" : (3, 8, 9)}),  
    ("snake",
     {"description" : "Those born under the Chinese Zodiac sign of the Snake are seductive, gregarious, \
introverted, generous, charming, good with money, analytical, insecure, jealous, slightly dangerous, \
smart, they rely on gut feelings, are hard-working and intelligent. Compatible with Rooster or Ox.",
      "luckynumbers" : (2, 8, 9),
      "unluckynumbers" : (1, 6, 7)}),  
    ("horse",
     {"description" : "Those born under the Chinese Zodiac sign of the Horse love to roam free. They’re \
energetic, self-reliant, money-wise, and they enjoy traveling, love and intimacy. They’re great at \
seducing, sharp-witted, impatient and sometimes seen as a drifter. Compatible with Dog or Tiger.",
      "luckynumbers" : (2, 3, 7, 8, 9, 10, 12, 13, 15),
      "unluckynumbers" : (1, 5, 6)}),  
    ("sheep",
     {"description" : "Those born under the Chinese Zodiac sign of the Goat enjoy being alone in their \
thoughts. They’re creative, thinkers, wanderers, unorganized, high-strung and insecure, and can be \
anxiety-ridden. They need lots of love, support and reassurance. Appearance is important too. \
Compatible with Pig or Rabbit.",
      "luckynumbers" : (2, 7),
      "unluckynumbers" : (3, 8)}),  
]

animalnumber = int(input("Enter corresponding numbers to get lucky numbers:\t"))

luckynumbers = animals[animalnumber][1]["luckynumbers"]

s = ""
for i in range(len(luckynumbers)-2):
    s += str(luckynumbers[i]) + ", "

s += str(luckynumbers[-2]) + " and " + str(luckynumbers[-1])
print(s)

"""
print("Lucky numbers:\t", end="")

for i in range(len(luckynumbers)-2):
    written = luckynumbers[i]
    print(written, ", ", sep="", end="")

print(luckynumbers[-2], " and ", luckynumbers[-1], sep="")
"""

print()
