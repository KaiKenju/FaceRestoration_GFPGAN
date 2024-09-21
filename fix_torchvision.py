import os
import importlib.util

# Tự động tìm kiếm và lấy đường dẫn của module basicsr
module_name = 'basicsr'
spec = importlib.util.find_spec(module_name)

if spec is not None:
    basicsr_path = os.path.dirname(spec.origin)
    
    # Tạo đường dẫn đầy đủ đến file degradations.py
    file_path = os.path.join(basicsr_path, 'data', 'degradations.py')

    # Kiểm tra xem file có tồn tại không
    if os.path.exists(file_path):
        # Định nghĩa dòng import mới cần thay thế
        new_import_statement = "from torchvision.transforms.functional import rgb_to_grayscale\n"

        # Đọc nội dung của file trước khi sửa
        with open(file_path, 'r') as file:
            lines = file.readlines()

        print("Nội dung trước khi sửa:")
        print("".join(lines[:10]))  # In 10 dòng đầu để kiểm tra

        # Sửa đổi dòng thứ 8 (index 7)
        if len(lines) >= 8:
            lines[7] = new_import_statement  # Thay thế dòng 8 bằng lệnh import mới

        # Ghi lại nội dung đã sửa vào file
        with open(file_path, 'w') as file:
            file.writelines(lines)

        print("Sửa đổi thành công!")

        # Đọc lại file để kiểm tra nội dung sau khi sửa
        with open(file_path, 'r') as file:
            updated_lines = file.readlines()

        print("Nội dung sau khi sửa:")
        print("".join(updated_lines[:10]))  # In lại 10 dòng đầu để kiểm tra
    else:
        print(f"Không tìm thấy file tại: {file_path}")
else:
    print(f"Không tìm thấy module {module_name}")

