# Dictionary mapping card names to a nested dictionary of their face value and corresponding reading for item locations
COMMON_DECK = {
    "Avenger" : {
        "VAL" : "One of Swords",
        "FORTUNE" : "The treasure lies in a dragon's house, in hands once clean and now corrupted."
    },
    "Paladin" : {
        "VAL" : "Two of Swords",
        "FORTUNE" : "I see a sleeping prince, a servant of light and the brother of darkness. The treasure lies with him."
    },
    "Soldier" : {
        "VAL" : "Three of Swords",
        "FORTUNE" : "Go to the mountains. Climb the white tower guarded by golden knights."
    },
    "Mercenary" : {
        "VAL" : "Four of Swords",
        "FORTUNE" : "The thing you seek lies with the dead, under mountains of gold coins."
    },
    "Myrmidon" : {
        "VAL" : "Five of Swords",
        "FORTUNE" : "Look for a den of wolves in the hills overlooking a mountain lake. The treasure belongs to Mother Night."
    },
    "Berserker" : {
        "VAL" : "Six of Swords",
        "FORTUNE" : "Find the Mad Dog's crypt. The treasure lies within, beneath blackened bones."
    },
    "Hooded One" : {
        "VAL" : "Seven of Swords",
        "FORTUNE" : "I see a faceless god. He awaits you at the end of a long and winding road, deep in the mountains."
    },
    "Dictator" : {
        "VAL" : "Eight of Swords",
        "FORTUNE" : "I see a throne fit for a king."
    },
    "Torturer" : {
        "VAL" : "Nine of Swords",
        "FORTUNE" : "There is a town where all is not well. There you will find a house of corruption, and within, a dark room full of still ghosts."
    },
    "Warrior" : {
        "VAL" : "Master of Swords",
        "FORTUNE" : "That which you seek lies in the womb of darkness, the devil's lair: the one place to which he must return."
    },
    "Transmuter" : {
        "VAL" : "One of Stars",
        "FORTUNE" : "Go to a place of dizzying heights, where the stone itself is alive!"
    },
    "Diviner" : {
        "VAL" : "Two of Stars",
        "FORTUNE" : "Look to the one who sees all. The treasure is hidden in her camp."
    },
    "Enchanter" : {
        "VAL" : "Three of Stars",
        "FORTUNE" : "I see a kneeling woman - a rose of great beauty plucked too soon. The master of the march knows of whom I speak."
    },
    "Abjurer" : {
        "VAL" : "Four of Stars",
        "FORTUNE" : "I see a fallen house guarded by a great stone dragon. Look to the highest peak."
    },
    "Elementalist" : {
        "VAL" : "Five of Stars",
        "FORTUNE" : "The treasure is hidden in a small castle beneath a mountain, guarded by amber giants."
    },
    "Evoker" : {
        "VAL" : "Six of Stars",
        "FORTUNE" : "Search for the crypt of a wizard ordinaire. His staff is the key."
    },
    "Illusionist" : {
        "VAL" : "Seven of Stars",
        "FORTUNE" : "A man is not what he seems. He comes here in a carnival wagon. Therein lies what you seek."
    },
    "Necromancer" : {
        "VAL" : "Eight of Stars",
        "FORTUNE" : "A woman hangs above a roaring fire. Find her, and you will find the treasure."
    },
    "Conjurer" : {
        "VAL" : "Nine of Stars",
        "FORTUNE" : "I see a dead village, drowned by a river, ruled by one who has brought great evil into the world."
    },
    "Wizard" : {
        "VAL" : "Master of Stars",
        "FORTUNE" : "Look for a wizard's tower on a lake. Let the wizard's name and servant guide you to that which you seek."
    },
    "Swashbuckler" : {
        "VAL" : "One of Coins",
        "FORTUNE" : "I see the skeleton of a deadly warrior, lying on a bed of stone flanked by gargoyles."
    },
    "Philanthropist" : {
        "VAL" : "Two of Coins",
        "FORTUNE" : "Look to a place where sickness and madness are bred. Where children once cried, the treasure lies still."
    },
    "Trader" : {
        "VAL" : "Three of Coins",
        "FORTUNE" : "Look to the wizard of wines! In wood and sand the treasure hides."
    },
    "Merchant" : {
        "VAL" : "Four of Coins",
        "FORTUNE" : "Seek a cask that once contained the finest wine, of which not a drop remains."
    },
    "Guild Member" : {
        "VAL" : "Five of Coins",
        "FORTUNE" : "I see a dark room full of bottles. It is the tomb of a guild member."
    },
    "Beggar" : {
        "VAL" : "Six of Coins",
        "FORTUNE" : "A wounded elf has what you seek. He will part with the treasure to see his dark desire fulfilled."
    },
    "Thief" : {
        "VAL" : "Seven of Coins",
        "FORTUNE" : "What you seek lies at the crossroads of life and death, among the buried dead."
    },
    "Tax Collector" : {
        "VAL" : "Eight of Coins",
        "FORTUNE" : "The Vistani have what you seek. A missing child holds the key to the treasure's release."
    },
    "Miser" : {
        "VAL" : "Nine of Coins",
        "FORTUNE" : "Look for a fortress inside a fortress, in a place hidden behind fire."
    },
    "Rogue" : {
        "VAL" : "Master of Coins",
        "FORTUNE" : "I see a nest of ravens. There you will find the prize."
    },
    "Monk" : {
        "VAL" : "One of Glyphs",
        "FORTUNE" : "The treasure you seek is hidden behind the sun, in the house of a saint."
    },
    "Missionary" : {
        "VAL" : "Two of Glyphs",
        "FORTUNE" : "I see a garden dusted with snow, watched over by a scarecrow with a sackcloth grin. Look not to the garden but to the guardian."
    },
    "Healer" : {
        "VAL" : "Three of Glyphs",
        "FORTUNE" : "Look to the west. Find a pool blessed by the light of the white sun."
    },
    "Shepherd" : {
        "VAL" : "Four of Glyphs",
        "FORTUNE" : "Find the mother - she who gave birth to evil."
    },
    "Druid" : {
        "VAL" : "Five of Glyphs",
        "FORTUNE" : "An evil tree grows atop a hill of graves where the ancient dead sleep. The ravens can help you find it. Look for the treasure there."
    },
    "Anarchist" : {
        "VAL" : "Six of Glyphs",
        "FORTUNE" : "I see walls of bones, a chandelier of bones, and a table of bones - all that remains of enemies long forgotten."
    },
    "Charlatan" : {
        "VAL" : "Seven of Glyphs",
        "FORTUNE" : "I see a lonely mill on a precipice. The treasure lies within."
    },
    "Bishop" : {
        "VAL" : "Eight of Glyphs",
        "FORTUNE" : "What you  seek lies in a pile of treasure, beyond a set of amber doors."
    },
    "Traitor" : {
        "VAL" : "Nine of Glyphs",
        "FORTUNE" : "Look for a wealthy woman. A staunch ally of the devil, she keeps her treasure under lock and key, with the bones of an ancient enemy."
    },
    "Priest" : {
        "VAL" : "Master of Glyphs",
        "FORTUNE" : "You will find what you seek in the castle, amid the ruins of a placce of supplication."
    }
}

