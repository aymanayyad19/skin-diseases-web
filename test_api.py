
from inference_sdk import InferenceHTTPClient

def testApi( image_url):
    CLIENT = InferenceHTTPClient(api_url="https://detect.roboflow.com", api_key="kdNkkbxsyXcEBKoX4JYO")

    result = CLIENT.infer(image_url, model_id="yolov8-skin-disease-detection/1")

    return result


if __name__ == "__main__":
    image_url = "https://media.post.rvohealth.io/wp-content/uploads/2022/04/acne-vulgaris-body1.jpg"
    print(f"result = {str(testApi(image_url))}")