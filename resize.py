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

def main():
    if len(sys.argv) != 4:
        print("用法: python resize.py <输入图片路径> <输出图片路径> <缩放比例>")
        print("示例: python resize.py input.jpg output.jpg 0.5  # 缩小一半")
        print("示例: python resize.py input.jpg output.jpg 2.0  # 放大一倍")
        return
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    ratio = float(sys.argv[3])
    
    if not os.path.exists(input_path):
        print(f"输入文件不存在: {input_path}")
        return
    
    if ratio <= 0:
        print("缩放比例必须大于0")
        return
    
    resize_image_by_ratio(input_path, output_path, ratio)
    print("处理完成！")

if __name__ == "__main__":
    main()