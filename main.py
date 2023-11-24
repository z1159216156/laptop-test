from cpu_performance import get_cpu_info, calculate_cpu_score
from memory_performance import get_memory_info, calculate_memory_score

def main():
    generation, cores, threads = get_cpu_info()
    if generation is not None:
        cpu_score = calculate_cpu_score(generation, cores, threads)
        print(f"您的CPU得分为：{cpu_score} 分，满分20分")
    else:
        print("无法确定处理器代数。")

    memory_speed, total_memory_gb = get_memory_info()
    memory_score = calculate_memory_score(memory_speed, total_memory_gb)
    print(f"您的内存得分为：{memory_score} 分，满分10分")

    total_score = cpu_score + memory_score
    print(f"您的总得分为：{total_score} 分，满分80分")

if __name__ == "__main__":
    main()
