#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

void setup() {
    Serial.begin(9600);
    if (!bmp.begin()) {
        Serial.println("BMP180 not found!");
        while (1);
    }
}

void loop() {
    float temperature = bmp.readTemperature();
    float pressure = bmp.readPressure() / 100.0; // Convert Pa to hPa
    float altitude = bmp.readAltitude();

    Serial.print(temperature);
    Serial.print(",");
    Serial.print(pressure);
    Serial.print(",");
    Serial.println(altitude);

    delay(500);
}
