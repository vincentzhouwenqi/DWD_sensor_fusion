# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rockauto_msgs/TunedResult.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rockauto_msgs.msg
import std_msgs.msg

class TunedResult(genpy.Message):
  _md5sum = "ddef3f42dffa20afab285bb50468c18e"
  _type = "rockauto_msgs/TunedResult"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
ColorSet Red
ColorSet Yellow
ColorSet Green

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: rockauto_msgs/ColorSet
ValueSet Hue
ValueSet Sat
ValueSet Val

================================================================================
MSG: rockauto_msgs/ValueSet
int32 center
int32 range
"""
  __slots__ = ['header','Red','Yellow','Green']
  _slot_types = ['std_msgs/Header','rockauto_msgs/ColorSet','rockauto_msgs/ColorSet','rockauto_msgs/ColorSet']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,Red,Yellow,Green

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TunedResult, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Red is None:
        self.Red = rockauto_msgs.msg.ColorSet()
      if self.Yellow is None:
        self.Yellow = rockauto_msgs.msg.ColorSet()
      if self.Green is None:
        self.Green = rockauto_msgs.msg.ColorSet()
    else:
      self.header = std_msgs.msg.Header()
      self.Red = rockauto_msgs.msg.ColorSet()
      self.Yellow = rockauto_msgs.msg.ColorSet()
      self.Green = rockauto_msgs.msg.ColorSet()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_18i().pack(_x.Red.Hue.center, _x.Red.Hue.range, _x.Red.Sat.center, _x.Red.Sat.range, _x.Red.Val.center, _x.Red.Val.range, _x.Yellow.Hue.center, _x.Yellow.Hue.range, _x.Yellow.Sat.center, _x.Yellow.Sat.range, _x.Yellow.Val.center, _x.Yellow.Val.range, _x.Green.Hue.center, _x.Green.Hue.range, _x.Green.Sat.center, _x.Green.Sat.range, _x.Green.Val.center, _x.Green.Val.range))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Red is None:
        self.Red = rockauto_msgs.msg.ColorSet()
      if self.Yellow is None:
        self.Yellow = rockauto_msgs.msg.ColorSet()
      if self.Green is None:
        self.Green = rockauto_msgs.msg.ColorSet()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.Red.Hue.center, _x.Red.Hue.range, _x.Red.Sat.center, _x.Red.Sat.range, _x.Red.Val.center, _x.Red.Val.range, _x.Yellow.Hue.center, _x.Yellow.Hue.range, _x.Yellow.Sat.center, _x.Yellow.Sat.range, _x.Yellow.Val.center, _x.Yellow.Val.range, _x.Green.Hue.center, _x.Green.Hue.range, _x.Green.Sat.center, _x.Green.Sat.range, _x.Green.Val.center, _x.Green.Val.range,) = _get_struct_18i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_18i().pack(_x.Red.Hue.center, _x.Red.Hue.range, _x.Red.Sat.center, _x.Red.Sat.range, _x.Red.Val.center, _x.Red.Val.range, _x.Yellow.Hue.center, _x.Yellow.Hue.range, _x.Yellow.Sat.center, _x.Yellow.Sat.range, _x.Yellow.Val.center, _x.Yellow.Val.range, _x.Green.Hue.center, _x.Green.Hue.range, _x.Green.Sat.center, _x.Green.Sat.range, _x.Green.Val.center, _x.Green.Val.range))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.Red is None:
        self.Red = rockauto_msgs.msg.ColorSet()
      if self.Yellow is None:
        self.Yellow = rockauto_msgs.msg.ColorSet()
      if self.Green is None:
        self.Green = rockauto_msgs.msg.ColorSet()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.Red.Hue.center, _x.Red.Hue.range, _x.Red.Sat.center, _x.Red.Sat.range, _x.Red.Val.center, _x.Red.Val.range, _x.Yellow.Hue.center, _x.Yellow.Hue.range, _x.Yellow.Sat.center, _x.Yellow.Sat.range, _x.Yellow.Val.center, _x.Yellow.Val.range, _x.Green.Hue.center, _x.Green.Hue.range, _x.Green.Sat.center, _x.Green.Sat.range, _x.Green.Val.center, _x.Green.Val.range,) = _get_struct_18i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_18i = None
def _get_struct_18i():
    global _struct_18i
    if _struct_18i is None:
        _struct_18i = struct.Struct("<18i")
    return _struct_18i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
