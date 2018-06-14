Python在科学计算领域有三个非常受欢迎库，numpy、SciPy、matplotlib。numpy是一个高性能的多维数组的计算库，SciPy是构建在numpy的基础之上的，它提供了许多的操作numpy的数组的函数。SciPy是一款方便、易于使用、专为科学和工程设计的python工具包，它包括了统计、优化、整合以及线性代数模块、傅里叶变换、信号和图像图例，常微分方差的求解等，[SciPy完整的教程](https://docs.scipy.org/doc/scipy/reference/index.html)。下面就简单的介绍一下SciPy在图像处理方面的应用，如果专业做图像处理当然还是建议使用opencv。本系列教程参考http://cs231n.github.io/python-numpy-tutorial/#scipy

## 一、读取图像获取图像的基本信息

![](https://img-blog.csdn.net/20171126124024872?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMjk5NTc0NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  


```python

from scipy.misc import imread,imsave,imresize  
  
if __name__ == "__main__":  
    #读取图片  
    img = imread("timg.jpg")  
    #获取图片的数据类型  
    img_type = img.dtype  
    print(img_type) #uint8  
    #获取图片的大小  
    img_shape = img.shape  
    print(img_shape) #(310, 493, 3)  
    #获取图片的高  
    img_height = img_shape[0]  
    print(img_height) #310  
    #获取图片的宽  
    img_width = img_shape[1]  
    print(img_width)  #493  
    #获取图片的通道数  
    img_channel = img_shape[2]  
    #通道数为1表示黑白图片，通道数为3表示彩色图片  
    print(img_channel)  #3  
```


## 二、修改图片色彩、裁剪、改变大小


```python
 from scipy.misc import imread,imsave,imresize  
   
 if __name__ == "__main__":  
     #读取图片  
     img = imread("timg.jpg")  
     #通过改变图片每一个通道的比例来改变图片的色彩  
     #将图片R:G:B的比例设置为1:0.9:0.9  
     img_tint = img * [1,0.9,0.9]  
     #保存图片,观察图片可以发现保存后的图片会有点偏红  
     imsave("timg_color.jpg",img_tint)  
     #改变图片的大小，将图片的大小设置为500*500  
     img_resize = imresize(img,(500,500))  
     #保存图片，因为这不是等比例的缩放，可以观察保存的图片会有点变形  
     imsave("timg_resize.jpg",img_resize)  
     #裁剪图片  
     img_incision = img[50:200,100:400]  
     imsave("timg_incision.jpg",img_incision)  
     #scipy中还提供了scipy.io.loadmat和scipy.io.savemat来读写MATLAB的文件  
```


![](https://img-blog.csdn.net/20171126124306016?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMjk5NTc0NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  

![](https://img-blog.csdn.net/20171126124311815?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMjk5NTc0NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  

![](https://img-blog.csdn.net/20171126124318604?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMjk5NTc0NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  

## 三、计算两点之间的欧式距离


```python
 import numpy as np  
 from scipy.spatial.distance import pdist,squareform,cdist  
   
 if __name__=="__main__":  
     x1 = np.array([[1,1]])  
     x2 = np.array([[4,5]])  
     #通过cdist函数，计算两个点之间的距离  
     distance = cdist(x1,x2,"euclidean")  
     print(distance)#[[ 5.]]  
      #创建一个数组，数组的每一行都是一个2维的数组，相当于三个点  
      x = np.array([[1,1],[4,5],[7,9]])  
      #计算每个行的一个点与本身以及另外两个点的欧式距离  
      x_d = squareform(pdist(x,"euclidean"))  
      #欧式距离计算公式：sqrt((x1-x2)^2+(y1-y2)^2)  
      print(x_d)  
      ''''' 
      [[  0.   5.  10.] 
       [  5.   0.   5.] 
       [ 10.   5.   0.]] 
      '''
```