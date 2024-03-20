# Chapter 3

> It makes all the difference whether one sees darkness through the light or brightness through the shadows.
> \- David Lindsay

## 3.1

- Spatial domain processing is based on the expression g(x, y) = T[f(x,y)], where f(x,y) is the input image, g(x,y) is the output image, and T is the operator defined on a neighborhood of the point (x,y).
- If the size of the smallest neighborhood is 1x1, then T is called the gray transform function: s = T(r).

## 3.2

- Invert the gray level of the image: s= L - 1 - r
- Logarithm transformation: s = c * log( 1 + r )
- Gamma transformation: s = c * r<sup>ˠ</sup>
- Piecewise linear contrast stretching
- Grayscale layering
- Bit plane layering

## 3.3

- PDF: probability density function
- Histogram equalization is an effective method to enhance saturation.
- Histogram matching can reduce noise in some problems.
- Local histogram equalization: define a square or rectangular neighborhood of each pixel
- Use of Histogram Statistics for Image Enhancement: The means and variance for enhancement purposes. The local mean and variance are used as the basis for making changes that depend on image characteristics in a predefined.

## 3.4

- Generally, linear filtering of an image f of size M\*N a filter mask of size m\*n: g(x,y) = ∑∑w(s,t)f(x+s,y+t) {s:from -a to a, t:from -b to b}
- The basic principle of correlation and convolution are the same.
- Correlation satisfies the law of distribute.
- Convolution satisfies the law of commutation, the law of associative and the law of distribute.

## 3.5

- Smooth spatial filters are used to reduce sharp transitions of gray. Since random noise usually consists of sharp transitions of grayscale, one obvious application of smoothing is noise reduction.
- The simplest separable low-pass filter kernel is the box kernel, which has the same value of coefficient. A box filter of size m \* n is an m \* n array with element value 1, and has a normalized constant in front of it, whose value is 1 divided by the sum of the coefficients.
- Gaussian kernel is the only separable circular-symmetric kernel. If the Gaussian kernel size is chosen to be ⎡6a⎤ \* ⎡6a⎤, then the results obtained are the same as those obtained using arbitrarily large Gaussian kernels.
- Two other fundamental properties of Gaussians are that the product and convolution of two Gaussians are also Gaussians.

## 3.6

- The sharpening effect highlights the transitions in grayscale. The response strength of the derivative operator is proportional to the magnitude of the gray discontinuity at the point where the operator is applied. As a result, image differentiation will enhance edges and other discontinuities, such as noise, and will not emphasize areas where the gray scale changes slowly.
- The first derivative of the constant gray region must be zero. The first derivative at the beginning of a grayscale step or ramp must be non-zero. The first derivative on a grayscale ramp must be non-zero.
- The simplest isotropic derivative operator is Laplace. For f(x,y), Laplacian is defined as: 𝛻<sup>2</sup>𝑓 = 𝑓(x+1,y) + 𝑓(x-1,y) + 𝑓(x,y+1) + 𝑓(x,y-1).
- Basic method of using Laplacian operator to sharpen: 𝑔(𝑥,𝑦) = 𝑓(𝑥,𝑦) + 𝑐[𝛻<sup>2</sup>𝑓(𝑥,𝑦)]
- For 𝑔(𝑥,𝑦) = 𝑓(𝑥,𝑦) + 𝑘𝑔<sub>mask</sub>(𝑥,𝑦), if k = 1, we call it unsharp masking. If k > 1, we call it boosting filtering.

## 3.7

- Construct low-pass filters into high-pass filters, band-rejection filters, and band-pass filters:
  - low-pass: 𝑙𝑝(𝑥,𝑦)
  - high-pass: ℎ𝑝(𝑥,𝑦) = 𝛅(𝑥,𝑦) - 𝑙𝑝(𝑥,𝑦)
  - band-rejection: 𝑏𝑟(𝑥,𝑦) = 𝑙𝑝<sub>1</sub>(𝑥,𝑦) + ℎ𝑝<sub>2</sub>(𝑥,𝑦) = 𝑙𝑝<sub>1</sub>(𝑥,𝑦) + [𝛅(𝑥,𝑦) - 𝑙𝑝<sub>2</sub>(𝑥,𝑦)]
  - band-pass: 𝑏𝑝(𝑥,𝑦) = 𝛅(𝑥,𝑦) - 𝑏𝑟(𝑥,𝑦) = 𝛅(𝑥,𝑦) - [𝑙𝑝<sub>1</sub>(𝑥,𝑦) + [𝛅(𝑥,𝑦) - 𝑙𝑝<sub>2</sub>(𝑥,𝑦)]]