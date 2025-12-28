import gradio as gr
import PIL.Image as Image

from ultralytics import YOLO

model = YOLO("best.pt")


def predict_image(img, conf_threshold, iou_threshold):
    """Predicts objects in an image using a YOLO11 model with adjustable confidence and IoU thresholds."""
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=640,
    )

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])

    return im


iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold"),
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="Oral Disease Detecetion - Powered by Ultralytics Gradio",
    description="Upload images for inference to detect caries, gingivitis, ulcers, and benign conditions using a YOLO8 model. Adjust the confidence and IoU thresholds to refine detection results.",
    examples=[
        ["benign.jpg", 0.25, 0.45],
        ["caries.jpg", 0.25, 0.45],
        ["gingivitis.jpg", 0.25, 0.45],
        ["ulcer.webp", 0.25, 0.45],
    ],
)

if __name__ == "__main__":
    iface.launch()