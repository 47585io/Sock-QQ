from PIL import Image
furry = Image.open(
    "/home/tom/vscode/idea/Sock-QQ/thedark.jpg", "r")
furry.convert("RGBA")
furry.save("./thedark.png")

#30,20
#150x450