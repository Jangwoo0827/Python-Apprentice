from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

# Global dictionary to store definitions
db = {}

def add_definition(db, key, value):
    """
    Add a new definition to the database.

    Parameters:
    - db (dict): The database to add the definition to.
    - key (str): The key for the new definition.
    - value (str): The value for the new definition.

    Returns:
    - None

    If there are already 5 items in the database, an error message is displayed and the new item is not added.
    """
    if len(db) >= 5:
        error("Database Limit Reached", "Cannot add more definitions. The limit of 5 definitions has been reached.")
    else:
        db[key] = value

def delete_definition(db, key):
    """
    Deletes the definition associated with the given key from the database.

    Args:
        db (dict): The database containing the key-value pairs.
        key: The key to be deleted from the database.

    Returns:
        None
    """
    if key in db:
        del db[key]
    else:
        error("Deletion Error", "The selected definition does not exist.")

def is_funny(definition):
    """
    Check if the definition is funny, which means it contains one of the words:

        'fun', 'funny', 'hilarious', 'amusing', 'pants', 'spleen'

    Args:
        definition (str): The definition to check.

    Returns:
        bool: True if the definition contains any of the funny words, False otherwise.
    """
    funny_words = ['fun', 'funny', 'hilarious', 'amusing', 'pants', 'spleen']
    return any(word in definition.lower() for word in funny_words)

def update_listbox(db):
    """
    Update the listbox with the current definitions in the database.

    Returns:
        list of str: A list of strings containing the definitions to be displayed in the listbox.
    """
    l = []
    for key, value in db.items():
        l.append(f"{key}: {value}")
    return l

# Function to add a definition
def _add_definition():
    word = word_entry.value.strip()
    definition = definition_entry.value.strip()
    
    if word and definition:
        if is_funny(definition):
            definition = "😂 " + definition + " 🤡"
        add_definition(db, word, definition)
        _update_listbox()
        word_entry.clear()
        definition_entry.clear()
    else:
        error("Input Error", "Both fields must be filled out.")

# Function to update the listbox with current definitions
def _update_listbox():
    listbox.clear()
    for item in update_listbox(db):
        listbox.append(item)

# Function to delete a definition
def _delete_definition():
    selected_item = listbox.value
    if selected_item:
        word = selected_item.split(":", 1)[0].strip()
        delete_definition(db, word)
        _update_listbox()

# Function to handle enter key press
def handle_enter(event):
    if event.tk_event.keysym == "Return":
        _add_definition()

# Main app
app = App(title="Funny Definitions", width=600, height=300)

# Top pane for input
top_pane = Box(app, align="top", width="fill", border=True)

Text(top_pane, text="Word:", align="left")
word_entry = TextBox(top_pane, width="10", align="left")
Text(top_pane, text="Definition:", width="10", align="left")
definition_entry = TextBox(top_pane, width="25", align="left")
PushButton(top_pane, text="Add", width="5", align="bottom", command=_add_definition)

# Bottom pane for displaying definitions
bottom_pane = Box(app, align="bottom", width="fill", height="fill", border=True)
listbox = ListBox(bottom_pane, items=[], width="fill", height="fill")
PushButton(bottom_pane, text="Delete Selected", command=_delete_definition)

# Bind enter key press event to handle_enter function
app.when_key_pressed = handle_enter

# Initial update of listbox
_update_listbox()

app.display()
