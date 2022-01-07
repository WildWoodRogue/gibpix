#include "Adafruit_NeoPixel.h"
Adafruit_NeoPixel strip = Adafruit_NeoPixel(200, 2, NEO_GRB + NEO_KHZ800);


void setup() {
  Serial.begin(170200);
  pinMode(2,OUTPUT);
  
  strip.begin();
}

void loop() {

String a;

if (Serial.available() > 0) {
  //если есть доступные данные
for (int i=0 ; i<200; i++){
      String data1=Serial.readStringUntil('\n');
// int w=data1.indexOf('!');
// String index1=data1.substring(0,w);
//  int index=index1.toInt();
 int y=data1.indexOf('@');
 String r1=data1.substring(0,y);
  int r=r1.toInt();
 int t=data1.indexOf('#');
 String g1=data1.substring(y+1,t);
 int g=g1.toInt();
 String b1=data1.substring(t+1,data1.length());
  int b=b1.toInt();
  strip.setPixelColor(i, strip.Color(r*0.9, g*0.9, b*0.9));}
  
  strip.show();
  
    }strip.begin();
} 
