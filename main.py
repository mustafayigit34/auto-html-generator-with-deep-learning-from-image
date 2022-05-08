import compile_page
from util.file_utils import clear_detect_dir
from util.get_parameters import label_txt_to_list

from yolov5 import detect


def run():
    clear_detect_dir()

    # Detecting classes on uploaded sketch image
    test_image_path = "test-images/test-image-1.jpg"

    detect.run(source=test_image_path, weights="yolov5/last.pt", conf_thres=0.75, save_txt=True, save_conf=True,
               imgsz=(416, 416))  # Detecting classes on uploaded sketch

    # Reading results from label file to label_list
    result_label_path = "yolov5/runs/detect/exp/labels/" + test_image_path.split("/")[1].split(".")[0] + ".txt"

    labels_list = label_txt_to_list(result_label_path)

    compile_page.generate_form(labels_list)


# test
if __name__ == '__main__':
    run()
