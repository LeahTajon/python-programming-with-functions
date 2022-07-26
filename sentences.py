"""
File: sentences.py
Author: Leah Tajon

Task:
Finish a program that automatically generates English sentences.
"""

import random

def main():
    """ Generate and print six random sentences with these characteristic:
    single - past, single - present, single - future,
    plural - past, plural - present, plural - future

    Parameter: none
    Return: nothing
    """
    print()
    # Single - past
    determiner_1 = get_determiner(1)
    noun_1 = get_noun(1)
    verb_1 = get_verb(1, "past")
    prep_1 = get_prepositional_phrase(1)
    adj_1 = get_adjective()
    sentence_1 = f"{determiner_1.capitalize()} {adj_1} {noun_1} {verb_1} {prep_1}."
    print(sentence_1)

    # Single - present
    determiner_2 = get_determiner(1)
    noun_2 = get_noun(1)
    verb_2 = get_verb(1, "present")
    prep_2 = get_prepositional_phrase(1)
    adj_2 = get_adjective()
    sentence_2 = f"{determiner_2.capitalize()} {adj_2} {noun_2} {verb_2} {prep_2}."
    print(sentence_2)
    
    # Single - future
    determiner_3 = get_determiner(1)
    noun_3 = get_noun(1)
    verb_3 = get_verb(1, "future")
    prep_3 = get_prepositional_phrase(1)
    adj_3 = get_adjective()
    sentence_3 = f"{determiner_3.capitalize()} {adj_3} {noun_3} {verb_3} {prep_3}."
    print(sentence_3)

    # Plural - past
    determiner_4 = get_determiner(2)
    noun_4 = get_noun(2)
    verb_4 = get_verb(2, "past")
    prep_4 = get_prepositional_phrase(2)
    adj_4 = get_adjective()
    sentence_4 = f"{determiner_4.capitalize()} {adj_4} {noun_4} {verb_4} {prep_4}."
    print(sentence_4)

    # Plural - present
    determiner_5 = get_determiner(2)
    noun_5 = get_noun(2)
    verb_5 = get_verb(2, "present")
    prep_5 = get_prepositional_phrase(2)
    adj_5 = get_adjective()
    sentence_5 = f"{determiner_5.capitalize()} {adj_5} {noun_5} {verb_5} {prep_5}."
    print(sentence_5)

    # Plural - future
    determiner_6 = get_determiner(2)
    noun_6 = get_noun(2)
    verb_6 = get_verb(2, "future")
    prep_6 = get_prepositional_phrase(2)
    adj_6 = get_adjective()
    sentence_6 = f"{determiner_6.capitalize()} {adj_6} {noun_6} {verb_6} {prep_6}."
    print(sentence_6)
    print()

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", \
            "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", \
            "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", \
            "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", \
            "will run", "will sleep", "will talk", "will walk", "will write"]
    
    word = random.choice(words)
    return word

def get_preposition():
    """ Return a randomly chosen preposition 
    from this list prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    
    Return: a randomly chosen preposition
    """  
    words = ["about", "above", "across", "after", "along",\
        "around", "at", "before", "behind", "below",\
        "beyond", "by", "despite", "except", "for",\
        "from", "in", "into", "near", "of",\
        "off", "on", "onto", "out", "over",\
        "past", "to", "under", "with", "without"]
    
    word = random.choice(words)

    return word

def get_prepositional_phrase(quantity):
    """ Build and return a prepositional phrase composed of four
    words: a preposition, a determiner, an adjective, and a noun by calling the
    get_preposition, get_determiner, get_adjective, and get_noun functions.

    Parameter:
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    adjective = get_adjective()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    word = f"{preposition} {determiner} {adjective} {noun}"

    return word

#--------- STRETCH CHALLENGE ----------------
# Write a function named get_adjective and call it in your main function
# to add an adjective to the sentences produced by your program. Does it
# make sense to call get_adjective in your get_prepositional_phrase function?

def get_adjective():
    """ Return a randomly chosen adjective 
    from this list adjectives:
        "big", "short", "fat", "skinny", "quiet",
        "stinky", "calm", "obedient", "scary", "famous",
        "clever", "white", "black", "stout", "beautiful",
        "clean", "dirty", "lazy", "sporty", "kind",
        "tall", "busy", "pretty", "hungry", "tense",
        "rich", "talented", "happy", "sad", "sassy"
    
    Return: a randomly chosen adjective
    """  
    words = ["big", "short", "fat", "skinny", "quiet",
        "stinky", "calm", "obedient", "scary", "famous",
        "clever", "white", "black", "stout", "beautiful",
        "clean", "dirty", "lazy", "sporty", "kind",
        "tall", "busy", "pretty", "hungry", "tense",
        "rich", "talented", "happy", "sad", "sassy"]

    word = random.choice(words)
    return word

# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
