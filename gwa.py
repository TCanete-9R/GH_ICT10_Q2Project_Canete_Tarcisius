from pyscript import display, document

def compute(e):
    output = document.getElementById("output")
    output.innerHTML = ""

    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    subjects = ["Filipino", "English", "Math", "Science", "Social Studies", "PE"]
    units = (3, 5, 5, 4, 3, 1)

    grades = [
        int(document.getElementById("filipino").value),
        int(document.getElementById("english").value),
        int(document.getElementById("math").value),
        int(document.getElementById("science").value),
        int(document.getElementById("social_studies").value),
        int(document.getElementById("pe").value)
    ]

    total_units = sum(units)
    weighted = sum(g * u for g, u in zip(grades, units))
    gwa = weighted / total_units

    display(f"Name: {fname} {lname}", target="output")
    display(f"GWA: {gwa:.2f}", target="output")