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
  //decoded.plus = (bytes[1] << 8) + bytes[0];
  // times 256
  //decoded.times = (bytes[1] * 256) + bytes[0];

  // Decode 2 bytes to a signed integer. As the
  // bitwise operators in JavaScript expect 32
  // bits, this needs "sign extension" to support
  // negative values. Shifting 24 bits leftwards,
  // followed by shifting 16 bits to the right,
  // extends a "two's complement" negative value
  // such as 0xF6D4 into 0xFFFFF6D4.

  decoded.signed = (bytes[0] << 24 >> 16) | bytes[1];


  // if (port === 1) decoded.led = bytes[0];

  return decoded;
}
