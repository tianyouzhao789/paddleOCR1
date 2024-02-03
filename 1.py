import numpy as np
import cv2
import matplotlib.pyplot as plt
# 1. 从paddleocr中import PaddleOCR类
from paddleocr import PaddleOCR
# 2. 声明PaddleOCR类
ocr = PaddleOCR()
img_path = '12.jpg'
# 3. 执行预测
result = ocr.ocr(img_path, rec=False)
# 4. 可视化检测结果
image = cv2.imread(img_path)
boxes = [line[0] for line in result]
for box in result:
    box = np.reshape(np.array(box), [-1, 1, 2]).astype(np.int64)
    image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)
# 画出读取的图片
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.show()

