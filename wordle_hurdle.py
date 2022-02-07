#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import tkinter as tk

GUI = True   #Variable to run the program in GUI mode
# Functions needed for GUI
def get_values():
    """A GUI window to get user input
    """
    def close_window():
        """Function to close GUI window
        """
        main_frame.destroy()
        
    main_frame = tk.Tk()
    main_frame.title('WORDLE-HURDLE')
    main_frame.resizable(True, True)
    main_frame.configure(bg='#6aaa64')
    
    AlphsInWord = tk.StringVar(main_frame)
    AlphsNotInWord = tk.StringVar(main_frame)
    AlphsWithKnownPosition = tk.StringVar(main_frame)
    AlphsWithNotKnownPosition = tk.StringVar(main_frame)
    AlphsPositions = tk.StringVar(main_frame)
    AlphsNotPositions = tk.StringVar(main_frame)
    
    Alphabets = tk.Label(main_frame, 
                         text="Write letters which are there in the word (without any space, e.g, cud)", 
                         fg='black', bg="#6aaa64", font=('Times', 16, 'bold'))
    NotThereAlphabets = tk.Label(main_frame, 
                         text="Write letters which are not there in the word (without any space, e.g, xyn)", 
                         fg='black', bg="#6aaa64", font=('Times', 16, 'bold'))
    AlphabetsWithKnownPos = tk.Label(main_frame, 
                         text="Write letters whose position is known in the word (without any space, e.g, cd)", 
                         fg='black', bg="#6aaa64", font=('Times', 16, 'bold'))
    AlphabetsWithNotKnownPos = tk.Label(main_frame, 
                         text="Write letters whose position is not known in the word (without any space, e.g, u)", 
                         fg='black', bg="#6aaa64", font=('Times',16, 'bold'))
    AlphabetsPos = tk.Label(main_frame, 
                         text="Give positions of the known letters in the word (without any space, e.g, 02)", 
                         fg='black', bg="#6aaa64", font=('Times',16, 'bold'))
    AlphabetsNotPos = tk.Label(main_frame, 
                         text="Give positions where letters are not in the word (without any space, e.g, 3)", 
                         fg='black', bg="#6aaa64", font=('Times',16, 'bold'))
    CloseButton = tk.Button(main_frame, text='See Words', command=close_window, 
                             font=('Times',16, 'bold'), bg='white', fg='red')
    
    Alphabets_Entry = tk.Entry(main_frame, bd=5, textvariable=AlphsInWord,font=('Times', 12))
    NotThereAlphabets_Entry = tk.Entry(main_frame, bd=5, textvariable=AlphsNotInWord,font=('Times', 12))
    AlphabetsWithKnownPos_Entry = tk.Entry(main_frame, bd=5, textvariable=AlphsWithKnownPosition,font=('Times', 12))
    AlphabetsPos_Entry = tk.Entry(main_frame, bd=5, textvariable=AlphsPositions,font=('Times', 12))
    AlphabetsWithNotKnownPos_Entry = tk.Entry(main_frame, bd=5, textvariable=AlphsWithNotKnownPosition,font=('Times', 12))
    AlphabetsNotPos_Entry = tk.Entry(main_frame, bd=5, textvariable=AlphsNotPositions,font=('Times', 12))

    
    Alphabets.grid(row=0, column=0, columnspan=2)
    Alphabets_Entry.grid(row=0, column=2)
    NotThereAlphabets.grid(row=1, column=0, columnspan=2)
    NotThereAlphabets_Entry.grid(row=1, column=2)
    AlphabetsWithKnownPos.grid(row=2, column=0, columnspan=2)
    AlphabetsWithKnownPos_Entry.grid(row=2, column=2)
    AlphabetsPos.grid(row=3, column=0, columnspan=2)
    AlphabetsPos_Entry.grid(row=3, column=2)
    AlphabetsWithNotKnownPos.grid(row=4, column=0, columnspan=2)
    AlphabetsWithNotKnownPos_Entry.grid(row=4, column=2)
    AlphabetsNotPos.grid(row=5, column=0, columnspan=2)
    AlphabetsNotPos_Entry.grid(row=5, column=2)
    CloseButton.grid(row=6, column=2)
    
    main_frame.mainloop()
    
    retain_set = set(AlphsInWord.get().lower())
    drop_set = set(AlphsNotInWord.get().lower())
    known_pairs = {}
    unknown_pairs = {}
    if len(AlphsWithKnownPosition.get()) != 0:
        for i in range(len(AlphsWithKnownPosition.get())):
            known_pairs[str(AlphsWithKnownPosition.get()[i])] = int(AlphsPositions.get()[i])
            
    if len(AlphsWithNotKnownPosition.get()) != 0:
        for i in range(len(AlphsWithNotKnownPosition.get())):
            unknown_pairs[str(AlphsWithNotKnownPosition.get()[i])] = int(AlphsNotPositions.get()[i])
    
    return retain_set, drop_set, known_pairs, unknown_pairs


