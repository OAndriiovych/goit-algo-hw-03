import os
import shutil
import argparse


def copy_and_sort(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                copy_to_destination(os.path.join(root, file), os.path.join(dest_dir, file))
            for dir in dirs:
                sub_src_dir = src_dir + '/' + dir
                sub_dest_dir = dest_dir + '/' + dir
                copy_and_sort(sub_src_dir, sub_dest_dir)
    except Exception as e:
        print(f"Помилка: {e}")


def copy_to_destination(file_path, new_path):
    try:
        shutil.copy2(file_path, new_path)
        print(f"Скопійовано: {file_path} -> {new_path}")
    except Exception as e:
        print(f"Помилка при копіюванні: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_dir', help='Шлях до вихідної директорії')
    parser.add_argument('-d', '--destination', default='dist', help='Шлях до директорії призначення')
    args = parser.parse_args()

    # Виклик функції копіювання та сортування
    copy_and_sort(args.source_dir, args.destination)


if __name__ == "__main__":
    main()
