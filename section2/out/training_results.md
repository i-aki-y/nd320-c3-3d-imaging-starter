## Taining and validation Loss

![Loss](./tensorboard_screenshots/tensorboard_loss.jpg)
Time evolution of train and validation loss.
The training epoch is 5. final mean dice score is 0.895.

## Images during training
In the following, original images ("Image data"), ground truth segmentation images ("Mask") and predicted segmentation images ("Predict") for each training step is shown.
Note, every images are results of validation dataset.

The result of "After 100 step" already shows a good correspondence with the ground truth while some small area fail to detect (see right upper image).
This is consistent with the validation loss where the validation loss is depict small value (between 0.015 - 0.02) at the first epoch.

### After 100 step
![Val](./tensorboard_screenshots/image_val_100.jpg)
![Val](./tensorboard_screenshots/mask_val_100.jpg)
![Val](./tensorboard_screenshots/pred_val_100.jpg)

### After 300 step
![Val](./tensorboard_screenshots/image_val_300.jpg)
![Val](./tensorboard_screenshots/mask_val_300.jpg)
![Val](./tensorboard_screenshots/pred_val_300.jpg)

### After 500 step
![Val](./tensorboard_screenshots/image_val_500.jpg)
![Val](./tensorboard_screenshots/mask_val_500.jpg)
![Val](./tensorboard_screenshots/pred_val_500.jpg)

