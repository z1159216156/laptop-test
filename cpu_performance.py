import psutil
import re
import subprocess

def calculate_cpu_score(generation, cores, threads):
    score = 0

    # 处理器代数评分
    if generation > 7:
        score += 10

    # 核心数评分
    if cores > 2:
        score += 8

    # 线程数评分
    if threads > 4:
        score += 2
    

    return score

def get_processor_generation():
    try:
        result = subprocess.run(['wmic', 'cpu', 'get', 'name'], capture_output=True, text=True)
        processor_name = result.stdout.strip()
        match = re.search(r"i[3579]-(\d+)", processor_name)
        if match:
            model_number = match.group(1)
            if len(model_number) == 5:  # 如果是五位数，取前两位
                return int(model_number[:2])
            else:
                return int(model_number[0])  # 否则，取第一位
        else:
            return None
    except Exception as e:
        return None

def get_cpu_info():
    # 获取处理器代数
    generation = get_processor_generation()

    # 获取CPU核心数
    cores = psutil.cpu_count(logical=False)

    # 获取CPU线程数
    threads = psutil.cpu_count(logical=True)

    return generation, cores, threads

