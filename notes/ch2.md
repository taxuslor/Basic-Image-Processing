# Chapter 2

> Those who wish to succeed must ask the right preliminary questions.
> \- Aristotle

## 2.1

- Cones (highly sensitive to colors): 6-7 million, in the centre of the retina-fovea, narrow band spectrum, 460 nm (blue), 575 nm (green), 625 nm (yellow), daylight
- Rods (luminance, sensitive, overall view of the object) 75-150 million, on the surface of the Blind spot, broad spectrum, daylight and night
- To focus on distant objects, the controlling muscles cause the lens to be relatively flattened. Similarly, these muscles allow the lens to become thicker in order to focus on objects near the eye.
- Experimental evidence indicates that subjective brightness (intensity as perceived by the human visual system) is a logarithmic function of the light intensity incident on the eye.
- We actually perceive a brightness pattern that is strongly scalloped, especially near the boundaries. These seemingly scalloped bands are called Mach bands after Ernst Mach.

## 2.2

- Three basic quantities to describe a chromatic light source
  - Radiance: total amount of energy that flows from the light source, measured in watts
  - Luminance: the amount of energy an observer perceives from a light source, measured in lumen（lm）
  - Brightness: a subjective descriptor of light perception, impossible to measure
- Red Green Blue (RGB)
- Cyan Magenta Yellow (CMY)
- Hue Saturation Intensity (HSI)

## 2.3

- Single Image Sensor
- Array Sensor
- Line Sensor
- The idea is simple: Incoming energy is transformed into a voltage by the combination of input electrical power and sensor material that is responsive to the particular type of energy being detected.
- The output voltage waveform is the response of the sensor(s), and a digital quantity is obtained from each sensor by digitizing its response.

## 2.4

- Digitizing the coordinate values is called sampling.
- Digitizing the amplitude values is called quantization.
- Sometimes, the range that gray spans is called the dynamic range, and this term is used differently in different contexts. Here, we define the dynamic range of an image system as the ratio of the maximum measurable gray level to the minimum detectable gray level in the system. In general, the upper limit depends on saturation and the lower limit depends on noise, but noise can also appear in brighter shades of gray.
- Dynamic range establishes the lowest and highest gray levels that a system can represent and that an image has. Closely related to this concept is image contrast, which is defined as the gray difference between the highest and lowest gray levels in an image. The contrast ratio is the ratio of these two quantities. When the appreciable number of pixels in an image has a high dynamic range, the image is said to have high contrast.
- When an image has 2^k possible gray levels, we usually call the image a "k-bit image" (for example, a 256-level image is an 8-bit image).
- The isopreference curves show images that are rich in detail may require fewer gray levels.
- Interpolation is the process of using known data to estimate a value for an unknown location.
- nearest neighbor interpolation / bilinear interpolation / bicubic interpolation.

## 2.5

- The image set of adjacent elements of a point p is called the neighborhood of p. If a neighborhood contains P, it is called a closed neighborhood, otherwise it is called an open neighborhood.
- To establish if two pixels are connected, it must be determined if they are neighbors and if their gray levels satisfy a specified criterion of similarity (say, if their gray levels are equal).
- Three types of adjacency:
  - 4-adjacency. Two pixels p and q with values from V are 4-adjacent if q is in the set N4(p).
  - 8-adjacency. Two pixels p and q with values from V are 8-adjacent if q is in the set N8(p).
  - m-adjacency (mixed adjacency). Two pixels p and q with values from V are m-adjacent if
    - (i) q is in N<sub>4</sub>(p), or
    - (ii) q is in N<sub>D</sub>(p) and the set N<sub>4</sub>(p)∩N<sub>4</sub>(q) has no pixels whose values are from V.
- For any pixel p in S, the set of pixels that are connected to it in S is called a connected component of S .If it only has one connected component, then set S is called a connected set.
- We call R a region of the image if R is a connected set.
- The boundary (also called border of contour) of a region R is the set of pixels in the region that have one or more neighbors that are not in R.
- The concept of an edge is found frequently in discussions dealing with regions and boundaries - a local definition based on discontinuities between pixel values. 
- The one exception in which edges and boundaries correspond is in binary images.
- The Euclidean distance between p and q is defined as D<sub>e</sub>(p,q)=[(x-s)2+(y-t)2]<sup>1/2</sup> where p and q are pixels with coordinates (x,y) and (s,t).
- The D<sub>4</sub> distance (also called city-block distance) between p and q is defined as D<sub>4</sub>(p,q)=|x-s|+|y-t|.
- The D<sub>8</sub> distance (also called chessboard distance) between p and q is defined as D<sub>8</sub>(p,q)= max (|x-s|,|y-t|).