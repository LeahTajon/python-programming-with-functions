"""
File: sentences.py
Author: Leah Tajon

Task:
Finish a program that automatically generates English sentences.
"""

from sentences import get_adjective, get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", \
        "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 10 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(10):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", \
        "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_noun function which
        # should return a plural nouns.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    
    past = ["drank", "ate", "grew", "laughed", "thought", \
            "ran", "slept", "talked", "walked", "wrote"]
    
    future = ["will drink", "will eat", "will grow", "will laugh", "will think", \
            "will run", "will sleep", "will talk", "will walk", "will write"]

    # 1. Test the single quantity

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a singular verb and past tense.
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past list.
        assert word in past

    present_singular = ["drinks", "eats", "grows", "laughs", "thinks", \
            "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):    

        # Call the get_verb function which
        # should return a singular verb and present tense.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_singular list.
        assert word in present_singular
    
    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a singular verb and future tense.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future list.
        assert word in future

    # 2. Test the plural quantity

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a plural verb and past tense.
        word = get_verb(2, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past list.
        assert word in past
    
    present_plural = ["drink", "eat", "grow", "laugh", "think", \
            "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a plural verb and present tense.
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_plural list.
        assert word in present_plural
    
     # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_verb function which
        # should return a plural verb and future tense.
        word = get_verb(2, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future list.
        assert word in future

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",\
        "around", "at", "before", "behind", "below",\
        "beyond", "by", "despite", "except", "for",\
        "from", "in", "into", "near", "of",\
        "off", "on", "onto", "out", "over",\
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 30 times.
    for _ in range(30):

        # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the prepositions list.
        assert word in prepositions

def test_get_prepositional_phrase():

    prepositions = ["about", "above", "across", "after", "along",\
        "around", "at", "before", "behind", "below",\
        "beyond", "by", "despite", "except", "for",\
        "from", "in", "into", "near", "of",\
        "off", "on", "onto", "out", "over",\
        "past", "to", "under", "with", "without"]

    adjectives = ["big", "short", "fat", "skinny", "quiet",
        "stinky", "calm", "obedient", "scary", "famous",
        "clever", "white", "black", "stout", "beautiful",
        "clean", "dirty", "lazy", "sporty", "kind",
        "tall", "busy", "pretty", "hungry", "tense",
        "rich", "talented", "happy", "sad", "sassy"]

    # 1. Test single determiners and nouns
    single_determiners = ["a", "one", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", \
        "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 30 times.
    for _ in range(30):

        # Call the get_preposition_phrase function which
        # should return a preposition, plural determiner,
        # adjective, and a plural noun.
        word = get_prepositional_phrase(1)

        # Use split() method to separate strings into a list
        split_word = word.split()

        # Verify that the words returned from split_word 
        # are in the prepositions, adj, single_determiners,
        # and single_nouns lists.
        assert split_word[0] in prepositions
        assert split_word[1] in single_determiners
        assert split_word[2] in adjectives
        assert split_word[3] in single_nouns

    # 2. Test plural determiners and nouns
    plural_determiners = ["two", "some", "many", "the"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", \
        "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 30 times.
    for _ in range(30):

        # Call the get_preposition_phrase function which
        # should return a preposition, plural determiner,
        # adjective, and a plural noun.
        word = get_prepositional_phrase(2)

        # Use split() method to separate strings into a list
        split_word = word.split()

        # Verify that the words returned from split_word 
        # are in the prepositions, adj, single_determiners,
        # and single_nouns lists.
        assert split_word[0] in prepositions
        assert split_word[1] in plural_determiners
        assert split_word[2] in adjectives
        assert split_word[3] in plural_nouns

#--------- STRETCH CHALLENGE ----------
# In test_sentences.py write a function named test_get_adjective that
# tests the get_adjective function.
def test_get_adjective():
    adjectives = ["big", "short", "fat", "skinny", "quiet",
        "stinky", "calm", "obedient", "scary", "famous",
        "clever", "white", "black", "stout", "beautiful",
        "clean", "dirty", "lazy", "sporty", "kind",
        "tall", "busy", "pretty", "hungry", "tense",
        "rich", "talented", "happy", "sad", "sassy"]

    # This loop will repeat the statements inside it 30 times.
    for _ in range(30):

        # Call the get_adjective function which
        # should return an adjective.
        word = get_adjective()

        # Verify that the word returned from get_adjective
        # is one of the words in the adjectives list.
        assert word in adjectives

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])