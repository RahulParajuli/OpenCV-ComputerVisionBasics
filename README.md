# ComputerVisionExercise

In this repository I will be contributing all the necessary tools in OpenCV and its application with better code explanation. Every operations are explain well below with their examples.

## Bitwise operation
Bitwise operation is similar to logic gate we have studied during our high school. This operation contains AND, OR, NOT, XOR operators that deals with same mathematical solution for images.

<b>1. bitwiseAND</b> <br>
Bitwise AND maps the common pixels present in overlapping images. <br>
<img height=250px width=600px src = "resources/results/bitwizeAND.png"> 

<b>2. bitwiseOR </b> <br>
Bitwise OR maps all images overlapping and non overlapping conditions.<br>
<img height=250px width=600px src = "resources/results/bitwiseOR.png">

<b>3. bitwiseNOT</b> <br>
Bitwise NOT maps overlapping condition and inverse it with non overlapping conditions. <br>
<img height=250px width=600px src = "resources/results/bitwiseNOT.png">

<b>4. bitwiseXOR</b> <br>
Bitwise XOR maps exclusive overlapping conditions. <br>
<img height=250px width=600px src = "resources/results/bitwiseXOR.png">


## Blurring Techniques
<b>1. averageBlur</b> <br>
The image is convolved with a box filter (normalized). In this process, the central element of the image is replaced by the average of all the pixels in the kernel area. <br>
<img height=350px width=600px src = "resources/results/averageBlurring.png">

<b>2. bilateralBlur</b> <br>
Bilaretal bluring is also known as image smoothing, image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content (eg: noise, edges) from the image. <br>
<img height=350px width=600px src = "resources/results/bilateralblurring.png">

<b>3. gaussianBlur</b> <br>
In Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced. <br>
<img height=350px width=600px src = "resources/results/gaussianblur.png">

<b>4. medianBlur</b> <br>
Here, the central element of the image is replaced by the median of all the pixels in the kernel area. This operation processes the edges while removing the noise. <br>
<img height=350px width=600px src = "resources/results/medianblur.png">

## Color Channels
This folder contains channeling of the images that combines all the basic colors that is red blue and green.
<b>1. splitting and merging colors</b> <br>
Since images in OpenCV are internally represented as NumPy arrays, accessing each channel can be accomplished in multiple ways, implying multiple ways to skin this images. <br>
a. Splitting red color <br>
<img height=350px width=600px src = "resources/results/splittingred.png"> <br>
b. Splitting blue color <br>
<img height=350px width=600px src = "resources/results/splittingblue.png"> <br>
c. Splitting green color <br>
<img height=350px width=600px src = "resources/results/splittinggreen.png"><br>


## Color Spaces
This folder contains most used image color spaces such as hue, gray, labs and blur.

<b>1. LAB</b><br>
It expresses color as three values: L* for perceptual lightness, and a* and b* for the four unique colors of human vision: red, green, blue, and yellow. CIELAB was intended as a perceptually uniform space, where a given numerical change corresponds to a similar perceived change in color. <br>
<img height= 150px, width = 450px, src = "https://static.packt-cdn.com/products/9781789537147/graphics/assets/3a0096f4-9c14-46d0-9072-d67580776f3f.png">

<b>2. Grayscale</b><br>
The grayscale image of the same size as a color image, made of just one of these primary colors. For instance, an image from a standard digital camera will have a red, green and blue channel. A grayscale image has just one channel. <br>
<img height=250px width=600px src = "resources/results/gray.png"> 
<img height=250px width=600px src = "https://static.packt-cdn.com/products/9781789537147/graphics/assets/51b0d759-4ef7-47f8-9878-e5cd4468fcec.png">

<b>3. Hues</b> <br>
Hue refers to the dominant color family. Hue refers to the origin of the colors we can see. Primary and Secondary colors (Yellow, Orange, Red, Violet, Blue, and Green) are considered hues.<br>
<img height=250px width=600px src = "resources/results/hues.png">

<b>4. LABtoBGR</b><br>
Conversion of image with channel LAB to BGR. <br>
<img height=250px width=600px src = "resources/results/LABtobgr.png">

<b>5. bgrtorgb</b> <br>
Conversion of image with channel BGR to RGB. <br>
<img height=250px width=600px src = "resources/results/bgrtorgb.png">

