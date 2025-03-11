It looks like you meant BMP180 with Arduino. The BMP180 is a barometric pressure sensor that can measure altitude, pressure, and temperature. It's commonly used in weather monitoring, altimeters, and navigation systems.

📌 Wiring BMP180 with Arduino
The BMP180 communicates using I2C. Here's how to connect it:

------------------------------------------
|BMP180 Pin |	Arduino Pin              |
------------------------------------------
| VCC	    | 3.3V                       |
| GND	    | GND                        |
| SDA	    | A4 (on Uno) / 21 (on Mega) |
| SCL	    | A5 (on Uno) / 20 (on Mega) |
------------------------------------------