def concat_sequence_v1(s1, s2):
    for elem in s1:
        yield elem
    for elem in s2:
        yield elem

def concat_sequence_v2(s1, s2):
    yield from s1
    yield from s2


seq1 = range(10)
seq2 = range(10, 20)
res = concat_sequence_v1(seq1, seq2)

for i in res:
    print(i)
print('='*25)
seq1 = range(10)
seq2 = range(10, 20)
res = concat_sequence_v2(seq1, seq2)

for i in res:
    print(i)