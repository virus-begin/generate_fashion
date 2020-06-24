import random

shirts = ["Black", "Green", "Blue", "Light Blue", "Red", "Gray"]
pants = ["Black", "Blue", "Gray", "Kaki", "Green"]
combined_array  = []

def random_selection(max_number):
    return random.randint(1, max_number)

def generate_fashion():
    global shirts,pants,combined_array
    shirts_count = len(shirts)
    pants_count = len(pants)
    pant_selection = random_selection(pants_count - 1)
    shirt_selection = random_selection(shirts_count - 1)
    selection = {}
    selection["shirt"] = shirts[shirt_selection]
    selection["pant"] = pants[pant_selection]
    combined_array.append(selection)
    del shirts[shirt_selection]
    del pants[pant_selection]
    

def intial():
    for i in range(4):
        generate_fashion()
    print(combined_array)
    
intial()