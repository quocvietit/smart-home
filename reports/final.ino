

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTTYPE DHT11   // DHT 11
#define DHTPIN 12
DHT dht(DHTPIN, DHTTYPE);
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
//DHT dht(DHTPIN, DHTTYPE);
// Update these with values suitable for your network.
#define ledPin 14
#define lightsensor 5
#define gassensor 4


const char* ssid = "NOVA P3";
const char* password = "123456789";
const char* mqtt_server = "192.168.43.221";
const char* userName = "pi";
const char* passWord = "123";
/*const char* ssid = "GalaxyS7";
  const char* password = "12345689";
  //const char* mqtt_server = "192.168.43.221";
  const char* mqtt_server = "broker.mqtt-dashboard.com";*/
WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup_wifi() {

  //delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

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

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(ledPin, HIGH);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(ledPin, LOW);  // Turn the LED off by making the voltage HIGH
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
    if (client.connect(clientId.c_str(), userName, passWord)) {
      //if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      //client.publish("home/room/flash_light", "hello world");
      // ... and resubscribe
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

  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  setup_wifi();
  dht.begin();
  client.setServer(mqtt_server, 1883);
  //
  client.setCallback(callback);


}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    //light
    int val = analogRead(lightsensor);
    String msg;
    // msg= msg+ val;
    if (val > 50)
      msg = "0";
    else
      msg = "1";
    char message[58];
    msg.toCharArray(message, 58);
    Serial.println(message);
    client.publish("LIVINGROOM/LIGHT", message);

    //gas

    int val2 = analogRead(gassensor);
    String msg2;
    // msg2= msg2+ val2;
    if (val2 < 50)
      msg2 = "0";
    else
      msg2 = "1";
    char message2[58];
    msg2.toCharArray(message2, 58);
    Serial.println(message2);
    client.publish("LIVINGROOM/GAS", message2);

    //nhiet do, do am
    int h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
    // Read temperature as Fahrenheit (isFahrenheit = true)
    /*float f = dht.readTemperature(true);

      // Check if any reads failed and exit early (to try again).1
      if (isnan(h) || isnan(t) || isnan(f)) {
      Serial.println(F("Failed to read from DHT sensor!"));
      return;
      }*/
    char message5[58];
    String msg5;
    msg5 = msg5 + h;
    Serial.println(message5);
    msg5.toCharArray(message5, 58);
    client.publish("LIVINGROOM/HUMIDITY", message5);

    char message4[58];
    String msg4;
    msg4 = msg4 + t;
    msg4.toCharArray(message4, 58);
    Serial.println(message4);
    client.publish("LIVINGROOM/TEMPERATURE", message4);

    //ledpin
    if ( digitalRead(ledPin) )

      client.publish("LIVINGROOM/FLASH_LIGHT", "1");
    else
      client.publish("LIVINGROOM/FLASH_LIGHT", "0");



  }
  //Serial.println(WiFi.localIP());
  //client.subscribe("LIVINGROOM/FLASH_LIGHT/CONTROL");
  delay(2000);
}
