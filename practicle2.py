print("Student Course Suggestion System")
print("Subjects you can choose from:")
print("1. maths 2. physics 3. programming 4. graphics 5. circuits 6. statistics 7. ai")
fav1 = input("Enter your favorite subject first (subject should only be maths or statistics): ").strip().upper()
fav2 = input("Enter your favorite subject second: ").strip().upper()
if fav1 == "MATHS" and fav2 == "PHYSICS":
   print("You can choose Engineering Science.")
elif fav1 == "MATHS" and fav2 == "PROGRAMMING":
   print("You can choose Computer Science.")
elif fav1 == "MATHS" and fav2 == "GRAPHICS":
   print("You can choose Mechanical Engineering.")
elif fav1 == "MATHS" and fav2 == "CIRCUITS":
   print("You can choose Mechatronics Engineering.")
elif fav1 == "STATISTICS" and fav2 == "PROGRAMMING":
   print("You can choose AI&DS Engineering.")
elif fav1 == "STATISTICS" and fav2 == "AI":
   print("You can choose AI&ML Engineering.")
elif fav1 == "MATHS" and fav2 == "AI":
   print("You can choose RO&AI Engineering.")
else:
   print("Sorry, no suggestions available for this combination.")
