#include <LiquidCrystal.h>
#include <DHT.h>
LiquidCrystal lcd(19,23,18,17,16,15);
const int pinoDHT = 22 ;
const int ledD2 = 2;
const int ledD4 = 4;
#define DHTTYPE DHT11
DHT dht(pinoDHT, DHTTYPE);

void setup() {
  //DHT.read11(pinoDHT);
  pinMode(ledD2, OUTPUT);
  pinMode(ledD4, OUTPUT);
  
  dht.begin();
  lcd.begin(16,2);
}
void loop() {
  //DHT.read11(pinoDHT);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.println("Umidade: ");
  lcd.print(dht.readHumidity());
  lcd.setCursor(0,1);
  lcd.print("Temperatura:");
  lcd.print(dht.readTemperature());
  
  // Verifica a temperatura e acende o LED correspondente
  if (dht.readTemperature() > 21) {
    digitalWrite(ledD2, LOW);
    digitalWrite(ledD4, HIGH);
  } else {
    digitalWrite(ledD2, HIGH);
    digitalWrite(ledD4, LOW);
  }

  delay(1000);
}  
