import socket
import pprint


def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    content = ''.join(lines[empty_index+1:])
    return int(status_code), headers, content


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_items = [
    'GET / HTTP/1.1',
    'Host: www.google.com',
    'Connection: keep-alive',
    'Accept: text/html',
]
content = '\n'.join(content_items)
print('---- HTTP MESSAGE ----')
print(content)
print('---- END OF MESSAGE ----')
sock.send(content.encode())
result = sock.recv(10024)
print(result.decode())
print('*'*36)
status_code, headers, content = parse_http_response(result.decode())
print(f'Status code: {status_code}')
print(f'Headers: {headers}')
print(f'Content: {content}')