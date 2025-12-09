# Egypt History Mini Exam
# Answers are included in comments next to each question

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print("Welcome To Egypt History Mini Exam")
score = 0
print("===================================")

# Question 1
print("1. Which king is traditionally credited with the unification of Upper and Lower Egypt?")
print("A. Khufu  B. Akhenaten")
print("C. Narmer(Menes)  D. Ramses II")
Answer = input("Enter Your answer: ")

if Answer.lower() in ("c","C. Narmer(Menes)","Narmer(Menes)"):
    print(GREEN + "Correct Answer!" + RESET)
    score += 1
else:
    print(RED + "Wrong Answer!" + RESET)
# Answer: C. Narmer(Menes)

print("===================================")

# Question 2
print("2. The main purpose of building pyramids during the Old Kingdom was to:")
print("A. Store grain  B. House markets")
print("C. Serve as tombs for pharaohs  D. Protect cities from invaders")
Answer = input("Enter Your answer: ")

if Answer.lower() in ("c","C. Serve as tombs for pharaohs","Serve as tombs for pharaohs"):
    print(GREEN + "Correct Answer!" + RESET)
    score += 1
else:
    print(RED + "Wrong Answer!" + RESET)
# Answer: C. Serve as tombs for pharaohs

print("===================================")

# Question 3
print("3. The ancient Egyptian writing system is known as:")
print("A. Cuneiform  B. Hieroglyphics")
print("C. Sanskrit  D. Phoenician Script")
Answer = input("Enter Your answer: ")

if Answer.lower() in ("b","B. Hieroglyphics","Hieroglyphics"):
    print(GREEN + "Correct Answer!" + RESET)
    score += 1
else:
    print(RED + "Wrong Answer!" + RESET)
# Answer: B. Hieroglyphics

print("===================================")

# Question 4
print("4. Which river was central to ancient Egyptian civilization?")
print("A. Nile  B. Amazon")
print("C. Tigris  D. Euphrates")
Answer = input("Enter Your answer: ")

if Answer.lower() in ("a","A. Nile","Nile"):
    print(GREEN + "Correct Answer!" + RESET)
    score += 1
else:
    print(RED + "Wrong Answer!" + RESET)
# Answer: A. Nile

print("===================================")

# Question 5
print("5. Who was the famous female pharaoh known for expanding trade and building projects?")
print("A. Cleopatra  B. Nefertiti")
print("C. Hatshepsut  D. Sobekneferu")
Answer = input("Enter Your answer: ")

if Answer.lower() in ("c","C. Hatshepsut","Hatshepsut"):
    print(GREEN + "Correct Answer!" + RESET)
    score += 1
else:
    print(RED + "Wrong Answer!" + RESET)
# Answer: C. Hatshepsut

print("===================================")
print(GREEN + f"Thank You! You got: {(score/5)*100}%" + RESET)
