from PIL import Image
furry=Image.open("./thedrak.png")
furry.thumbnail((500,490))
furry.save("./thedark.png")