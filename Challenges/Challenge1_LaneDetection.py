import cv2
import numpy as np
import time

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass



def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (3,3), 0 )
    vertices = np.array([[80,440],[240,330], [326,327], [380,440]], np.int32)
    processed_img = roi(processed_img, [vertices])
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    draw_lines(processed_img,lines)
    return processed_img

def main():
	width = 600
	height = 337
	dim = (width, height)
	count = 1
	
	while True:
		img_name = 'LANE/'+ '{:04}'.format(count) + '.jpg'
		image = cv2.imread(img_name, 1)
		frame = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
		frame2 = process_img(frame)
		cv2.imshow('frame', frame2)
		time.sleep(0.5)
		k = cv2.waitKey(5) & 0xFF

		if k == 27 or count == 699:
			break
			
		count+=1

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()
