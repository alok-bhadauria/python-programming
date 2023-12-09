print("<== COUNT NO. OF VOWELS AND CONSONANTS IN A STRING ==>")

a = input("Enter your string : ")

vowels = consonants = uppercase = lowercase = 0

v_list=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in a:
    if i in v_list:
        vowels += 1
    if ((i>='a' and i<='z')or(i>='A' and i<='Z'))and(i not in v_list):
        consonants += 1
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase += 1

print("Number of vowels : ", vowels)
print("Number of consonants : ", consonants)
print("Number of uppercase characters : ", uppercase)
print("Number of lowercase characters : ", lowercase)