def print_words(words):
    """GUI window to print output words
    """
    
    def close_window():
        """Function to close GUI window
        """
        main_frame.destroy()
        
    main_frame = tk.Tk()
    main_frame.title('WORDLE-HURDLE')
    main_frame.resizable(True, True)
    main_frame.configure(bg='#6aaa64')
    var = tk.StringVar(main_frame)
    words_print = tk.Text(main_frame,  
                         fg='black', bg='#6aaa64', font=('Times',16,'bold'))
    words_print.insert('1.0',words)
    CloseButton = tk.Button(main_frame, text='Exit', command=close_window, 
                             font=('Times',12), bg='white', fg='red')
    words_print.pack()
    CloseButton.pack()
    main_frame.mainloop()


#Read Words' list from the words.txt file and filter unnecessery words
words = pd.read_csv('words.txt', sep='\n', names=['WORDS'])
words_new = pd.DataFrame()
words_new['WORDS'] = words['WORDS'].apply(lambda x: x if len(str(x)) == 5 else np.nan)
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
words_new['WORDS'] = words_new['WORDS'].apply(lambda x : x if 
                                    set(list(str(x).lower())).issubset(set(alphabets.lower())) else np.nan)
words_new = words_new.dropna().reset_index(drop=True)

# Input values if GUI is false; {} are dictionaries 
if GUI:
    retaining, dropping, alphabet_pos, alphabet_nos_pos = get_values()
else:
    retaining = ['a','e']
    dropping = ['x']
    alphabet_pos = {
                    'a':1,
                    'e':2
                   }
    alphabet_nos_pos = {
                        'k':2,
                        'l':4
                        }
    
#Logic to filter words on the basis of user's input
    
words_new['WORDS'] = words_new['WORDS'].apply(lambda x : x if 
                                    set(list(str(x).lower())).isdisjoint(set(dropping)) else np.nan)
words_new['WORDS'] = words_new['WORDS'].apply(lambda x : x if 
                                 (set(retaining)).issubset(set(list(str(x).lower()))) else np.nan)
words_new = words_new.dropna().reset_index(drop=True)

if bool(alphabet_pos):
    for key, value in alphabet_pos.items():
        words_new['WORDS'] = words_new['WORDS'].apply(lambda x: x if (str(x).lower()[int(alphabet_pos[key])]
                                                                      == str(key)) else np.nan)
        words_new = words_new.dropna().reset_index(drop=True)
        
if bool(alphabet_nos_pos):
    for key, value in alphabet_nos_pos.items():
        words_new['WORDS'] = words_new['WORDS'].apply(lambda x: x if (str(x).lower()[int(alphabet_nos_pos[key])]
                                                                      != str(key)) else np.nan)
        words_new = words_new.dropna().reset_index(drop=True)
        
words_new['WORDS'] = words_new['WORDS'].apply(lambda x: x.upper())
    
words_to_print = str(words_new['WORDS'].values)

if GUI:
    print_words(words=words_to_print)
else:
    print(words_to_print)