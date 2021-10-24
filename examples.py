dict = {
    "Kenneth" : "Computer Science", 
    "Aubrey" : "Chemical Engineering",
    "Donna" : "Electrical Engineering",
    "Gwyn" : "Organizational Communication",
    "Alhonzo" : "Speech Pathologist",
    "Rafael" : "Geologist", 
    "Lyka" : "Medical Technologist"
}

string = '=== List of Discord Members Plus their Courses ===\n'
for name, course in dict.items():
    string += f'{name} is taking {course} as her/his course.\n'

fileHandle = open("hello", "w")
fileHandle.write(string)
fileHandle.close()