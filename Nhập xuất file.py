import json
FILE_NAME = 'data.txt'

# Hàm hỗ trợ ghi nội dung vào file
def save_data_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False)


# Hàm hỗ trợ đọc nội dung từ file:
def read_data_from_file(file_name):
    with open (file_name, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


content = [['data', 'data', 'data'], ['data', 'data', 'data'], ['data', 'data', 'data']]

save_data_to_file(FILE_NAME, content)
print(read_data_from_file(FILE_NAME))