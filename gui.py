from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
import os
import random
import requests
import json

FOREGROUND_COLOR = "#B67352"
BACKGROUND_COLOR = "#EADFB4"

API_KEY = os.environ["API_KEY"]
paramaters = {"apiKey" : API_KEY,
              }

FONT = ("Georgia", 45, "bold")

# num = random.randint(1,4)

BUTTON_STYLE = {
    "font": ("Georgia", 45, "bold"),
    "foreground": "#B67352",
    "background": "#EADFB4",
    "activeforeground": FOREGROUND_COLOR,
    "activebackground": BACKGROUND_COLOR,
    "borderless": 1,
    "relief": "ridge",
    "width": 350,
    "height": 100,
}

BUTTON_STYLE2 = {
    "font": ("Georgia", 45, "bold"),
    "foreground": "#B67352",
    "background": "#EADFB4",
    "activeforeground": FOREGROUND_COLOR,
    "activebackground": BACKGROUND_COLOR,
    "borderless": 1,
    "relief": "ridge",
    "width": 500,
    "height": 100,
}
BUTTON_STYLE3 = {
    "font": ("Georgia", 45, "bold"),
    "foreground": "#B67352",
    "background": "#EADFB4",
    "activeforeground": FOREGROUND_COLOR,
    "activebackground": BACKGROUND_COLOR,
    "borderless": 1,
    "relief": "ridge",
    "width": 800,
    "height": 100,
}


