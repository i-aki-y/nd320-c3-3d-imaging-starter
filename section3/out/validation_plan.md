## **Intended Use Statement:** 

This device is intended to assist the diagnosis of radiologists or clinicians responsible for the MRI scan image diagnosis.

## **Device description**

This device estimate patient's single hippocampus volume from the MR 3D image.
This software receives cropped 3D images of the patient's brain MRI scan data as an input and predicts the area of the hippocampus by applying the segmentation algorithm for each 2D slices.
After the calculation, the result is output as a DICOM format report.
The software can be integrated into a medical network system by using a DICOM protocol.
As the segmentation algorithm, the neural network (UNet) trained by the "Hippocampus" dataset published in http://medicaldecathlon.com.
The input images should be cropped into less than 64x64 images, including a whole single hippocampus image.
The resulting report shows hippocampus volume and sampled segmentation images that are used for volume calculation.

## **Indications for use**

This device indicated to use for the estimation of Alzheimer's Progression.
The hippocampus volume is an important factor in measuring Alzheimer's disease progression.
Measuring patients hippocampus volume over a certain period and examining how the volume reduces is an efficient way to diagnose Alzheimer's progression.
However, measuring hippocampus volume is a labor-intensive procedure in which radiologists have to annotate every slice of MR scan images.
This device automatically makes segmentation of the hippocampus and save radiologists labor tasks.

## **Limitation**

This algorithm is trained by using the dataset published in http://medicaldecathlon.com.
In the paper (https://arxiv.org/abs/1902.09063), there is the following description.
"All subjects were free from significant medical or neurological illness, head injury, and active substance use or dependence."
Therefore this algorithm can not apply to the people who have significant medical or neurological illness, head injury, and active substance use or dependence.

## **Validation plan**

We need to collect MR 3D scan images from real-world medical scan data.
The patient list includes healthy people who had no disease and also people who had Alzheimer's disease.
The patients equally distribute over the age group in the range of 30s - 80s. In each age group, the ratio of sex should be equal.
The images should include the whole hippocampus and both the right and left hippocampus.

In this algorithm, the volume calculation is based on the segmentation result of 2D images.
Therefore, in this validation plan, the 2D image segmentation made by radiologists is used as the ground truth.

The collected scan images are annotated by radiologists, where the radiologists make segmentation for each slice of scan images.
To evaluate the device performance, the same images are evaluated by this device. And the Dice scores are calculated.

The annotation results are expected to have large variations depending on the radiologists.
To reduce such a variation, more than three radiologists perform segmentation of the same image, and the averaged dice score is used for the performance evaluation.
For example, the Dice score of an image X is calculated in the following way.

  score_X_A = 'Dice score of image X between radiologist A result and this device result'
  score_X_B = 'Dice score of image X between radiologist B result and this device result'
  score_X_C = 'Dice score of image X between radiologist C result and this device result'

The averaged Dice score of the image 'X' is (score_X_A + score_X_B + score_X_C) / 3.