
import jieba
text_seg_all=[]
with open("D:\python project me\data\my_seq_attn_diffc/test/test.txt","r",encoding="utf-8") as f1:
    for line in f1.readlines():
        seg = jieba.cut(line)
        text_seg=' '.join(seg)
        text_seg_all.append(text_seg)
with open("D:\python project me\data\my_seq_attn_diffc/test/test_seg.txt","w") as f2:
    for i in text_seg_all:
       f2.write(i)
