from PIL import Image
furry = Image.open(
    "/home/tom/vscode/idea/Sock-QQ/From/Server/one/dog.png", "r")
furry.thumbnail((130,380))
furry.save("./dog.png")

#100x90
#150x450