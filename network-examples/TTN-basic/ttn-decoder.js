function Decoder(bytes, port) {
  // Decode an uplink message from a buffer
  // (array) of bytes to an object of fields.
  var decoded = {};

  // little endian <
  // big endian >
  // Note this if for TWO bytes ...

  // bitwise OR
  decoded.bitwise_or = bytes[1] << 8 | bytes[0];

  // plus ..
  decoded.plus = (bytes[1] << 8) + bytes[0];
  // times 256
  decoded.times = (bytes[1] * 256) + bytes[0];


  // if (port === 1) decoded.led = bytes[0];

  return decoded;
}
