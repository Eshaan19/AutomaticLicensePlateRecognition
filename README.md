# Automatic License Plate Recognition System
#### Video Demo:  <youtube.com/watch?v=BafHa0Fxpz8>
#### Description:

As we all know, ANPR is being used daily in many places, but it is still not widely used in India.
My project was a web application in which I created the extract function to extract the license plate number
which was done in python. Next, I created a homepage and an application page using HTML.
I integrated them using Flask. 

The major issue I faced was in using the Tesseract-OCR. But it was fun.
The two templates file contains the templates for my two webpages.

The extract.py is python library I created for ANPR. This library contains the function which help with the OCR.
The extract.py is being called in app.py for being used. It returns the License plate number and state which it belongs to.

The app.py is used to connect the webpages with the python backend using Flask.
The extract() is used here to get the license plate number and state.