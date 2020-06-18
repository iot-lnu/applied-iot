function Decoder(bytes, port) {
  // Decode an uplink message from a buffer
  // (array) of bytes to an object of fields.

  // first two bytes are for co2. No need of signed, and range of sensor is 400-8192.

  var co2 = (bytes[0] << 8) | bytes[1];

  // third and fourth bytes are for VOC. range 0-1187de
  var voc = (bytes[2] << 8) | bytes[3];

  return {
    co2: co2,
    voc: voc
  }
}
