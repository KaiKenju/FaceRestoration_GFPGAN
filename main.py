
import os
import subprocess
import argparse
import time
from tqdm import tqdm  # Thêm thư viện tqdm để tạo thanh tiến trình

# Chức năng phục chế ảnh với mô tả chi tiết từng hoạt động
def restore_image(input_image_paths, output_dir='results', upscale=2, version='1.4'):
    """
    Phục chế ảnh mờ hoặc hư hỏng bằng GFPGAN.
    
    Tham số:
    - input_image_paths: Danh sách đường dẫn đến các ảnh đầu vào.
    - output_dir: Thư mục lưu kết quả đầu ra. Mặc định là 'results'.
    - upscale: Tăng độ phân giải của ảnh (mặc định là 2x).
    - version: Phiên bản của mô hình GFPGAN, mặc định là '1.4'.
    """
    
    # Kiểm tra xem mô hình đã được tải về chưa
    model_path = 'model/GFPGANv1.4.pth'
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Mô hình GFPGAN chưa được tải về: {model_path}")
    
    # Sử dụng tqdm để tạo thanh tiến trình cho từng ảnh trong danh sách
    for idx, input_image_path in enumerate(tqdm(input_image_paths, desc="Đang xử lý ảnh", unit=" ảnh")):
        if not os.path.exists(input_image_path):
            print(f"Ảnh đầu vào không tồn tại: {input_image_path}")
            continue
        
        print(f"\nĐang phục chế ảnh: {input_image_path}")
        print(f"Sử dụng mô hình GFPGAN phiên bản {version}")
        print(f"Tăng độ phân giải lên {upscale}x")
        print(f"Đang trong quá trình xử lý, vui lòng chờ...")
        
        # Bắt đầu đo thời gian
        start_time = time.time()
        
        # Lệnh để chạy quá trình phục chế
        command = [
            'python', 'GFPGAN/inference_gfpgan.py', 
            '-i', input_image_path,  # Đường dẫn đến ảnh đầu vào
            '--version', version,    # Phiên bản của GFPGAN
            '-o', output_dir,        # Thư mục lưu kết quả
            '--upscale', str(upscale),  # Hệ số tăng độ phân giải
            '--bg_upsampler', 'realesrgan'  # Sử dụng Real-ESRGAN để tăng độ phân giải phần nền
        ]
        
        # Thực thi lệnh phục chế
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Kết thúc đo thời gian
        end_time = time.time()
        
        # Tính toán thời gian thực thi
        elapsed_time = end_time - start_time
        
        # Kiểm tra kết quả trả về
        if result.returncode == 0:
            print(f"Phục chế ảnh {input_image_path} thành công! Ảnh được lưu trong thư mục: {output_dir}")
        else:
            print(f"Có lỗi xảy ra trong quá trình phục chế ảnh {input_image_path}:\n{result.stderr.decode('utf-8')}")
        
        # In ra thời gian thực thi cho ảnh hiện tại
        print(f"Thời gian thực thi cho ảnh {input_image_path}: {elapsed_time:.2f} giây")


# Ví dụ sử dụng: Phục chế nhiều ảnh
if __name__ == '__main__':    
    # Sử dụng argparse để nhận đường dẫn ảnh và các tùy chọn từ dòng lệnh
    parser = argparse.ArgumentParser(description='Phục chế ảnh cũ bằng GFPGAN.')
    parser.add_argument('-i', type=str, nargs='+', help='Danh sách đường dẫn đến các ảnh cần phục chế')
    parser.add_argument('--output_dir', type=str, default='results', help='Thư mục lưu kết quả đầu ra')
    parser.add_argument('--upscale', type=int, default=2, help='Hệ số tăng độ phân giải (mặc định là 2x)')
    parser.add_argument('--version', type=str, default='1.4', help='Phiên bản của mô hình GFPGAN (mặc định là 1.4)')
    
    args = parser.parse_args()

    # Gọi hàm phục chế
    try:
        restore_image(args.i, args.output_dir, args.upscale, args.version)
    except Exception as e:
        print(f"Lỗi: {e}")