# Dictionary mapping High Deck cards to a nested dictionary of the corresponding "Chosen Ally" (or in some cases array of possible allies) and location of the showdown with Strahd
HIGH_DECK = {
    "Artifact": {
        "ALLY" : "Look for an entertaining man with a monkey. This man is more than he seems.",
        "LOCATION" : "He lurks in the darkness where the morning light once shone - a sacred place."
    },
    "Beast": {
        "ALLY" : "A werewolf holds a secret hatred for your enemy. Use her hatred to your advantage",
        "LOCATION" : "The beast sits on his dark throne."
    },
    "Broken One": {
        "ALLY" : ["Your greatest ally will be a wizard. His mind is broken, but his spells are strong.", "I see a man of faith whose sanity hangs by a thread. He has lost someone close to him."],
        "LOCATION" : "He haunts the tomb of the man he envied above all."
    },
    "Darklord": {
        "ALLY" : "Ah, the worst of all truths: You must face the evil of this land alone!",
        "LOCATION" : "He lurks in the depths of darkness, in the one place to which he must return."
    },
    "Donjon": {
        "ALLY" : ["Search for a troubled young man surrounded by wealth and madness. His home is his prison.", "Find a girl driven to insanity, locked in the heart of her dead father's house. Curing her madness is key to your success."],
        "LOCATION" : "He lurks in a hall of bones, in the dark pits of his castle."
    },
    "Seer": {
        "ALLY" : "Look for a dusk elf living among the Vistani. He has suffered a great loss and is haunted by dark dreams. Help him, and he will help you in return.",
        "LOCATION" : "He waits for you in a place of wisdom, warmth, and despair. Great secrets are there."
    },
    "Ghost": {
        "ALLY" : ["I see a fallen paladin of a fallen order of knights. He lingers like a ghost in a dead dragon's lair.", "Stir the spirit of the clumsy knight whose crypt lies deep within the castle."],
        "LOCATION" : "Look to the father's tomb."
    },
    "Executioner": {
        "ALLY" : "Seek out the bother of the devil's bride. They call him 'the lesser', but he has a powerful soul.",
        "LOCATION" : "I see a dark figure on a balcony, looking down upon this tortured land with a twisted smile."
    },
    "Horseman": {
        "ALLY" : ["I see a dead man of noble birth, guarded by his widow. Return life to the dead man's corpse, and he will be your staunch ally.", " A man of death named Arrigal will forsake his dark lord to serve your cause. Beware! He has a rotten soul."],
        "LOCATION" : "He lurks in the one place to which he must return - a place of death."
    },
    "Innocent": {
        "ALLY" : ["I see a young man with a kind heart. A mother's boy! He is strong of body but weak of mind. Seek him out in the village of Barovia.", "Evil's bride is the one you seek!"],
        "LOCATION" : "He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon."
    },
    "Marionette": {
        "ALLY" : ["What horror is this? I see a man made by a man. Ageless and alone, it haunts the towers of the castle.", "Look for a man of music, a man with two heads. He lives in a place of great hunger and sorrow."],
        "LOCATION" : "Look to the great heights. Find the beating heart of the castle. He waits nearby."
    },
    "Mists": {
        "ALLY" : "A Vistana wanders this land alone, searching for he mentor. She does not stay in one place for long. Seek her out at Saint Markovia's abbey, near the mists",
        "LOCATION" : "The cards can't see where the evil lurks. The mists obscure all!"
    },
    "Raven": {
        "ALLY" : "Find the leader of the feathered ones who live among the vines. Though old, he has one more fight left in him.",
        "LOCATION" : "Look to the mother's tomb."
    },
    "Tempter": {
        "ALLY" : ["I see a child - a Vistana. You must hurry, for her fate hands in the balance. Find her at the lake!", "I head a wedding bell, or perhaps a death knell. It calls thee to a mountainside abbeym wherein you will find a woman who is more than the sum of her parts."],
        "LOCATION" : "I see a secret place - a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure."
    },
}

