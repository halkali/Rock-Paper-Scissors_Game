import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pc = [rock,paper,scissors]
ch= int(input("your choice 0=rock, 1=paper, 2=scissors:"))
rnd= random.randint(0,2)
print(f"your choose:{pc[ch]}")
print(f"pc choose:{pc[rnd]}")
if(pc[ch]==pc[rnd]):
  print("beraber")
elif((rnd==0 and ch==1) or (rnd==1 and ch==2) or (rnd==2 and ch==0)):
    print("you win.")
else:
    print("you lose")


