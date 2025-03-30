# title, print empty word, start hangman, input for letter, input for whole word

def grid():
    import random
    print("\nHangman\n")
    
    words=["moin", "servus", "hallo", "hey"]
    global word_choice, empty_word, start_grid, sep
    word_choice=random.choice(words)
    empty_word = " ".join("_" for x in word_choice)
    print("Word: ", empty_word, "\n")
    
    start_grid=[[6*"_", " "],
                        ["|", 2* " "],
                        ["|", 2* " "],
                        ["|", 1* " "],
                        ["|", 2* " "],
                        ["|", " "], 
                        ["-", 6* " "]]
    for row in start_grid:
                                 print(*row)  
    sep="__________________"                             
    user_choice()
    
def user_choice():
       goal=" ".join(word_choice)
       global h, k, sep
       h=1
       k=0
       right_chars=[]
       wrong_chars=[]
       #goal=goal.split(" ")
       while True:
           global empty_word 
           if k == 5:
               print("\nYou fucked up!")
               play_again2=input("\nPlay again? (y/n): ")
               if play_again2.lower == "y":
                   grid()
               else:
                   break    
           print(sep)
           choice=input("\nEnter a guess: ")
           choice=choice.lower()
           if len(choice) >=2 and choice != word_choice:
                     print("Invalid Input! Your guess can only be a single char. ") 
                     continue
           if choice in right_chars or choice in wrong_chars:
               print("This character is already used.")
               continue
           for x in word_choice:
                if x == choice:
                      if x in right_chars:
                           index_char=word_choice.index(x, index_char//2+1)*2
                      else:
                           right_chars.append(choice)
                           index_char=word_choice.index(x)*2
                      empty_word=list(empty_word)
                      empty_word[index_char]=x
                      empty_word= "".join(empty_word)
           if choice== word_choice:
               print(goal)
           else:
               print("\nWord: ", empty_word) 
           if choice not in right_chars and choice != word_choice:
                        wrong_chars.append(choice)
                        print(f"\n", (choice.upper()), "is not in the word!")
                        hangman()
                        print_grid()
                        h+=1
                        k+=1
         
           if choice == word_choice or empty_word== goal:
               print("\nCongratulations! You guessed the word,\'", word_choice,"\' correctly!")
               play_again1=input("\nPlay again? (y/n): ")
               if play_again1.lower == "y":
                    grid()
               else:
                   break    
      
def hangman():
       global start_grid, h, k
       characters = ["|", "O", "\|/", "|", "/ \\"]
       start_grid[h].append(characters[k])
def print_grid():
       global start_grid
       for row in start_grid:
             print(*row)
                                 
                                                                                                 
grid()