from aip import AipImageClassify

APP_ID = 11160858
API_KEY = "yk3QgeOs6o7F2lstKw8mKa0u"
SECRET_KEY = "4X6GFZXYmn00FOfCLIw6aoOdvFtPrXQs"
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

'''图片读取'''
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
image = get_file_content('benchi.jpg')

''' 调用车辆识别 '''
print(client.animalDetect(image,options={"top_num":1})["result"][0]['name'])