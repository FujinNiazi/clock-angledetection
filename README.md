# Angle Detection for Analogue Clocks

This program allows you to measure the angle between the hands of analogue clocks. 

It does this using **OpenCV** by detecting edges and then lines using *Canny* and *Hough Line Transform* and filtering through them.

It has two scripts:
- **1_clock** give the angle between the minute and hour hand of a single clock.
- **2_clcoks** gives the angle between the minute hands of two different clocks.

## Installation

Clone the repo
git clone https://github.com/FujinNiazi/clock-angledetection.git

Navigate to the main directory
cd clock-angledetection

Install dependencies
pip install -r requirements.txt

## Usage
Run either *detect_edges.py* in the respective directory for either 1 or 2 clocks. 

New samples can be added in the data folder and then have to be updated accordingly in *detect_edges.py*.

The following result was generated using the *clock1* example in the data folder. 

<img width="997" alt="test output" src="https://github.com/user-attachments/assets/9431efc4-8800-4992-8f58-8a0719062b61">

Note that the limits for the *Canny* and *Hough Line Transform* may need adjustment depending on the type of clock and its size. 

## License
This program is licensed under the Apache 2.0 License.

