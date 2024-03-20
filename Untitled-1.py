
import random





def game(): 
  
  
  celebrities = [
      {"name": "Kylie Jenner", "followers": 276},
      {"name": "Dwayne Johnson", "followers": 265},
      {"name": "Cristiano Ronaldo", "followers": 338},
      {"name": "Ariana Grande", "followers": 256},
      {"name": "Selena Gomez", "followers": 222},
      {"name": "Kim Kardashian", "followers": 236},
      {"name": "Lionel Messi", "followers": 242},
      {"name": "Beyoncé", "followers": 198},
      {"name": "Justin Bieber", "followers": 214},
      {"name": "Taylor Swift", "followers": 164},
      {"name": "Neymar Jr.", "followers": 158},
      {"name": "Kendall Jenner", "followers": 187},
      {"name": "Jennifer Lopez", "followers": 147},
      {"name": "LeBron James", "followers": 127},
      {"name": "Shakira", "followers": 77},
      {"name": "Kevin Hart", "followers": 108},
      {"name": "Gigi Hadid", "followers": 69},
      {"name": "Zayn Malik", "followers": 75},
      {"name": "Priyanka Chopra", "followers": 72},
      {"name": "Drake", "followers": 88},
      {"name": "Billie Eilish", "followers": 103},
      {"name": "Rihanna", "followers": 103},
      {"name": "Ed Sheeran", "followers": 90},
      {"name": "Ellen DeGeneres", "followers": 105},
      {"name": "Lionel Messi", "followers": 242},
      {"name": "David Beckham", "followers": 71},
      {"name": "Jennifer Aniston", "followers": 38},
      {"name": "Shawn Mendes", "followers": 74},
      {"name": "Lady Gaga", "followers": 111},
      {"name": "Kevin Durant", "followers": 12},
      {"name": "Emma Watson", "followers": 60},
      {"name": "Robert Downey Jr.", "followers": 50},
      {"name": "Will Smith", "followers": 99}
  ]


  life = 3
  correct = 0
  pick1 = random.randint(0 , len(celebrities))
  print("pick if followers of the celeb is higher or lower")
  while(life > 0):
    pick = random.randint(0 , len(celebrities)-1)
    
    print(f"do you think {celebrities[pick1]} higher than {celebrities[pick]}!" )
    print('enter "y" or "n" ')
    user_input= input()
    if(user_input == "y" and celebrities[pick1]["followers"] >= celebrities[pick]["followers"]):
      print("correct")
      pick1 = pick
      correct += 1
    elif(user_input == "n" and celebrities[pick1]["followers"] <= celebrities[pick]["followers"]):
      print("correct")
      pick1 = pick
      correct += 1
    else: 
      print("wrong answer loss a life")
      life -= 1
      print(f"{life} / 3")
  print("you lost")


game()
    
