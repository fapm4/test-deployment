import base64 

def read_image(image_file):
	with open(image_file, "rb") as img_file:
		b64_string = base64.b64encode(img_file.read()).decode()
	return f"data:image/{image_file.split('.')[-1]};base64,{b64_string}"