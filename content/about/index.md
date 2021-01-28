---
title: "About"
date: 2021-01-15
---

## The Background
![Panel](https://raw.githubusercontent.com/ex172000/lab-web/master/docs/panel.png)

An internal combustion engine (ICE) is a heat engine in which the combustion of a fuel occurs with an oxidizer (usually air) in a combustion chamber that is an integral part of the working fluid flow circuit. In an internal combustion engine, the expansion of the high-temperature and high-pressure gases produced by combustion applies direct force to some component of the engine. The force is applied typically to pistons, turbine blades, rotor or a nozzle. This force moves the component over a distance, transforming chemical energy into useful work. This replaced the external combustion engine for applications where weight or size of the engine is important.

In the actual lab, we have conducted the experiment with the following inputs:
- Torque
- Throttle Position

, and Obtained the outputs:
- Air Flow Rate
- Engine Speed
- Fuel Flow Rate

The sample data is like the following:
|Barometric Pressure (mBar)|Inlet Pressure (kPa)|Air Flow Pressure (Pa)|Oil Pressure (Bar)|Fuel Pressure (Bar)|Throttle Position (%)|Torque (Nm)|Engine Speed (rpm)|Fuel Flow Rate (cm^3/min)|Air Temp. (C)|Fuel Temp. (C)|Oil Out Temp. (C)|Exhaust Temp. (C)|Plant In Temp. (C)|Cool In Temp. (C)|Cool Out Temp. (C)|Dyno Out Temp. (C)|Oil In Temp. (C)|Cal Water In Temp. (C)|Cal Water Out Temp. (C)|Cal Exhaust In Temp. (C)|Cal Exhaust Out Temp. (C)|
|--------------------------|--------------------|----------------------|------------------|-------------------|---------------------|-----------|------------------|-------------------------|-------------|--------------|-----------------|-----------------|------------------|-----------------|------------------|------------------|----------------|----------------------|-----------------------|------------------------|-------------------------|
|994.97                    |101.02              |221.71                |4.34              |2.53               |14.42                |24.12      |1237.64           |0.26                     |22.25        |23.11         |40.75            |162.39           |16.94             |44.24            |43.25             |17.37             |42.83           |17.20                 |20.54                  |77.60                   |19.47                    |
|995.07                    |99.04               |276.61                |4.39              |2.48               |14.62                |24.12      |1237.91           |0.26                     |22.18        |23.04         |40.77            |162.48           |16.92             |44.31            |43.31             |17.34             |42.89           |17.23                 |20.55                  |77.81                   |19.51                    |
|994.87                    |101.90              |232.25                |4.39              |2.44               |14.72                |24.30      |1238.12           |0.26                     |22.14        |23.03         |40.86            |162.60           |16.91             |44.45            |43.45             |17.36             |42.97           |17.27                 |20.57                  |78.07                   |19.56                    |
|995.48                    |99.14               |320.80                |4.39              |2.53               |14.77                |24.27      |1239.65           |0.44                     |22.23        |23.12         |41.05            |162.87           |16.97             |44.55            |43.49             |17.30             |43.01           |17.25                 |20.56                  |78.29                   |19.54                    |

## Deep Learning Modeling

With the above data, we will construct the following deep learning model:
- 128-node Dense layer, with ReLu activation
- 256-node Dense layer, with ReLu activation
- 64-node Dense layer, with ReLu activation
- 3-node Dense layer, for converting to the output

The model is trained on Tensorflow(Python) with a Mean Absolute Error loss function and it obtained a Mean Square Error of 7.6440300941467285 after 5000 iterations.

## Learning the Noise

With the above model, we successfully constructed the internal state of the engine, but one of the important item, noise, is missing from it. To construct the noise, we assume it's coming from the input(and also the feedback from the engine itself). We also assume the noise distribution is a Gussian distribution.

With the above two assumptions, we decided to get the noise with K-Means unsupervised learning algorithms. The algorithm can be found here: https://en.wikipedia.org/wiki/K-means_clustering

For us, we got the following data for two different engine types:

**Diesel**

Number of samples: 2034

![Diesel Engine Noise Inertia](https://raw.githubusercontent.com/ex172000/lab-web/master/docs/diesel.png)
- Optimal Number of Classes: 17
- Torque Sigma: 1.2506192871765371
- Position Sigma:  0.8401700850752418

**Petrol**

Number of samples: 1677

![Diesel Engine Noise Inertia](https://raw.githubusercontent.com/ex172000/lab-web/master/docs/petrol.png)

- Optimal Number of Classes: 17
- Torque Sigma: 0.39536827344266434
- Position Sigma: 0.27096564078006163

The optimal number of classes is got with with inertia ploting, and the finding of the "knee". It is learnt with the package of *kneed*

## Serving the Model as a Tool

To serve the model on web, we have leveraged the following services/tools:
- Tensorflow JavaScript(TFJS) convertor
- Hugo static webpage generator
- GitHub Pages

We firstly convert the model with the TFJS convertor
```bash
 tensorflowjs_converter --input_format=keras ./lab.h5 ./petrol
```

This model is then served via an async function in the HTML/JavaScript
```javascript
const model = await tf.loadLayersModel('https://raw.githubusercontent.com/zackzhu123/model.json');
```

Then we use the loaded model inside the Hugo-generated page, which you can find in the **Lab** tab.