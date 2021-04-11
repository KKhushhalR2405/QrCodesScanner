import cv2
import pyzbar.pyzbar as pyzbar
import time


def display(im, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points;

    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
    # cv2.imshow("F",im)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
img = cv2.imread("image/test1.jpg")

t1 = time.time()
d = pyzbar.decode(img)
print("{:.3f}".format(time.time()-t1))
print(d)
display(img,d)

#cv2.imwrite("testoutput.jpg",img)

cv2.imshow("F",img)
cv2.waitKey(0)
cv2.destroyAllWindows()