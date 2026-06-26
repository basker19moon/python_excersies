import pyfiglet
import random
def generate__fathers_day_wish():
    message = "Happy father's Day!"
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = random.choice(fonts)
    ascii_art = pyfiglet.figlet_format(message, font=selected_font)
    return ascii_art

#calling the function to generate the wish
father_day_wish = generate__fathers_day_wish()

# printing the wish
print(father_day_wish)
