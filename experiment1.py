# Experiment 1: Knowledge Representation Using Python
# Aim: To represent facts about a student using a Python dictionary and display the stored knowledge.

student = {
    "name": "Arun",
    "department": "CSE",
    "course": "Python Programming",
    "year": 2,
}

print("Student Knowledge Representation")
for key, value in student.items():
    print(key, ":", value)
