import io

data = io.StringIO('asdfa in memory')
print(data.getvalue())
print(data.tell())
print(len(data.getvalue()))
data.read()
print(data.tell())
