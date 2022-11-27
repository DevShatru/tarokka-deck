import os
from random import randint

itemLocations = {
    "Avenger" : {
        "val" : "One of Swords",
        "reading" : "The treasure lies in a dragon's house, in hands once clean and now corrupted."
    },
    "Paladin" : {
        "val" : "Two of Swords",
        "reading" : "I see a sleeping prince, a servant of light and the brother of darkness. The treasure lies with him."
    },
    "Soldier" : {
        "val" : "Three of Swords",
        "reading" : "Go to the mountains. Climb the white tower guarded by golden knights."
    },
    "Mercenary" : {
        "val" : "Four of Swords",
        "reading" : "The thing you seek lies with the dead, under mountains of gold coins."
    },
    "Myrmidon" : {
        "val" : "Five of Swords",
        "reading" : "Look for a den of wolves in the hills overlooking a mountain lake. The treasure belongs to Mother Night."
    },
    "Berserker" : {
        "val" : "Six of Swords",
        "reading" : "Find the Mad Dog's crypt. The treasure lies within, beneath blackened bones."
    },
    "Hooded One" : {
        "val" : "Seven of Swords",
        "reading" : "I see a faceless god. He awaits you at the end of a long and winding road, deep in the mountains."
    },
    "Dictator" : {
        "val" : "Eight of Swords",
        "reading" : "I see a throne fit for a king."
    },
    "Torturer" : {
        "val" : "Nine of Swords",
        "reading" : "There is a town where all is not well. There you will find a house of corruption, and within, a dark room full of still ghosts."
    },
    "Warrior" : {
        "val" : "Master of Swords",
        "reading" : "That which you seek lies in the womb of darkness, the devil's lair: the one place to which he must return."
    },
    "Transmuter" : {
        "val" : "One of Stars",
        "reading" : "Go to a place of dizzying heights, where the stone itself is alive!"
    },
    "Diviner" : {
        "val" : "Two of Stars",
        "reading" : "Look to the one who sees all. The treasure is hidden in her camp."
    },
    "Enchanter" : {
        "val" : "Three of Stars",
        "reading" : "I see a kneeling woman - a rose of great beauty plucked too soon. The master of the march knows of whom I speak."
    },
    "Abjurer" : {
        "val" : "Four of Stars",
        "reading" : "I see a fallen house guarded by a great stone dragon. Look to the highest peak."
    },
    "Elementalist" : {
        "val" : "Five of Stars",
        "reading" : "The treasure is hidden in a small castle beneath a mountain, guarded by amber giants."
    },
    "Evoker" : {
        "val" : "Six of Stars",
        "reading" : "Search for the crypt of a wizard ordinaire. His staff is the key."
    },
    "Illusionist" : {
        "val" : "Seven of Stars",
        "reading" : "A man is not what he seems. He comes here in a carnival wagon. Therein lies what you seek."
    },
    "Necromancer" : {
        "val" : "Eight of Stars",
        "reading" : "A woman hangs above a roaring fire. Find her, and you will find the treasure."
    },
    "Conjurer" : {
        "val" : "Nine of Stars",
        "reading" : "I see a dead village, drowned by a river, ruled by one who has brought great evil into the world."
    },
    "Wizard" : {
        "val" : "Master of Stars",
        "reading" : "Look for a wizard's tower on a lake. Let the wizard's name and servant guide you to that which you seek."
    },
    "Swashbuckler" : {
        "val" : "One of Coins",
        "reading" : "I see the skeleton of a deadly warrior, lying on a bed of stone flanked by gargoyles."
    },
    "Philanthropist" : {
        "val" : "Two of Coins",
        "reading" : "Look to a place where sickness and madness are bred. Where children once cried, the treasure lies still."
    },
    "Trader" : {
        "val" : "Three of Coins",
        "reading" : "Look to the wizard of wines! In wood and sand the treasure hides."
    },
    "Merchant" : {
        "val" : "Four of Coins",
        "reading" : "Seek a cask that once contained the finest wine, of which not a drop remains."
    },
    "Guild Member" : {
        "val" : "Five of Coins",
        "reading" : "I see a dark room full of bottles. It is the tomb of a guild member."
    },
    "Beggar" : {
        "val" : "Six of Coins",
        "reading" : "A wounded elf has what you seek. He will part with the treasure to see his dark desire fulfilled."
    },
    "Thief" : {
        "val" : "Seven of Coins",
        "reading" : "What you seek lies at the crossroads of life and death, among the buried dead."
    },
    "Tax Collector" : {
        "val" : "Eight of Coins",
        "reading" : "The Vistani have what you seek. A missing child holds the key to the treasure's release."
    },
    "Miser" : {
        "val" : "Nine of Coins",
        "reading" : "Look for a fortress inside a fortress, in a place hidden behind fire."
    },
    "Rogue" : {
        "val" : "Master of Coins",
        "reading" : "I see a nest of ravens. There you will find the prize."
    },
    "Monk" : {
        "val" : "One of Glyphs",
        "reading" : "The treasure you seek is hidden behind the sun, in the house of a saint."
    },
    "Missionary" : {
        "val" : "Two of Glyphs",
        "reading" : "I see a garden dusted with snow, watched over by a scarecrow with a sackcloth grin. Look not to the garden but to the guardian."
    },
    "Healer" : {
        "val" : "Three of Glyphs",
        "reading" : "Look to the west. Find a pool blessed by the light of the white sun."
    },
    "Shepherd" : {
        "val" : "Four of Glyphs",
        "reading" : "Find the mother - she who gave birth to evil."
    },
    "Druid" : {
        "val" : "Five of Glyphs",
        "reading" : "An evil tree grows atop a hill of graves where the ancient dead sleep. The ravens can help you find it. Look for the treasure there."
    },
    "Anarchist" : {
        "val" : "Six of Glyphs",
        "reading" : "I see walls of bones, a chandelier of bones, and a table of bones - all that remains of enemies long forgotten."
    },
    "Charlatan" : {
        "val" : "Seven of Glyphs",
        "reading" : "I see a lonely mill on a precipice. The treasure lies within."
    },
    "Bishop" : {
        "val" : "Eight of Glyphs",
        "reading" : "What you  seek lies in a pile of treasure, beyond a set of amber doors."
    },
    "Traitor" : {
        "val" : "Nine of Glyphs",
        "reading" : "Look for a wealthy woman. A staunch ally of the devil, she keeps her treasure under lock and key, with the bones of an ancient enemy."
    },
    "Priest" : {
        "val" : "Master of Glyphs",
        "reading" : "You will find what you seek in the castle, amid the ruins of a placce of supplication."
    }
}
HighDict = {
    "Artifact": {
        "chosen": "Look for an entertaining man with a monkey. This man is more than he seems.",
        "location": "He lurks in the darkness where the morning light once shone - a sacred place."
    },
    "Beast": {
        "chosen": "A werewolf holds a secret hatred for your enemy. Use her hatred to your advantage",
        "location": "The beast sits on his dark throne."
    },
    "Broken One": {
        "chosen": ["Your greatest ally will be a wizard. His mind is broken, but his spells are strong.", "I see a man of faith whose sanity hangs by a thread. He has lost someone close to him."],
        "location": "He haunts the tomb of the man he envied above all."
    },
    "Darklord": {
        "chosen": "Ah, the worst of all truths: You must face the evil of this land alone!",
        "location": "He lurks in the depths of darkness, in the one place to which he must return."
    },
    "Donjon": {
        "chosen": ["Search for a troubled young man surrounded by wealth and madness. His home is his prison.", "Find a girl driven to insanity, locked in the heart of her dead father's house. Curing her madness is key to your success."],
        "location": "He lurks in a hall of bones, in the dark pits of his castle."
    },
    "Seer": {
        "chosen": "Look for a dusk elf living among the Vistani. He has suffered a great loss and is haunted by dark dreams. Help him, and he will help you in return.",
        "location": "He waits for you in a place of wisdom, warmth, and despair. Great secrets are there."
    },
    "Ghost": {
        "chosen": ["I see a fallen paladin of a fallen order of knights. He lingers like a ghost in a dead dragon's lair.", "Stir the spirit of the clumsy knight whose crypt lies deep within the castle."],
        "location": "Look to the father's tomb."
    },
    "Executioner": {
        "chosen": "Seek out the bother of the devil's bride. They call him 'the lesser', but he has a powerful soul.",
        "location": "I see a dark figure on a balcony, looking down upon this tortured land with a twisted smile."
    },
    "Horseman": {
        "chosen": ["I see a dead man of noble birth, guarded by his widow. Return life to the dead man's corpse, and he will be your staunch ally.", " A man of death named Arrigal will forsake his dark lord to serve your cause. Beware! He has a rotten soul."],
        "location": "He lurks in the one place to which he must return - a place of death."
    },
    "Innocent": {
        "chosen": ["I see a young man with a kind heart. A mother's boy! He is strong of body but weak of mind. Seek him out in the village of Barovia.", "Evil's bride is the one you seek!"],
        "location": "He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon."
    },
    "Marionette": {
        "chosen": ["What horror is this? I see a man made by a man. Ageless and alone, it haunts the towers of the castle.", "Look for a man of music, a man with two heads. He lives in a place of great hunger and sorrow."],
        "location": "Look to the great heights. Find the beating heart of the castle. He waits nearby."
    },
    "Mists": {
        "chosen": "A Vistana wanders this land alone, searching for he mentor. She does not stay in one place for long. Seek her out at Saint Markovia's abbey, near the mists",
        "location": "The cards can't see where the evil lurks. The mists obscure all!"
    },
    "Raven": {
        "chosen": "Find the leader of the feathered ones who live among the vines. Though old, he has one more fight left in him.",
        "location": "Look to the mother's tomb."
    },
    "Tempter": {
        "chosen": ["I see a child - a Vistana. You must hurry, for her fate hands in the balance. Find her at the lake!", "I head a wedding bell, or perhaps a death knell. It calls thee to a mountainside abbeym wherein you will find a woman who is more than the sum of her parts."],
        "location": "I see a secret place - a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure."
    },
}
CommonDeck = list(itemLocations.keys())
HighDeck = list(HighDict.keys())

