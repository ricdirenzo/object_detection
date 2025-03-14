from constants import NUM, TRAINING_DIR, RESULTS_DIR
from preprocessing.preprocessor import get_image_urls, save_data
from detecting.predictor_detector import object_detecting

image_urls = get_image_urls(num=NUM)
save_data(image_urls=image_urls)

object_detecting(source_path=TRAINING_DIR, dest_path=RESULTS_DIR)