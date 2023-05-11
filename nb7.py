my_message = "Welcome to {COLLEGE} {NAME} ! I will be handling {SUBJECT}."
COLLEGE = "JAIN UNIVERSITY"
NAME = "STUDENTS"
SUBJECT = "PYTHON"
my_message_a = my_message.format(**{"COLLEGE":COLLEGE, "NAME":NAME, "SUBJECT":SUBJECT})
print(my_message_a)