def getReading(obj):
    if type(obj) is str:
        return obj
    else:
        return obj[randint(1, 2) - 1]

def tell_fortune():
    book = CommonDeck[randint(1, len(CommonDeck)) - 1]
    symbol = CommonDeck[randint(0, len(CommonDeck)) - 1]
    while book == symbol:
        symbol = CommonDeck[randint(0, len(CommonDeck)) - 1]
    sword = CommonDeck[randint(1, len(CommonDeck)) - 1]
    while book == sword or symbol == sword:
        sword = CommonDeck[randint(1, len(CommonDeck)) - 1]
    chosen = HighDeck[randint(1, len(HighDeck)) - 1]
    showdown = HighDeck[randint(1, len(HighDeck)) - 1]
    while chosen == showdown:
        showdown = HighDeck[randint(1, len(HighDeck)) - 1]
    print("The Vistana lays out two decks of cards before you, one much larger than the other.")
    input()
    print("From the larger deck, she draws three cards and lays them face down in a row in from of you.")
    input()
    print("From the smaller deck, she draws two cards. She lays one above the middle card of the row of three, and one below to form a cross.")
    input()
    print("\nShe touches the first card from the row of three and says, \"This card tells of history. Knowledge of the ancient will help you better understand your enemy.\" She flips the card over to reveal " + itemLocations[book]["val"] + " - The " + book + ".\n\"" + itemLocations[book]["reading"] + "\"\n")
    input()
    print("\nShe touches the second card from the same row and says, \"This card tells of a powerful force for good and protections, a holy symbol of great hope.\" She flips the card over to reveal " + itemLocations[symbol]["val"] + " - The " + symbol + ".\n\"" + itemLocations[symbol]["reading"] + "\"\n")
    input()
    print("\nShe picks up the last card from the row and says, \"This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight.\" She flips the card over to reveal " + itemLocations[sword]["val"] + " - The " + sword + ".\n\"" + itemLocations[sword]["reading"] + "\"\n")
    input()
    print("\nShe picks up the card above the row of three saying, \"This card sheds light on one who will help you greatly in the battle against darkness.\" She flips the card over to reveal The " + chosen + ".\n\"" + getReading(HighDict[chosen]["chosen"]) + "\"\n")
    input()
    print("\nShe touches the last face down card and says, \"Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him!\" She flips the card over to reveal The " + showdown + ".\n\"" + HighDict[showdown]["location"] + "\"\n")
    input()

tell_fortune()