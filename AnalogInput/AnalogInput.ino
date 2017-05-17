
int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 2;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor

const int BLimit = 21;
int buttonDecay = 0;

const int ZeroLimit = 5;
bool firstZero = false;

const int MSize = 500;
int mean[MSize];
int index = 0;
float sum = 0;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, INPUT);
  Serial.begin(9600);
  delay(1000);
  Serial.println(9999);
}

void loop() {

start:  
  check_led();
  
  sensorValue = analogRead(sensorPin);
  mean[index] = sensorValue;  
  index = (index+1) % MSize;
  if (sensorValue == 0 && firstZero == false) {
    firstZero = true;
    for (int i=0 ; i<ZeroLimit ; i++) {
      if(digitalRead(ledPin) == LOW)
        firstZero = false;
        goto start;
      delay(100);
    }    
  } else if (sensorValue != 0)
    firstZero = false;
    
 

  if (index == 0) {
    sum = 0;
    for (int i=0 ; i<MSize ; i++)
      sum += mean[i];
      
    float mv = sum/MSize;
      
    char temp[50];
    sprintf(temp, "%04d", (int)mv);
    Serial.println(temp);
  }
}


bool check_led() {
  if(digitalRead(ledPin) == LOW) {
    buttonDecay = BLimit;
    while(buttonDecay) {    
      delay(90);
      //Serial.println(buttonDecay);
      if(digitalRead(ledPin) == HIGH)
        buttonDecay--;        
      else
        buttonDecay = BLimit;            
    }
    return true;
  }
  return false;
}
