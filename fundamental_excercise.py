def maker(phrase):
    capitalized= phrase.capitalize()
    interrogatives=("who", "why", "how", "what")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


phrase_list=[]
while True: 

    user_input= input("Say something: ")
    if(user_input == "\end"):
        break
    else:
        phrase_list.append(maker(user_input))

print(" ".join(phrase_list))
        
