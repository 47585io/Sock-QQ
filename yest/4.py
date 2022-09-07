from PIL import Image
one=Image.open("/home/tom/vscode/idea/Sock-QQ/picture/fresh.png","r")
two=Image.open("./fresh.png","r")
new_one=one.resize((40,30))
new_two=two.resize(new_one.size)
new=Image.blend(new_one,new_two,0.1)
new.save("./end.png")