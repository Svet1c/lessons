# task 1

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line.find("-") - 1
        request_type = line.find('"') + 1
        split = line.find("/", request_type)
        requested_resource = line.find('HTTP')
        print(f"{line[:remote_addr], line[request_type: split - 1], line[split: requested_resource - 1]}")