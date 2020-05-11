import tkinter as tk
from requirements import requirement 

# requirement
time = requirement()
#---------------------------------------------my function ----------------------------------------------

        #search_handel
def search_handel() :
    all_word_gui = time.read_file()
    search_key = entry_search.get()

    lbl_result["text"] = time.search_in_file(search_key)


        
def add_handel() :
    key = entry_new_word.get()
    val = entry_meaning.get()

    lbl_result_add["text"] = time.write_in_file(key,val)
        
    #add_word handel
def update_handel() :
        
        all_word_gui = time.read_file()

        update_key = entry_word_update.get()
        update_val = entry_meaning_update.get()

        time.Update_file(update_key,update_val)

        lbl_result_update["text"] =  "Updated"
        
    


#---------------------------------------------make gui----------------------------------------------
 

window = tk.Tk()
window.title("dict by python ex1")


frame_search = tk.Frame(master=window,
            relief=tk.RAISED,
            borderwidth=1)
frame_search.grid(row=0, column=3, padx=5, pady=5)


frame_new_word = tk.Frame(master=window,
            relief=tk.RAISED,
            borderwidth=1)
frame_new_word.grid(row=1, column=3, padx=5, pady=5)


frame_update = tk.Frame(master=window,
            relief=tk.RAISED,
            borderwidth=1)
frame_update.grid(row=2, column=3, padx=5, pady=5)


#-------------------------------------------search_gui------------------------------------------------

entry_search = tk.Entry(master=frame_search ,fg="yellow", bg="#7b7b7b")
entry_search.grid(row=0, column=1, padx=5, pady=5)

lbl_result = tk.Label(master=frame_search, text="here you can see the meaning of word")
lbl_result.grid(row=0, column=4, padx=5, pady=5)


button_search = tk.Button(master=frame_search,text="Find the meaning",
    foreground="white",  
    background="#34A2FE",  
    command=search_handel
    )
button_search.grid(row=0, column=2, padx=5, pady=5)

#-----------------------------------------add_word gui--------------------------------------------------

lbl_word = tk.Label(master=frame_new_word, text="New word")
lbl_word.grid(row=1, column=0, padx=5, pady=5)

entry_new_word = tk.Entry(master=frame_new_word ,fg="yellow", bg="#7b7b7b")
entry_new_word.grid(row=1, column=1, padx=5, pady=5)

lbl_meaning = tk.Label(master=frame_new_word, text="Meaning")
lbl_meaning.grid(row=1, column=2, padx=5, pady=5)

entry_meaning = tk.Entry(master=frame_new_word ,fg="yellow", bg="#7b7b7b")
entry_meaning.grid(row=1, column=3, padx=5, pady=5)

button_search = tk.Button(master=frame_new_word,text="Add my word",
    foreground="white",  
    background="#34A2FE",  
    command=add_handel
    )
button_search.grid(row=1, column=4, padx=5, pady=5)

lbl_result_add = tk.Label(master=frame_new_word, text="Result")
lbl_result_add.grid(row=1, column=5, padx=5, pady=5)

#-----------------------------------------update--------------------------------------------------

lbl_word_update = tk.Label(master=frame_update, text="word")
lbl_word_update.grid(row=2, column=0, padx=5, pady=5)

entry_word_update = tk.Entry(master=frame_update ,fg="yellow", bg="#7b7b7b")
entry_word_update.grid(row=2, column=1, padx=5, pady=5)

lbl_meaning_update = tk.Label(master=frame_update, text="Meaning")
lbl_meaning_update.grid(row=2, column=2, padx=5, pady=5)

entry_meaning_update = tk.Entry(master=frame_update ,fg="yellow", bg="#7b7b7b")
entry_meaning_update.grid(row=2, column=3, padx=5, pady=5)

button_update = tk.Button(master=frame_update,text="update",
    foreground="white",  
    background="#34A2FE",  
    command=update_handel
    )
button_update.grid(row=2, column=4, padx=5, pady=5)

lbl_result_update = tk.Label(master=frame_update, text="Result")
lbl_result_update.grid(row=2, column=5, padx=5, pady=5)

#exit
button_update = tk.Button(master=window,text="exit",
    foreground="white",  
    background="#34A2FE",  
    command=window.destroy
    )
button_update.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()




   







window.mainloop()










