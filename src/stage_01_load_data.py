from src.utils.all_utils import read_yaml, create_directory
import argparse
import os
import shutil
import tqdm
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def copy_file(source_downlaod_dir, local_data_dir):
    list_of_files = os.listdir(source_downlaod_dir)
    N = len(list_of_files)
    for file in tqdm(list_of_files, total=N, desc=f'copying file from {source_download_dir} to {local_data_dir}', colour="green"):
        src = os.path.join(source_downlaod_dir, file)
        dest = os.path.join(local_data_dir, file)
        shutil.copy(src, dest)

def get_data(path_of_config):
    config = read_yaml(path_of_config)
    source_download_dirs = config["source_download_dirs"]
    local_data_dirs = config["local_data_dirs"]

    for source_file, local_file in tqdm(zip(source_download_dirs, local_data_dirs), total=2, desc= "list of folders", colour="red"):
        create_directory([local_data_dirs])
        copy_file(source_download_dirs, local_data_dirs)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>> stage one started")
        get_data(config_path=parsed_args.config)
        logging.info("stage one completed! all the data are saved in local >>>>>\n")
    except Exception as e:
        logging.exception(e)
        raise e










