#!/usr/bin/env python
# coding: utf-8

# # Hang Man Game

# In[2]:


import random
from os import name, system 


# Clean screen

# In[3]:


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Game Code

# In[11]:


def game():
    
    clear()
    
    print('\nWelcome to the game.')
    print('\nGuess the word...\n')
    
    #words' list
    words = ['banana', 'grape', 'avocado', 'strawberry', 'orange']
    
    #random word
    word = random.choice(words)
    
    #discover word template
    discover_letter = ['-' for letter in word]
    
    #nb of chances
    chances = 6
    
    #wrong letter
    wrong_letters = []
    
    #while nb of chances > 0
    while chances > 0:
        print(''.join(discover_letter))
        print('\nChances: ',chances)
        print('Wrong letters:',''.join(wrong_letters))
    
    #try
        trial = input('\nDigite uma letra: ').lower()
    
    #Condicional
    
        if trial in word:
            index = 0
            for letter in word:
                if trial == letter:
                    discover_letter[index] = letter
                index += 1
            
        else: 
            chances -= 1
            wrong_letters.append(trial)

        if "-" not in discover_letter:
            print('\nYou win! The word is: ', word)
            break
            
    if "_" in discover_letter:
        print('\nYou lose! The word is: ', word)


# In[12]:


game()