class Gui():
    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x500+300+100")
        self.root.wm_resizable(False,False)
        self.background_image = PhotoImage(file=f"./assets/background4.png")
        self.background_label = Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1,relheight=1)
        self.start_screen()
        self.root.mainloop()


    def start_screen(self):

        self.find_recipe = Button(self.root, text="Find Recipe",command=self.find_button)
        self.find_recipe.configure(BUTTON_STYLE)
        self.find_recipe.place(x=10,y=10)
        self.create_recipe = Button(self.root, text="Create Recipe",command=self.create_button)
        self.create_recipe.configure(BUTTON_STYLE)
        self.create_recipe.place(x=440,y=10)

    def create_button(self):
        self.find_recipe.place_forget()
        self.create_recipe.place_forget()
        self.textbox = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox.insert(0, "Ingredient 1")
        self.textbox.bind("<FocusOut>", self.on_focus_out)
        self.textbox.bind("<FocusIn>", self.on_entry_click)
        self.textbox.place(x=10, y=10)

        self.textbox2 = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox2.insert(0, "Ingredient 2")
        self.textbox2.bind("<FocusOut>", self.on_focus_out2)
        self.textbox2.bind("<FocusIn>", self.on_entry_click2)
        self.textbox2.place(x=10, y=80)

        self.textbox3 = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox3.insert(0, "Ingredient 3")
        self.textbox3.bind("<FocusOut>", self.on_focus_out3)
        self.textbox3.bind("<FocusIn>", self.on_entry_click3)
        self.textbox3.place(x=10, y=150)

        self.textbox4 = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox4.insert(0, "Ingredient 4")
        self.textbox4.bind("<FocusOut>", self.on_focus_out4)
        self.textbox4.bind("<FocusIn>", self.on_entry_click4)
        self.textbox4.place(x=10, y=220)

        self.textbox_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox_amount.insert(0, "Add Amount")
        self.textbox_amount.bind("<FocusOut>", self.on_focus_out_amount)
        self.textbox_amount.bind("<FocusIn>", self.on_entry_click_amount)
        self.textbox_amount.place(x=360, y=10)

        self.textbox2_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox2_amount.insert(0, "Add Amount")
        self.textbox2_amount.bind("<FocusOut>", self.on_focus_out2_amount)
        self.textbox2_amount.bind("<FocusIn>", self.on_entry_click2_amount)
        self.textbox2_amount.place(x=360, y=80)

        self.textbox3_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox3_amount.insert(0, "Add Amount")
        self.textbox3_amount.bind("<FocusOut>", self.on_focus_out3_amount)
        self.textbox3_amount.bind("<FocusIn>", self.on_entry_click3_amount)
        self.textbox3_amount.place(x=360, y=150)

        self.textbox4_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox4_amount.insert(0, "Add Amount")
        self.textbox4_amount.bind("<FocusOut>", self.on_focus_out4_amount)
        self.textbox4_amount.bind("<FocusIn>", self.on_entry_click4_amount)
        self.textbox4_amount.place(x=360, y=220)

        self.back_button5 = Button(self.root, text="Go Back", command=self.back_to_menu5)
        self.back_button5.configure(BUTTON_STYLE2)
        self.back_button5.place(x=150, y=390)

        self.add_description = Button(self.root, text="Add Description",command=self.recipe_description)
        self.add_description.configure(BUTTON_STYLE2)
        self.add_description.place(x=150, y=290)

    def recipe_description(self):
        self.back_button5.place_forget()
        self.textbox.place_forget()
        self.textbox2.place_forget()
        self.textbox3.place_forget()
        self.textbox4.place_forget()
        self.textbox_amount.place_forget()
        self.textbox2_amount.place_forget()
        self.textbox3_amount.place_forget()
        self.textbox4_amount.place_forget()
        self.add_description.place_forget()

        self.INGREDIENT1 = self.textbox.get()
        self.INGREDIENT2 = self.textbox2.get()
        self.INGREDIENT3 = self.textbox3.get()
        self.INGREDIENT4 = self.textbox4.get()

        self.AMOUNT1 = self.textbox_amount.get()
        self.AMOUNT2 = self.textbox2_amount.get()
        self.AMOUNT3 = self.textbox3_amount.get()
        self.AMOUNT4 = self.textbox4_amount.get()

        if self.INGREDIENT1 == "Ingredient 1":
            self.INGREDIENT1 = ""
        if self.INGREDIENT2 == "Ingredient 2":
            self.INGREDIENT2 = ""
        if self.INGREDIENT3 == "Ingredient 3":
            self.INGREDIENT3 = ""
        if self.INGREDIENT4 == "Ingredient 4":
            self.INGREDIENT4 = ""

        if self.AMOUNT1 == "Add Amount":
            self.AMOUNT1 = ""
        if self.AMOUNT2 == "Add Amount":
            self.AMOUNT2 = ""
        if self.AMOUNT3 == "Add Amount":
            self.AMOUNT3 = ""
        if self.AMOUNT4 == "Add Amount":
            self.AMOUNT4 = ""

        print(self.INGREDIENT1,self.INGREDIENT2,self.INGREDIENT3,self.INGREDIENT4)
        print(self.AMOUNT1,self.AMOUNT2,self.AMOUNT3,self.AMOUNT4)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.description = Text(self.root, width=int(screen_width / 10), height=int(screen_height / 20), fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 20), wrap="word")
        self.description.insert("1.0", "Your Description Here: ")

        self.description.mark_set("insert", "1.0")
        self.description.tag_add("start", "1.0", "1.end")
        self.description.tag_config("start", justify="left")

        self.description.pack(fill="both", expand=True)

        self.back_button6 = Button(self.root, text="Go Back", command=self.back_to_menu6)
        self.back_button6.configure(BUTTON_STYLE2)
        self.back_button6.place(x=150, y=390)

        self.add_recipe = Button(self.root, text="Add Recipe", command=self.add_recipe_function)
        self.add_recipe.configure(BUTTON_STYLE2)
        self.add_recipe.place(x=150, y=290)

    def add_recipe_function(self):
        messagebox.showinfo("showinfo", "Recipe Added Succesfully!")
        self.user_description = self.description.get("1.0", "end-1c")
        self.description.destroy()
        self.add_recipe.place_forget()
        self.back_button6.place_forget()

        self.find_recipe = Button(self.root, text="Find Recipe", command=self.find_button)
        self.find_recipe.configure(BUTTON_STYLE)
        self.find_recipe.place(x=10, y=10)
        self.create_recipe = Button(self.root, text="Create Recipe", command=self.create_button)
        self.create_recipe.configure(BUTTON_STYLE)
        self.create_recipe.place(x=440, y=10)

        print(self.INGREDIENT1, self.INGREDIENT2, self.INGREDIENT3, self.INGREDIENT4)
        print(self.AMOUNT1, self.AMOUNT2, self.AMOUNT3, self.AMOUNT4)
        print(self.user_description)





        ### take ingredients, amounts and description and post it online

    def back_to_menu6(self):
        self.back_button6.place_forget()
        self.description.pack_forget()
        self.add_recipe.place_forget()
        self.textbox = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox.insert(0, "Ingredient 1")
        self.textbox.bind("<FocusOut>", self.on_focus_out)
        self.textbox.bind("<FocusIn>", self.on_entry_click)
        self.textbox.place(x=10, y=10)

        self.textbox2 = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox2.insert(0, "Ingredient 2")
        self.textbox2.bind("<FocusOut>", self.on_focus_out2)
        self.textbox2.bind("<FocusIn>", self.on_entry_click2)
        self.textbox2.place(x=10, y=80)

        self.textbox3 = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox3.insert(0, "Ingredient 3")
        self.textbox3.bind("<FocusOut>", self.on_focus_out3)
        self.textbox3.bind("<FocusIn>", self.on_entry_click3)
        self.textbox3.place(x=10, y=150)

        self.textbox4 = Entry(self.root, width=10, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox4.insert(0, "Ingredient 4")
        self.textbox4.bind("<FocusOut>", self.on_focus_out4)
        self.textbox4.bind("<FocusIn>", self.on_entry_click4)
        self.textbox4.place(x=10, y=220)

        self.textbox_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox_amount.insert(0, "Add Amount")
        self.textbox_amount.bind("<FocusOut>", self.on_focus_out_amount)
        self.textbox_amount.bind("<FocusIn>", self.on_entry_click_amount)
        self.textbox_amount.place(x=360, y=10)

        self.textbox2_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox2_amount.insert(0, "Add Amount")
        self.textbox2_amount.bind("<FocusOut>", self.on_focus_out2_amount)
        self.textbox2_amount.bind("<FocusIn>", self.on_entry_click2_amount)
        self.textbox2_amount.place(x=360, y=80)

        self.textbox3_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox3_amount.insert(0, "Add Amount")
        self.textbox3_amount.bind("<FocusOut>", self.on_focus_out3_amount)
        self.textbox3_amount.bind("<FocusIn>", self.on_entry_click3_amount)
        self.textbox3_amount.place(x=360, y=150)

        self.textbox4_amount = Entry(self.root, width=13, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox4_amount.insert(0, "Add Amount")
        self.textbox4_amount.bind("<FocusOut>", self.on_focus_out4_amount)
        self.textbox4_amount.bind("<FocusIn>", self.on_entry_click4_amount)
        self.textbox4_amount.place(x=360, y=220)

        self.back_button5 = Button(self.root, text="Go Back", command=self.back_to_menu5)
        self.back_button5.configure(BUTTON_STYLE2)
        self.back_button5.place(x=150, y=390)

        self.add_description = Button(self.root, text="Add Description", command=self.recipe_description)
        self.add_description.configure(BUTTON_STYLE2)
        self.add_description.place(x=150, y=290)

    def back_to_menu5(self):
        self.back_button5.destroy()
        self.textbox.place_forget()
        self.textbox2.place_forget()
        self.textbox3.place_forget()
        self.textbox4.place_forget()
        self.textbox_amount.place_forget()
        self.textbox2_amount.place_forget()
        self.textbox3_amount.place_forget()
        self.textbox4_amount.place_forget()
        self.add_description.place_forget()

        self.find_recipe = Button(self.root, text="Find Recipe", command=self.find_button)
        self.find_recipe.configure(BUTTON_STYLE)
        self.find_recipe.place(x=10, y=10)
        self.create_recipe = Button(self.root, text="Create Recipe", command=self.create_button)
        self.create_recipe.configure(BUTTON_STYLE)
        self.create_recipe.place(x=440, y=10)

    def find_button(self):
        self.find_recipe.destroy()
        self.create_recipe.destroy()

        self.search_ingredient = Button(self.root, text="Search By Ingredient", command=self.search_by_ingredient)
        self.search_ingredient.configure(BUTTON_STYLE2)
        self.search_ingredient.place(x=150, y=10)

        self.back_button = Button(self.root, text="Go Back", command=self.back_to_menu)
        self.back_button.configure(BUTTON_STYLE2)
        self.back_button.place(x=150, y=380)

    def search_by_ingredient(self):

        self.search_ingredient.place_forget()
        self.back_button.place_forget()

        self.textbox = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"),justify="center")
        self.textbox.insert(0, "Ingredient 1")
        self.textbox.bind("<FocusOut>", self.on_focus_out)
        self.textbox.bind("<FocusIn>", self.on_entry_click)
        self.textbox.place(x=10, y=10)

        self.textbox2 = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"),justify="center")
        self.textbox2.insert(0, "Ingredient 2")
        self.textbox2.bind("<FocusOut>", self.on_focus_out2)
        self.textbox2.bind("<FocusIn>", self.on_entry_click2)
        self.textbox2.place(x=10, y=80)

        self.textbox3 = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"),justify="center")
        self.textbox3.insert(0, "Ingredient 3")
        self.textbox3.bind("<FocusOut>", self.on_focus_out3)
        self.textbox3.bind("<FocusIn>", self.on_entry_click3)
        self.textbox3.place(x=10, y=150)

        self.textbox4 = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"),justify="center")
        self.textbox4.insert(0, "Ingredient 4")
        self.textbox4.bind("<FocusOut>", self.on_focus_out4)
        self.textbox4.bind("<FocusIn>", self.on_entry_click4)
        self.textbox4.place(x=10, y=220)

        self.back_button2 = Button(self.root, text="Go Back", command=self.back_to_menu2)
        self.back_button2.configure(BUTTON_STYLE2)
        self.back_button2.place(x=150, y=390)

        self.activate_search = Button(self.root, text="Search Recipes",command=self.search_input_ingredient_button)
        self.activate_search.configure(BUTTON_STYLE2)
        self.activate_search.place(x=150, y=290)

    def on_entry_click(self, event):
        if self.textbox.get() == "Ingredient 1":
            self.textbox.delete(0, "end")
            self.textbox.config(fg="#B67352", justify="center")

    def on_entry_click_amount(self, event):
        if self.textbox_amount.get() == "Add Amount":
            self.textbox_amount.delete(0, "end")
            self.textbox_amount.config(fg="#B67352", justify="center")

    def on_focus_out(self, event):
        if self.textbox.get() == "":
            self.textbox.insert(0, "Ingredient 1")
            self.textbox.configure(fg="#B67352", justify="center")

    def on_focus_out_amount(self, event):
        if self.textbox_amount.get() == "":
            self.textbox_amount.insert(0, "Add Amount")
            self.textbox_amount.configure(fg="#B67352", justify="center")

    def on_entry_click2(self, event):
        if self.textbox2.get() == "Ingredient 2":
            self.textbox2.delete(0, "end")
            self.textbox2.config(fg="#B67352", justify="center")

    def on_focus_out2(self, event):
        if self.textbox2.get() == "":
            self.textbox2.insert(0, "Ingredient 2")
            self.textbox2.configure(fg="#B67352", justify="center")

    def on_entry_click3(self, event):
        if self.textbox3.get() == "Ingredient 3":
            self.textbox3.delete(0, "end")
            self.textbox3.config(fg="#B67352", justify="center")

    def on_focus_out3(self, event):
        if self.textbox3.get() == "":
            self.textbox3.insert(0, "Ingredient 3")
            self.textbox3.configure(fg="#B67352", justify="center")

    def on_entry_click4(self, event):
        if self.textbox4.get() == "Ingredient 4":
            self.textbox4.delete(0, "end")
            self.textbox4.config(fg="#B67352", justify="center")

    def on_focus_out4(self, event):
        if self.textbox4.get() == "":
            self.textbox4.insert(0, "Ingredient 4")
            self.textbox4.configure(fg="#B67352", justify="center")

    def on_entry_click2_amount(self, event):
        if self.textbox2_amount.get() == "Add Amount":
            self.textbox2_amount.delete(0, "end")
            self.textbox2_amount.config(fg="#B67352", justify="center")

    def on_focus_out2_amount(self, event):
        if self.textbox2_amount.get() == "":
            self.textbox2_amount.insert(0, "Add Amount")
            self.textbox2_amount.configure(fg="#B67352", justify="center")

    def on_entry_click3_amount(self, event):
        if self.textbox3_amount.get() == "Add Amount":
            self.textbox3_amount.delete(0, "end")
            self.textbox3_amount.config(fg="#B67352", justify="center")

    def on_focus_out3_amount(self, event):
        if self.textbox3_amount.get() == "":
            self.textbox3_amount.insert(0, "Add Amount")
            self.textbox3_amount.configure(fg="#B67352", justify="center")

    def on_entry_click4_amount(self, event):
        if self.textbox4_amount.get() == "Add Amount":
            self.textbox4_amount.delete(0, "end")
            self.textbox4_amount.config(fg="#B67352", justify="center")

    def on_focus_out4_amount(self, event):
        if self.textbox4_amount.get() == "":
            self.textbox4_amount.insert(0, "Add Amount")
            self.textbox4_amount.configure(fg="#B67352", justify="center")

    def back_to_menu(self):
        self.search_ingredient.destroy()
        self.back_button.destroy()

        self.find_recipe = Button(self.root, text="Find Recipe", command=self.find_button)
        self.find_recipe.configure(BUTTON_STYLE)
        self.find_recipe.place(x=10, y=10)
        self.create_recipe = Button(self.root, text="Create Recipe", command=self.create_button)
        self.create_recipe.configure(BUTTON_STYLE)
        self.create_recipe.place(x=440, y=10)

    def back_to_menu2(self):
        self.back_button2.place_forget()
        self.textbox.place_forget()
        self.textbox2.place_forget()
        self.textbox3.place_forget()
        self.textbox4.place_forget()
        self.activate_search.place_forget()

        self.search_ingredient = Button(self.root, text="Search By Ingredient", command=self.search_by_ingredient)
        self.search_ingredient.configure(BUTTON_STYLE2)
        self.search_ingredient.place(x=150, y=10)

        self.back_button = Button(self.root, text="Go Back", command=self.back_to_menu)
        self.back_button.configure(BUTTON_STYLE2)
        self.back_button.place(x=150, y=380)

    def search_input_ingredient_button(self):

        self.textbox.place_forget()
        self.textbox2.place_forget()
        self.textbox3.place_forget()
        self.textbox4.place_forget()
        self.back_button2.place_forget()
        self.activate_search.place_forget()

        self.canvas = Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)

        frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=frame, anchor="nw")

        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.place(x=790, y=10, width=10, height=500)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        INGREDIENT1 = self.textbox.get()
        INGREDIENT2 = self.textbox2.get()
        INGREDIENT3 = self.textbox3.get()
        INGREDIENT4 = self.textbox4.get()

        response = requests.get(
            f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={INGREDIENT1},{INGREDIENT2},{INGREDIENT3},{INGREDIENT4}&number=15&ranking=2&apiKey={API_KEY}")

        if response.status_code == 200:

            data = response.json()

            list_of_recipes = []
            list_of_names = []
            list_of_ingredients = []
            self.food_dict = {}
            row=0
            self.recipe_buttons = []

            for result in data:
                recipe_name = result["title"]
                list_of_recipes.append(recipe_name)

                for ingredient in result["missedIngredients"]:
                    name = ingredient["name"]
                    list_of_names.append(name)
                    amount = ingredient["original"]
                    list_of_ingredients.append(amount)

                self.recipe_button = Button(frame, text=recipe_name, anchor="w",command=lambda t=recipe_name: self.on_button_click(t))
                self.recipe_button.configure(BUTTON_STYLE3)
                self.recipe_button.grid(row=row, column=0, sticky="ew")
                self.recipe_buttons.append(self.recipe_button)
                row += 1

                self.food_dict = {**self.food_dict, recipe_name: (list_of_names,list_of_ingredients)}
                list_of_names = []
                list_of_ingredients = []

            print(self.food_dict)

            self.back_button3 = Button(frame, text="Go Back", command=self.back_to_menu3)
            self.back_button3.configure(BUTTON_STYLE3)
            self.back_button3.grid(row=row, column=0, sticky="ew")

            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))


        else:
            print("Error:", response.status_code)



        def on_mousewheel(event):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

        self.canvas.bind_all("<MouseWheel>", on_mousewheel)


    def back_to_menu3(self):
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.canvas.unbind_all("<MouseWheel>")

        self.textbox = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox.insert(0, "Ingredient 1")
        self.textbox.bind("<FocusOut>", self.on_focus_out)
        self.textbox.bind("<FocusIn>", self.on_entry_click)
        self.textbox.place(x=10, y=10)

        self.textbox2 = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox2.insert(0, "Ingredient 2")
        self.textbox2.bind("<FocusOut>", self.on_focus_out2)
        self.textbox2.bind("<FocusIn>", self.on_entry_click2)
        self.textbox2.place(x=10, y=80)

        self.textbox3 = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox3.insert(0, "Ingredient 3")
        self.textbox3.bind("<FocusOut>", self.on_focus_out3)
        self.textbox3.bind("<FocusIn>", self.on_entry_click3)
        self.textbox3.place(x=10, y=150)

        self.textbox4 = Entry(self.root, width=24, fg="#B67352", bg=BACKGROUND_COLOR, font=("Georgia", 45, "bold"), justify="center")
        self.textbox4.insert(0, "Ingredient 4")
        self.textbox4.bind("<FocusOut>", self.on_focus_out4)
        self.textbox4.bind("<FocusIn>", self.on_entry_click4)
        self.textbox4.place(x=10, y=220)

        self.back_button2 = Button(self.root, text="Go Back", command=self.back_to_menu2)
        self.back_button2.configure(BUTTON_STYLE2)
        self.back_button2.place(x=150, y=390)

        self.activate_search = Button(self.root, text="Search Recipes", command=self.search_input_ingredient_button)
        self.activate_search.configure(BUTTON_STYLE2)
        self.activate_search.place(x=150, y=290)

    def on_button_click(self, text):
        print(f"Button '{text}' clicked")
        recipe_to_show = text
        if recipe_to_show in self.food_dict:


            def wrap_text(text, width):
                return '\n'.join(text[i:i + width] for i in range(0, len(text), width))

            self.canvas2 = Canvas(self.root, bg=BACKGROUND_COLOR, highlightbackground=FOREGROUND_COLOR)
            self.canvas2.place(x=0, y=0, height=500, width=800)

            recipe_title = recipe_to_show
            recipe_name_label = Label(self.canvas2, text=recipe_title, font=("Georgia", 40, "bold"), bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR)
            recipe_name_label.place(relx=0.5, y=25, anchor="center")

            ingredients = self.food_dict[recipe_to_show][0]
            amounts = self.food_dict[recipe_to_show][1]

            ingredients_text = wrap_text("\n".join(ingredients), 200)
            amounts_text = wrap_text("\n".join(amounts), 500)

            ingredients_label = Label(self.canvas2, text=ingredients_text, font=("Georgia", 24), bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, justify="left", anchor="nw")
            ingredients_label.place(x=20, y=60)

            amounts_label = Label(self.canvas2, text=amounts_text, font=("Georgia", 24), bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR, justify="left", anchor="nw")
            amounts_label.place(x=300, y=60)

            self.back_button4 = Button(self.root, text="Go Back", command=self.back_to_recipes)
            self.back_button4.configure(BUTTON_STYLE2)
            self.back_button4.place(x=150, y=390)


    def back_to_recipes(self):
        self.canvas2.destroy()
        self.back_button4.place_forget()


### when add recipe is clicked it should take the ingredients, the amounts and the description and post it online, maybe send a messagebox saying recipe added
