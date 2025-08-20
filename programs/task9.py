

info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}
for key,value in info.items():
    if isinstance(value,str):
        print(key.ljust(16),":",value)
    elif isinstance(value,dict):
        for skey,svalue in value.items():
            fkey = key + " " + skey
            print(fkey.ljust(16),":",svalue)