<b>6. hsvtobgr</b> <br>
Conversion of images with channel HSV to BGR.<br>
<img height=250px width=600px src = "resources/results/hsvtoBGR.png">

## Computing Histogram
Histogram from matplotlib can clearly classify which color channel the image adapt. This program creates a frequency of all the color channel used in the image.

<b>1. Colorhistogram</b> <br>
Frequency of all the color present in the colored images. <br>
<img height=350px width=600px src = "resources/results/BGRhistogram.png">

<b>2. Grayhistogram</b> <br>
Frequency of the channel grayscale images.<br>
<img height=350px width=600px src = "resources/results/histogramgray.png">

<b>3. Histogram masking</b><br>
This checks colors frequency of masked area.<br>
<img height=350px width=600px src = "resources/results/maskingregionhist.png">

## Gradients and edges
Every pixel inside the Gradient image represents the contrast intensity in the neighborhood of a pixel. It is used for image segmentation and edge detection.<br>
Edge detection is an image-processing technique, which is used to identify the boundaries (edges) of objects, or regions within an image. Edges are among the most important features associated with images. <br>

<b>1. AbsoluteLaplation</b> <br>
<img height=350px width=600px src = "resources/results/absoluteLaplacian.png">

<b>2. Laplacian</b> <br>
<img height=350px width=600px src = "resources/results/simplelaplacian.png">

<b>3. Sobel </b> <br>
<img height=350px width=600px src = "resources/results/sobel.png">

## Image Transformations
This folder contains all the image transformations related functions and libraries in OpenCV.

<b>1. Image Flipping. </b> <br>
<img height=350px width=600px src = "resources/results/imageflipping.png"><br>
<b>2. Image Rotation.</b> <br>
<img height=350px width=600px src = "resources/results/imagerotation.png"><br>
<b>3. Shifting Images.</b> <br>
<img height=350px width=600px src = "resources/results/imageshifting.png"><br>

## Important color scaling
It contains all the scaling features of openCV.

<b>1. Canny. </b><br>
<img height=350px width=600px src = "resources/results/canny.png"><br>
<b>2. Gaussian Blur.</b> <br>
<img height=350px width=600px src = "resources/results/gaussianblur.png"><br>
<b>3. GrayScale.</b><br>
<img height=350px width=600px src = "resources/results/gray.png"><br>


## Masking
Masking is something we consider as focusing in some areas of image. Lets have a look into some of the methods that are carried out for masking. <br>
<b> circleMasking </b><br>
<img height=350px width=600px src = "resources/results/circlemask.png"><br>

<b>2. rectangleMasking</b><br>
<img height=350px width=600px src = "resources/results/rectanglemasking.png"><br>

<b>3. weirdshapes</b> <br>
<img height=350px width=600px src = "resources/results/weirdshapemasking.png"><br>


## Some reallife implementations
This folder contains all the real life implementation that I have done using OpenCV.

1. motion detection.

## Basic reading and rescaling
This folder contains all the basic reading and rescaling technique in OpenCV.

1. cv2 reading image.
2. cv2 reading videos.
3. cv2 resize and rescale.
4. cv2 resizing.
5. cv2 webcam.

## Draw and write on images.
This folder contains drawing in a blank canvas or creating a bounding box in the detected place.

1. Draw.

## Resources
This folder contains images and video used for all the programs.

1. Images.
2. Videos.

These are some of the fundamentals of this repository.
Hope it helps somebody who is exploring OpenCV and ended up here.

## Thresholding
<b>1. AdaptiveThresholding </b> <br>
Adaptive thresholding is the method where the threshold value is calculated for smaller regions and therefore, there will be different threshold values for different regions. <br>
<img height=350px width=600px src = "resources/results/adaptivethresh.png"><br>

<b>2. InverseThresholding</b> <br>
Inverse-Binary Thresholding is just the opposite of Binary Thresholding. The destination pixel is set to: zero, if the corresponding source pixel is greater than the threshold. <br>
<img height=350px width=600px src = "resources/results/inversethresh.png"><br>

<b>3. SimpleThresholding </b> <br>
Simple thresholding where we manually supply parameters to segment the image — this works extremely well in controlled lighting conditions where we can ensure high contrast between the foreground and background of the image. <br>
<img height=350px width=600px src = "resources/results/simplethresholding.png"><br>


## happy coding.
