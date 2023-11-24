import psutil
import subprocess

def calculate_memory_score(speed, total_gb):
    score = 0

    # 内存速度评分
    if speed > 2133:
        score += 5

    # 内存大小评分
    if total_gb > 8:
        score += 5

    return score

def get_memory_info():
    # 获取内存大小
    total_memory_gb = psutil.virtual_memory().total / (1024 ** 3)  # 转换为GB

    # 获取内存速度
    try:
        result = subprocess.run(['wmic', 'MemoryChip', 'get', 'Speed'], capture_output=True, text=True)
        speeds = result.stdout.strip().split("\n")[1:]
        speeds = [int(speed) for speed in speeds if speed.strip()]
        max_speed = max(speeds) if speeds else 0
    except Exception:
        max_speed = 0

    return max_speed, total_memory_gb