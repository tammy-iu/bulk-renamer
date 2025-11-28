import os
import json

def load_config():
    """读取配置文件"""
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def rename_files(config):
    folder = config["folder"]
    prefix = config["prefix"]
    suffix = config["suffix"]
    start_num = config["start_num"]
    extension = config["extension"]

    if not os.path.exists(folder):
        print(f"❌ 文件夹不存在：{folder}")
        return

    files = sorted([f for f in os.listdir(folder) if f.endswith(extension)])

    if not files:
        print("⚠️ 未找到任何匹配的文件。")
        return

    print(f"找到 {len(files)} 个文件，开始重命名...\n")

    num = start_num
    for old_name in files:
        old_path = os.path.join(folder, old_name)
        new_name = f"{prefix}{num}{suffix}{extension}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print(f"{old_name}  →  {new_name}")

        num += 1

    print("\n🎉 重命名完成！")

if __name__ == "__main__":
    config = load_config()
    rename_files(config)
