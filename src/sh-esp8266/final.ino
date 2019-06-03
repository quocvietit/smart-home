

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTTYPE DHT11   // DHT 11
#define DHTPIN 12 // Digital pin connected to the DHT sensor(Serial GPIO12)
DHT dht(DHTPIN, DHTTYPE);

#define ledPin 14   // Digital pin connected to the led (Serial GPIO14)
#define lightsensor 5   // Digital pin connected to the light sensor (Serial GPIO05)
#define intensity A0    // Digital pin connected to the gas sensor (Serial ADC)

// Update these with values suitable for your network.
/*const char* ssid = "NOVA P3";  // WiFi username
  const char* password = "123456789"; // WiFi password
  const char* mqtt_server = "192.168.43.221";  // MQTT address
  const char* userName = "pi";  // MQTT username
  const char* passWord = "123";   // MQTT password*/
const char* ssid = "Sieunhanhong";
const char* password = "0799696143";
//const char* mqtt_server = "192.168.43.221";
const char* mqtt_server = "broker.mqtt-dashboard.com";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup_wifi() {

  //delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to Wifi");
  //Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
////print any message received for subscribed topic
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(ledPin, HIGH);
    // Turn the LED on (Note that LOW is the voltage level
    Serial.println("Turn on light");
  } else {
    digitalWrite(ledPin, LOW);  // Turn the LED off by making the voltage HIGH
    Serial.println("Turn off light");
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    //if (client.connect(clientId.c_str(), userName, passWord)) {
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      client.subscribe("LIVINGROOM/FLASH_LIGHT/CONTROL");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {

  pinMode(ledPin, OUTPUT);    //// initialize digital pin ledPin as an output.
  Serial.begin(9600); // Sets serial port for communication
  setup_wifi();
  dht.begin();
  client.setServer(mqtt_server, 1883); // connect to MQTT on gate 1883
  client.setCallback(callback); //Callback executed when message received
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;

    //Light Sensor
    int val = analogRead(lightsensor);  //read the value from the sensor
    String msg;
    // If there is no light, the value is 0. Greater than value 50 is dark
    if (val > 50)
      msg = "0";
    else
      msg = "1";
    char message[58];
    msg.toCharArray(message, 58);
    Serial.println("LIVINGROOM/LIGHT");
    Serial.println(message);
    Serial.println("---------------------");
    client.publish("LIVINGROOM/LIGHT", message);  //publish value 0 or 1 to MQTT. Th network is "LIVINGROOM/LIGHT"

    //Gas sensor

    int val2 = analogRead(intensity);  ////read the value from the sensor
    String msg2;
    //If the value is less than 500, it has no gas. if greater than 500, is has gas in air.
    if (val2 < 500)
      msg2 = "0";
    else
      msg2 = "1";
    char message2[58];
    msg2.toCharArray(message2, 58);
    Serial.println("LIVINGROOM/GAS");
    Serial.println(message2);
    Serial.println("---------------------");
    client.publish("LIVINGROOM/GAS", message2); //publish value 0 or 1 to MQTT. The network is "LIVINGROOM/GAS"

    //Humidity and Temperature Sensor
    // read the Humidity value from the sensor
    int h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();

    char message5[58];
    String msg5;
    msg5 = msg5 + h;
    Serial.println("LIVINGROOM/HUMIDITY");
    Serial.println(message5);
    Serial.println("---------------------");
    msg5.toCharArray(message5, 58);
    client.publish("LIVINGROOM/HUMIDITY", message5);// publish value of Humidity to MQTT. The network is LIVINGROOM/HUMIDITY. The value is from 0 to 100

    char message4[58];
    String msg4;
    msg4 = msg4 + t;
    msg4.toCharArray(message4, 58);
    Serial.println("LIVINGROOM/TEMPERATURE");
    Serial.println(message4);
    Serial.println("---------------------");
    client.publish("LIVINGROOM/TEMPERATURE", message4); // // publish value of Temperature to MQTT. The network is LIVINGROOM/TEMPERATURE. The value is from 0 to 100

    //Read the status of ledPin
    if ( digitalRead(ledPin) )
    {
      client.publish("LIVINGROOM/FLASH_LIGHT", "1"); // If the led pin is high the value send to MQTT is 1
      Serial.println("LIVINGROOM/FLASH_LIGHT");
      Serial.println("Light is on");
      Serial.println("---------------------");
    }

    else
    { client.publish("LIVINGROOM/FLASH_LIGHT", "0"); // If the led pin is low the value send to MQTT is 0
      Serial.println("LIVINGROOM/FLASH_LIGHT");
      Serial.println("Light is off");
      Serial.println("---------------------");
    }
  }
  delay(5000);
}