# Text for the fortune reading, with variables to be replaced by parameters
FORTUNE_TEXT = {
    "INTRO_A": "The Vistana lays out two decks of cards before you, one much larger than the other.",
    "INTRO_B": "From the larger deck, she draws three cards and lays them face down in a row in from of you.",
    "INTRO_C": "From the smaller deck, she draws two cards. She lays one above the middle card of the row of three, and one below to form a cross.",
    "BOOK_A": "She touches the first card from the row of three and says, \"This card tells of history. Knowledge of the ancient will help you better understand your enemy.\" She flips the card over to reveal BOOK_VAL - The BOOK_NAME.",
    "BOOK_B": "\"BOOK_FORTUNE\"",
    "SYMBOL_A": "She touches the second card from the same row and says, \"This card tells of a powerful force for good and protections, a holy symbol of great hope.\" She flips the card over to reveal SYMBOL_VAL - The SYMBOL_NAME.",
    "SYMBOL_B": "\"SYMBOL_FORTUNE\"",
    "SWORD_A": "She picks up the last card from the row and says, \"This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight.\" She flips the card over to reveal SWORD_VAL - The SWORD_NAME.",
    "SWORD_B": "\"SWORD_FORTUNE\"",
    "ALLY_A": "She picks up the card above the row of three saying, \"This card sheds light on one who will help you greatly in the battle against darkness.\" She flips the card over to reveal The ALLY_NAME.",
    "ALLY_B": "\"ALLY_FORTUNE\"",
    "LOCATION_A": "She touches the last face down card and says, \"Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him!\" She flips the card over to reveal The LOCATION_NAME.",
    "LOCATION_B": "\"LOCATION_FORTUNE\"",
}