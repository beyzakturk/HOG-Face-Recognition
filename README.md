# A Take on H.O.G Feature Descriptor
### An explanation on the Histogram of Oriented Gradients Feature Descriptor

Face recognition is one of the most sought-after technologies in the field of machine learning. There are two phases in such a system: Face Detection followed by Face Recognition.

Initially, the faces are detected using a Haar Cascade Classifier on an image in conjunction with the cropping of the cardinal section of the face. A geometric face model is formed with the detection of eyes performed using the Haar Cascade Classifier, while nose detection has been used as a reaffirmation mechanism along with the eyes.

Later, HOG features are extracted from large numbers of facial images to be used as part of the recognition mechanism. These HOG features are then labeled together for a face/user and a Support Vector Machine(SVM) model is trained to predict faces that are fed into the system.
The H.O.G(Histogram of Oriented Gradients) is a feature descriptor used in computer vision for image processing for the purpose of object detection. This got traction after Navneet Dalal and Bill Triggs published a paper called [Histograms of Oriented Gradients for Human Detection](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf) in 2005. This was powerful and state of the art way of doing object detection before the deep learning era. HOGs are widely known for their use in pedestrian detection.

## Intuition

Before knowing how H.O.G works let us know what are gradients in this context. Take the following image for example:

![Image](https://miro.medium.com/max/1400/1*EF-lhrdIWBDGAF0EtnCoVQ.png)

When you step from left to right pixel by pixel, you will find that after some steps, there is a sudden change in the pixel value i.e, from a black lower pixel number to a white higher pixel number. This sudden change in the color is called a gradient and going from a darker tone to a lighter tone is called a positive gradient and vice versa. Going from left to right gives us the horizontal gradient and as expected going from top to down gives a vertical gradient.

## How the H.O.G works

HOG works with something called a block which is similar to a sliding window. A block is considered as a pixel grid in which gradients are constituted from the magnitude and direction of change in the intensities of the pixel within the block.

![Image](https://miro.medium.com/max/512/0*HpySen1_BkMRkNOj.gif)

1. So the first step would be to convert an RGB image to grayscale.
2. To get a closer look, let's focus on one such grid of size 8*8. Look at the following picture.

In the block of 64 pixels, for each pixel, horizontal and vertical gradients are calculated. Like in the above picture, horizontal and vertical gradients are calculated as :
Horizontal Gradient: 120 –70 = 50
Vertical Gradient : 100 –50 = 50
3. Once we get the gradients we try to calculate something called gradient magnitude and gradient angle for each of 64 pixels.

Now with those 64 gradient vectors, we try to compress them to 9 vectors, trying to retain the maximum structure. To do this we try to plot a histogram of magnitudes and angles. Here x-axis is angles and they are binned into 9 bins each with a size of 20 degrees.
> **Note: Creating 9 bins is decided by the authors of the HOG paper. So it's pretty much constant everywhere.**

![Image](https://miro.medium.com/max/1400/0*hU5iB_mQN5G0AQCP.jpg)

The above results are for one 8*8 grid and we compressed the representation to 9 vectors.

4. When we slide that 8*8 grid along the whole image and try to interpret the histogram results we get something like below.
5. And by plotting the HOG features we will find that the structure of the object or face is well maintained, losing all the insignificant features.

![Image](https://miro.medium.com/max/1400/1*gWeh90aKfv7A-bpc0vC0oQ.png)

And such input can be leveraged by any Machine Learning algorithm to do the classification or regression.
It’s a very powerful technique being used still today and object detection can be achieved without the use of heavy architectures from DL.
The best place to get HOG detection functionality is from the library [Dlib](http://dlib.net/).

Now that you know an old handy tool to represent an image in a compressed format and still maintains the structure of it, you can incorporate this in many computer vision use cases.
