import os
import logging
from datetime import datetime

def get_project_root() -> str:
    """Returns project root directory"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def setup_logging(log_level: str = 'INFO') -> logging.Logger:
    logger = logging.getLogger('devops-scripts')
    logger.setLevel(getattr(logging, log_level.upper()))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

def get_current_timestamp() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File {file_path} not found')

def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w') as file:
        file.write(content)