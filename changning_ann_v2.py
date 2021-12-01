# import os
# import cv2
# from collections import deque
# prev=deque
# txtpath="./data1_ann.txt"
# a = open(txtpath,'r')
# out=open("output_data1.txt",'a')
# cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
# none_img=[]
# for line in a:
#     prev.append(line)
#     if len(prev)>10:
#         prev.popleft()
#     flag=False
#     updated_box=[]
#     imgpath=line.split()[0]
#     updated_box.append(imgpath)
#     img=cv2.imread("./"+imgpath)
#     if img is None:
#         print("cant open image please check")
#         none_img.append(imgpath)
#         continue
#     for bbox in line.split()[1:]:
#         img2=img.copy()
#         x1,y1,x2,y2,cl=map(int,bbox.strip().split(','))
#         cv2.rectangle(img2,(x1,y1),(x2,y2),(0,255,255),5)
#         while True:
#             cv2.imshow("frame",img2)
#             key=cv2.waitKey(1)
#             if key==ord('c'):
#                 updated_box.append(",".join(map(str,[x1,y1,x2,y2,cl])))
#                 break
#             if key==ord('b'):
#                 cl=1
#                 print(updated_box)
#                 # print(",".join(map(str,[x1,y1,x2,y2,cl])))
#                 updated_box.append(",".join(map(str,[x1,y1,x2,y2,cl])))
#                 break
#             if key==ord('q'):
#                 flag=True
#         if flag:
#             break
#     if flag:
#         break
#     cv2.destroyAllWindows()
#     out.write(" ".join(updated_box)+"\n")

# out.close()
# a.close()
# # print(none_img)
# print("done")

# # ['lskdfjlskdjf','1,2,3,4,0']






import os 
import cv2

otname=os.getcwd().split('/')[-1]
txt_path="./"+str(otname)+"_ann.txt"
output_path="./"+str(otname)+"_ann_out.txt"
RL=[]
try:
    for rl in open(output_path,"r"):
        RL.append(rl.split()[0])
except:
    pass
lines=[]
a=open(txt_path)
for line in a:
    if not line.split()[0] in RL:
        lines.append(line)


out1=open(output_path,'a')


out=[]
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
none_img=[]

i=0
while i<len(lines):
    flag=False
    flag1=False
    updated_box=[]
    imgpath=lines[i].split()[0]
    updated_box.append(imgpath)
    img=cv2.imread("./"+imgpath)
    if img is None:
        print("cant open image please check")
        none_img.append(imgpath)
        continue
    for bbox in lines[i].split()[1:]:
        img2=img.copy()
        x1,y1,x2,y2,cl=map(int,bbox.strip().split(','))
        cv2.rectangle(img2,(x1,y1),(x2,y2),(0,255,255),5)
        while True:
            cv2.imshow("frame",img2)
            key=cv2.waitKey(1)
            if key==ord('c'):
                updated_box.append(",".join(map(str,[x1,y1,x2,y2,cl])))
                break
            if key==ord('b'):
                cl=1
                print(updated_box)
                # print(",".join(map(str,[x1,y1,x2,y2,cl])))
                updated_box.append(",".join(map(str,[x1,y1,x2,y2,cl])))
                break
            if key==ord('p'):
                out.pop()
                i-=1
                flag1=True
                cv2.destroyAllWindows()
                break
            if key==ord('q'):
                flag=True
                break
        if flag:
            break
        if flag1:
            break
    if flag:
        break
    if not flag1:
        out.append(" ".join(updated_box))
        print(out)
        i+=1
cv2.destroyAllWindows()
print(out)
out1.write("\n".join(out))