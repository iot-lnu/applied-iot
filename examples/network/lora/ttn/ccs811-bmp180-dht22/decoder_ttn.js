function Decoder(bytes, port) {
  // Decode an uplink message from a buffer
  // (array) of bytes to an object of fields.

  // byte 0,1 are for co2. No need of signed, and range of sensor is 400-8192.
  var co2 = (bytes[0] << 8) | bytes[1];
  // byte 2,3 are for VOC. range 0-1187de
  var voc = (bytes[2] << 8) | bytes[3];
  // byte 4,5 pressure in hPa
  var bmp_pressure = (bytes[4] << 8) | bytes[5];
  // byte 6 temp from bmp
  var bmp_temp = bytes[6];
  // byte 7 temp from dht
  var dht_temp = bytes[7];
  // byte 8 RH from dht
  var dht_RH = bytes[8];

  return {
    co2: co2,
    voc: voc,
    bmp_pressure: (bmp_pressure / (65536 / 800)) + 300,
    bmp_temp: (bmp_temp) / (256/125) - 40,
    dht_temp: (dht_temp) / (256/125) - 40,
    dht_RH: dht_RH / (256/100)
  }
}
