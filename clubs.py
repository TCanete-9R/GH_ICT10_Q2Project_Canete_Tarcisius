from pyscript import display, document

art_club = {
    "Description": "To develop their drawing skills and to express their feelings",
    "Meeting Time": "Tuesday & Thursday 3:00 to 5:00 PM",
    "Location": "Music Room",
    "Club Moderator": "Ms. Suarez",
    "Number of Members": 30,
    "Category": "Non-Academic"
}

v_ball = {
    "Description": "Training and skills development for volleyball players.",
    "Meeting Time": "Tuesday 3:00 to 5:00 PM",
    "Location": "Quadrangle/MM Hall",
    "Club Moderator": "Mr. Gervacio",
    "Number of Members": 30,
    "Category": "Non-Academic"
}

monarchs = {
    "Description": "A group for students who enjoy dancing and performing.",
    "Meeting Time": "Mondays & Thursdays 3:00 to 5:00 PM",
    "Location": "MM Hall",
    "Club Moderator": "Mr. Marutani",
    "Number of Members": 20,
    "Category": "Non-Academic"
}

b_ball = {
    "Description": "Training and skills development for basketball players.",
    "Meeting Time": "Monday 3:00 to 5:00 PM",
    "Location": "Quadrangle/MM Hall",
    "Club Moderator": "Mr. Amargo",
    "Number of Members": 30,
    "Category": "Non-Academic"
}

glee_club = {
    "Description": "To enhance singing voices and to express how they feel",
    "Meeting Time": "Monday & Tuesday 3:00 to 4:30 PM",
    "Location": "Music Room",
    "Club Moderator": "Ms. Bayola",
    "Number of Members": 38,
    "Category": "Non-Academic"
}

def art(e):
    document.getElementById('output').innerHTML = ""
    
    art = f'''
    Art Club 
        Description: {art_club["Description"]}
        Meeting Time: {art_club["Meeting Time"]}
        Location: {art_club["Location"]}
        Club Moderator: {art_club["Club Moderator"]}
        Number of Members: {art_club["Number of Members"]}
        Category: {art_club["Category"]}
    '''
    display(art, target='output')

def vball(e):
    document.getElementById('output').innerHTML = ""
    
    vball = f'''
    Volleyball Club 
        Description: {v_ball["Description"]}
        Meeting Time: {v_ball["Meeting Time"]}
        Location: {v_ball["Location"]}
        Club Moderator: {v_ball["Club Moderator"]}
        Number of Members: {v_ball["Number of Members"]}
        Category: {v_ball["Category"]}
    '''
    display(vball, target='output')

def monarch(e):
    document.getElementById('output').innerHTML = ""
    
    monarch = f'''
    Monarchs Club
        Description: {monarchs["Description"]}
        Meeting Time: {monarchs["Meeting Time"]}
        Location: {monarchs["Location"]}
        Club Moderator: {monarchs["Club Moderator"]}
        Number of Members: {monarchs["Number of Members"]}
        Category: {monarchs["Category"]}
    '''
    display(monarch, target='output')

def bball(e):
    document.getElementById('output').innerHTML = ""
    
    bball = f'''
    Basketball Club 
        Description: {b_ball["Description"]}
        Meeting Time: {b_ball["Meeting Time"]}
        Location: {b_ball["Location"]}
        Club Moderator: {b_ball["Club Moderator"]}
        Number of Members: {b_ball["Number of Members"]}
        Category: {b_ball["Category"]}
    '''
    display(bball, target='output')

def glee(e):
    document.getElementById('output').innerHTML = ""
    
    glee = f'''
    Glee Club 
        Description: {glee_club["Description"]}
        Meeting Time: {glee_club["Meeting Time"]}
        Location: {glee_club["Location"]}
        Club Moderator: {glee_club["Club Moderator"]}
        Number of Members: {glee_club["Number of Members"]}
        Category: {glee_club["Category"]}
    '''
    display(glee, target='output')

