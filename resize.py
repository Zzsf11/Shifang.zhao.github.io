from PIL import Image
import sys
import os

def resize_image_by_ratio(input_path, output_path, ratio):
    """
    按比例缩放图片
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        ratio: 缩放比例 (例如: 0.5表示缩小一半, 2.0表示放大一倍)
    """
    try:
        # 打开图片
        with Image.open(input_path) as img:
            # 计算新尺寸
            original_width, original_height = img.size
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)
            
            # resize图片
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            # 保存图片
            resized_img.save(output_path)
            print(f"图片已按比例 {ratio} 缩放为 {new_width}x{new_height} 并保存到: {output_path}")
    except Exception as e:
        print(f"处理图片时出错: {e}")

def resize_image_to_size(input_path, output_path, width, height):
    """
    将图片缩放到指定大小
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        width: 目标宽度
        height: 目标高度
    """
    try:
        # 打开图片
        with Image.open(input_path) as img:
            original_width, original_height = img.size
            
            # resize到指定大小
            resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
            # 保存图片
            resized_img.save(output_path)
            print(f"图片已从 {original_width}x{original_height} 缩放为 {width}x{height} 并保存到: {output_path}")
    except Exception as e:
        print(f"处理图片时出错: {e}")

def main():
    if len(sys.argv) < 4:
        print("用法:")
        print("  按比例缩放: python resize.py ratio <输入图片路径> <输出图片路径> <缩放比例>")
        print("  指定大小: python resize.py size <输入图片路径> <输出图片路径> <宽度> <高度>")
        print("示例:")
        print("  python resize.py ratio input.jpg output.jpg 0.5  # 缩小一半")
        print("  python resize.py size input.jpg output.jpg 800 600  # 缩放到800x600")
        return
    
    mode = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    
    if not os.path.exists(input_path):
        print(f"输入文件不存在: {input_path}")
        return
    
    if mode == "ratio":
        if len(sys.argv) != 5:
            print("按比例缩放需要4个参数")
            return
        ratio = float(sys.argv[4])
        if ratio <= 0:
            print("缩放比例必须大于0")
            return
        resize_image_by_ratio(input_path, output_path, ratio)
    
    elif mode == "size":
        if len(sys.argv) != 6:
            print("指定大小缩放需要5个参数")
            return
        width = int(sys.argv[4])
        height = int(sys.argv[5])
        if width <= 0 or height <= 0:
            print("宽度和高度必须大于0")
            return
        resize_image_to_size(input_path, output_path, width, height)
    
    else:
        print("模式必须是 'ratio' 或 'size'")
        return
    
    print("处理完成！")

if __name__ == "__main__":
    main()