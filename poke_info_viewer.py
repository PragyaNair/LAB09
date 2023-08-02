from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import poke_api


# Create the main window

root = Tk()

root.title("Pokemon Information")


# TODO: Create the frames

info_frame = ttk.LabelFrame(root, text="Info")

info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


stats_frame = ttk.LabelFrame(root, text="Stats")

stats_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


user_input_frame = ttk.Frame(root)

user_input_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


# TODO: Populate the user input frame with widgets

pokemon_name_label = ttk.Label(user_input_frame, text="Pokémon Name:")

pokemon_name_label.grid(row=0, column=0, padx=5, pady=5)


pokemon_name_entry = ttk.Entry(user_input_frame)

pokemon_name_entry.grid(row=0, column=1, padx=5, pady=5)


get_info_button = ttk.Button(user_input_frame, text="Get Info", command=fetch_pokemon_info)

get_info_button.grid(row=0, column=2, padx=5, pady=5)


# TODO: Define button click event handler function

def fetch_pokemon_info():

    pokemon_name = pokemon_name_entry.get()

    if not pokemon_name:

        messagebox.showerror("Error", "Please enter a Pokémon name.")

    else:

        pokemon_info = poke_api.get_pokemon_info(pokemon_name)

        if not pokemon_info:

            messagebox.showerror("Error", f"Invalid Pokémon name: {pokemon_name}")

        else:

            display_pokemon_info(pokemon_info)


def display_pokemon_info(pokemon_info):

    # TODO: Populate the Info and Stats frames with retrieved Pokemon information

    pass


root.mainloop