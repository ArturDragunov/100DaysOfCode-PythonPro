################
#### Day 27 ####
################

from tkinter import *
def button_clicked():
  print("I got clicked")
  new_text = input.get()
  my_label.config(text=new_text) # to setup/change text in label

window = Tk()

window.title('My First GUI Program')
window.minsize(width = 500, height=300)
window.config(padx=100, pady=200) # boundary -> you add space around your widgets so that they don't crash together

#Label
my_label = Label(text = 'I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack() # to make the label visible

my_label['text'] = 'New Text'
my_label.config(text="New Text")
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
button = Button(text="Click Me", command=button_clicked) # we add NAME of the function and we are not calling the function (so, no parantheses at the end)
button.grid(column=1, row=1)
# With Parentheses: Use parentheses when you want to call the function immediately and pass its return value as a parameter.
# Without Parentheses: Use the function name without parentheses when you want to pass the function itself as a parameter, to be called later (e.g., as a callback or event handler).
# In your example, command=button_clicked passes the function button_clicked to be called when the button is clicked, so no parentheses are used.
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())











window.mainloop()