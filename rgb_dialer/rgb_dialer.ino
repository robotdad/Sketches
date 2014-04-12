#include "SPI.h"
#include "Adafruit_WS2801.h"

//pin 1 of pots tied to ground, pin 3 to power, wiper as assigned below to the arduino
const int redPotPin = 0;
const int greenPotPin = 1;
const int bluePotPin = 2;
const int faderPotPin = 3;

//since I'm always looking it up, 5v for the strip of pixels I have...
uint8_t dataPin  = 2;    // Yellow wire on Adafruit Pixels
uint8_t clockPin = 3;    // Green wire on Adafruit Pixels
Adafruit_WS2801 strip = Adafruit_WS2801(25, dataPin, clockPin);

int colorRed;
int colorGreen;
int colorBlue;
int refresh;
char msg [50];

void setup()
{
  strip.begin();
  strip.show();
  //Serial.begin(9600);
}

void loop()
{
  colorRed = (255 - map(analogRead(redPotPin), 0, 1024, 0, 255));
  colorGreen = (255 - map(analogRead(greenPotPin), 0, 1024, 0, 255));
  colorBlue = (255 - map(analogRead(bluePotPin), 0, 1024, 0, 255));
  refresh = (100 - map(analogRead(faderPotPin), 0, 1024, 0, 100));
  colorWipe(Color(colorRed, colorGreen, colorBlue), refresh);
  //sprintf(msg, "Red %d, Green %d, Blue %d Brightness %d", colorRed, colorGreen, colorBlue, refresh); 
  //Serial.println(msg);
}

// fill the dots one after the other with said color
// good for testing purposes
void colorWipe(uint32_t c, uint8_t wait) {
  int i;
  
  for (i=0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}

/* Helper functions */

// Create a 24 bit color value from R,G,B
uint32_t Color(byte r, byte g, byte b)
{
  uint32_t c;
  c = r;
  c <<= 8;
  c |= g;
  c <<= 8;
  c |= b;
  return c;
}
