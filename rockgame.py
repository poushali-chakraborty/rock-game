from Tkinter import *
import random

def computer_pick():
	options=["rock","paper","scissors"]
	return random.choice(options)
def game(user,computer):
	if user==computer:
    		return "draw"
  	elif (user=="rock" and computer=="scissors") or (user=="scissors" and computer=="paper") or (user=="paper" and computer=="rock") :
    		return "you win"
  	elif (computer=="rock" and user=="scissors") or (computer=="scissors" and user=="paper") or (computer=="paper" and user=="rock") :
    		return "you lost"
  	else:
   		 	return "error"


root=Tk()
root.title("rock paper scissor")

root["bg"]="white"



lbl_show=Label(root,text="Rock Paper Scissor Game",padx=100,pady=40, fg="red",bg="white")
lbl_show.grid(row=0,column=0,columnspan=3)

lbl_computer=Label(root,text="Computer",padx=50,pady=40, fg="blue",bg="white")
lbl_computer.grid(row=1,column=0)
lbl_user=Label(root,text="User",padx=50,pady=40, fg="blue",bg="white")
lbl_user.grid(row=1,column=2)


logo = PhotoImage(file="robot.gif")
rock = PhotoImage(file="rock.gif")
paper = PhotoImage(file="paper.gif")
scissors = PhotoImage(file="scissors.gif")

computer_image= Label(root, image=logo)
user_image=Label(root, image=logo)

computer_image.grid(row=2,column=0)
user_image.grid(row=2, column=2)


lbl_result=Label(root,text="Result",padx=100,pady=40, fg="red",bg="white")
lbl_result.grid(row=3,column=0,columnspan=3)

def put_computer_image(computer):
	if computer=="rock":
		computer_image["image"]=rock
	elif computer=="paper":
		computer_image["image"]=paper
	elif computer=="scissors":
		computer_image["image"]=scissors
	




def click_rock():
	user_image["image"]=rock
	computer=computer_pick()
	put_computer_image(computer)
	lbl_result["text"]=game("rock",computer)



def click_paper():
	user_image["image"]=paper
	computer=computer_pick()
	put_computer_image(computer)
	lbl_result["text"]=game("paper",computer)
	
def click_scissor():
	user_image["image"]=scissors
	computer=computer_pick()
	put_computer_image(computer)
	lbl_result["text"]=game("scissors",computer)

button_rock=Button(root,text="rock",padx=20,pady=10,command=click_rock)
button_rock.grid(row=4,column=0,padx=20,pady=10)
button_paper=Button(root,text="paper",padx=20,pady=10,command=click_paper)
button_paper.grid(row=4,column=1,padx=20,pady=10)
button_scissor=Button(root,text="scissor",padx=20,pady=10,command=click_scissor)
button_scissor.grid(row=4,column=2,padx=40,pady=10)





root.mainloop()
