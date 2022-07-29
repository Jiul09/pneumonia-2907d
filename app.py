{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "423b77e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "from werkzeug.utils import secure_filename\n",
    "#from skimage import io\n",
    "from keras.models import load_model\n",
    "#import cv2\n",
    "from PIL import Image #use PIL\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "334fe6f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def init():\n",
    "    if request.method == 'POST':\n",
    "        file = request.files['file']\n",
    "        print(\"File Received\")\n",
    "        filename = secure_filename(file.filename)\n",
    "        print(filename)\n",
    "        #Open the image form working derectory\n",
    "        \n",
    "        #file.save(app.config(\"static/\"+ filename)) #Heroku no need static\n",
    "        #file = open(app.config(\"static/\"+ filename,\"r\")) #Heroku no need static\n",
    "        image = Image.open(file)\n",
    "        model = load_model(\"Pneumonia\")\n",
    "        img = np.asarray(image)\n",
    "        img.resize((150,150,3))      \n",
    "        img = np.asarray(img, dtype=\"float32\") #need to transfer to np to reshape\n",
    "        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) #rgb to reshape to 1,100,100,3\n",
    "        pred = model.predict(img)\n",
    "        pred = \"WAITING\"  \n",
    "        return(render_template(\"index.html\", result=str(pred)))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"WAITING\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "58892e22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [18/Jul/2022 10:02:22] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File Received\n",
      "NORMAL2-IM-1427-0001.jpeg\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [18/Jul/2022 10:02:34] \"POST / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0394bd1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
