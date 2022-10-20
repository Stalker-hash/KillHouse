#pylint:disable=E0001
#pylint:disable=C0114
#pylint:disable=C0301
#pylint:disable=C0103
from tkinter import Y


Inventory = [loveletter, fuse]
attack = 1
health = 100
PickupKnife = input("You founded a knife! Do you want to pick it up (Y/N) ")
if PickupKnife == 'y':
 print("you got a knife!")
 attack += 10
 Inventory = Inventory, 'knife'
 print(f"your new inventory looks like {Inventory}")
else:
  print("strange choise but your choise ")
zombieHP = 30
zombieATT = 5
encounter = input("Oh no there is a zombie do you wan to attack? ")
if encounter == 'y':
  if PickupKnife == 'y':
    print(f"thank god you picked that knife you hit {attack} hp! ")
    zombieHP -= attack
  else:
    print("I thnik you made a goof man")
    zombieHP -= attack
  print(f"good job now zombie has {zombieHP} HP! but zombie hit you as well! your hp is {health - zombieATT} ")
if zombieHP > 0:
	 encounter = input(f'Oh no Zombie still has {zombieHP}HP left do you want to attak again? ')
	 if encounter == 'y':
	 	  if PickupKnife == 'y':
	 	   print(f'you hit it again now zombie has {zombieHP - attack}HP left')
	 	  else:
	 	   print(f'you hit it zombie has {zombieHP - attack}HP left tho ur knuckles hurt as well {health - 10}')
	 else:
	  print("It is not a good idea to turn your back to a zombie Game Over")
#Chapter 2 exploretion begins
pickupitem = input('Great! you killed the zombie he droped 3 item one of them is bandage other one is key the last one is a fuse whic one do you pick?')
if pickupitem=='1':
  Inventory = [Inventory, 'bandage']
elif pickupitem=='2':
  Inventory = Inventory, 'key'
else:
  Inventory = [Inventory, 'fuse']
  
print(f'Great now you can explore home a bit more{Inventory}')
lroom = ["cabin", "desk"]
bedroom=['bed', 'woredrop', 'window' ]
garage=['fusebox', 'car', 'garage door']
bossrooms=['a thing']
abominationHP=1000
abominationATT=100
#Locked room interaction
if 'key' in Inventory:
  answer=input('You founded a door whic seems to be locked how ever you have the key! want to unlock it? ')
  if answer=='y':
    print('you wander in the room ')
    print(f"you see quite few things {lroom}")
    answer=input('whic one you want to go in? ')
    if answer=='cabin':
      answer=input('you seem to find a gun and few bullets do you want to pick it up? ')
      if answer=='y':
        bullets=5
        Inventory=Inventory, 'gun', 'bullets', bullets
        print(f'your Inventory looks like {Inventory}')
        answer=input('you looked at the desk there is a boltcutter want to take it? ')
        if answer=='y':
          Inventory=Inventory, 'boltcutter'
          print(f'{Inventory} your inventory looks like this ')
        else:
          print('you left the boltcutter ')
      else:
        print('you left the gun inside of the cabin ')  
    else:
      answer=input('you looked at the desk there is a boltcutter want to take it? ')
      if answer == 'y':
        Inventory = Inventory, 'boltcutter'
        print(f'{Inventory} your inventory looks like this ')
        print('you go to the cabin ')
        answer = input('you seem to find a gun and few bullets do you want to pick it up? ')
        if answer == 'y':
         bullets = 5
         Inventory = Inventory, 'gun', 'bullets', bullets
         print(f'{Inventory} your inventory looks like this ')
        else:
          print('you left the gun inside of the cabin ')
      else:
        print('you left the boltcutter')
        print('you go to the cabin')
        answer = input('you seem to find a gun and few bullets do you want to pick it up? ')
        if answer == 'y':
         bullets = 5
         Inventory = Inventory, 'gun', 'bullets', bullets
         print(f'{Inventory} your inventory looks like this ')
        else:
          print('you left the gun inside of the cabin ')
                        
else:
  print('You founded a door whic seems to be locked you started to wander other places ')
print('You seem to find another 2 places bedroom and a garage ')
answer=input('whic one you like to go? ')
if answer=='bedroom':
  print(f'there is {bedroom}')
  answer=input('whic one you like to check ')
  if answer=='bed':
    print('there is nothing usefull ')
    answer=input('where should you check now? window or wordrop ')
    if answer=='window':
      print('you try your hardest but cant seem to open it up ')
      answer=input('you look at the woredrop you find a fuse would you like to pick it up? ')
      if answer=='y':
        Inventory=Inventory, 'fuse'
        print('you picked it up the fuse ')
      else:
       print('you know that you dont have a limited storage right? ')
    else:
      answer = input('you look at the woredrop you find a fuse would you like to pick it up? ')
      if answer=='y':
       Inventory = Inventory, 'fuse'
       print('you picked it up the fuse ')
      else:
        print('you know that you dont have a limited storage right? ')
  elif answer=='window':
    print('you try your hardest but cant seem to open it up ')
    answer=input('where should you checked it? ')
    if answer=='bed':
      print('you cant seem to find anythink usefull ')
      answer = input('you look at the woredrop you find a fuse would you like to pick it up? ')
      if answer == 'y':
       Inventory = Inventory, 'fuse'
       print('you picked it up the fuse ')
      else:
       print('you know that you dont have a limited storage right? ')
    else:
      answer = input('you look at the woredrop you find a fuse would you like to pick it up? ')
      if answer == 'y':
       Inventory = Inventory, 'fuse'
       print('you picked it up the fuse ')
      else:
        print('you know that you dont have a limited storage right? ')
  elif answer=='woredrop':
    answer = input('you look at the woredrop you find a fuse would you like to pick it up? ')
    if answer == 'y':
       Inventory = Inventory, 'fuse'
       print('you picked it up the fuse ')
       answer=input('where would you like to look bed or window ')
       if answer=='bed':
         print('you cant seem to find anything usefull ')
         print('you try to open the window but cant seem to opened it ')
       else:
         print('you try to open the window but cant seem to opened it ')
    else:
       print('you know that you dont have a limited storage right? ')
       answer=input('where would you like to look bed or window ')
       if answer=='bed':
         print('you cant seem to find anything usefull ')
         print('you try to open the window but cant seem to opened it ')
       else:
         print('you try to open the window but cant seem to opened it ')
         print('you cant seem to find anything usefull ')
elif answer=='garage': 
  print(f'you seem to find {garage}')
  answer==input('whic one do you like to go? ')
  if answer=='garage door':
    print('it seems quite heavy you cant lift it with your hand')
    answer=input('you go to the fuse box you saw 3 fuse is missing')
    print(f'you have {Inventory.count("fuse")}')
    if Inventory.count("fuse") == '3':
      print('you opened the door and ecaped')
    else:
      print('you dont have enough fuse it seems')
  else:
   answer = input('you go to the fuse box you saw 3 fuse is missing')
   print(f'you have {Inventory.count("fuse")}')
   if Inventory.count("fuse") == '3':
      print('you opened the door and ecaped')
   else:
     print('you dont have enough fuse it seems')
     print('you walked to the garage door but it seems it is to heavy to lift it')

                 
    
        
        
       
     
      
    

#else: bir ara düzelticem
  #  print("It is not a good idea to turn your back to a zombie Game Over")
    
