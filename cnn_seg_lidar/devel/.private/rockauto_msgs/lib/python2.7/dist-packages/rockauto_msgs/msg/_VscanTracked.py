# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rockauto_msgs/VscanTracked.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import rockauto_msgs.msg

class VscanTracked(genpy.Message):
  _md5sum = "bff5c0a61020da26ef210837bea359b1"
  _type = "rockauto_msgs/VscanTracked"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Point position
float32 orientation
float32 velocity
GeometricRectangle geo_rect
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: rockauto_msgs/GeometricRectangle
float32 wl
float32 wr
float32 lf
float32 lb"""
  __slots__ = ['position','orientation','velocity','geo_rect']
  _slot_types = ['geometry_msgs/Point','float32','float32','rockauto_msgs/GeometricRectangle']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       position,orientation,velocity,geo_rect

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VscanTracked, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.orientation is None:
        self.orientation = 0.
      if self.velocity is None:
        self.velocity = 0.
      if self.geo_rect is None:
        self.geo_rect = rockauto_msgs.msg.GeometricRectangle()
    else:
      self.position = geometry_msgs.msg.Point()
      self.orientation = 0.
      self.velocity = 0.
      self.geo_rect = rockauto_msgs.msg.GeometricRectangle()

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
      buff.write(_get_struct_3d6f().pack(_x.position.x, _x.position.y, _x.position.z, _x.orientation, _x.velocity, _x.geo_rect.wl, _x.geo_rect.wr, _x.geo_rect.lf, _x.geo_rect.lb))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.geo_rect is None:
        self.geo_rect = rockauto_msgs.msg.GeometricRectangle()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.position.x, _x.position.y, _x.position.z, _x.orientation, _x.velocity, _x.geo_rect.wl, _x.geo_rect.wr, _x.geo_rect.lf, _x.geo_rect.lb,) = _get_struct_3d6f().unpack(str[start:end])
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
      buff.write(_get_struct_3d6f().pack(_x.position.x, _x.position.y, _x.position.z, _x.orientation, _x.velocity, _x.geo_rect.wl, _x.geo_rect.wr, _x.geo_rect.lf, _x.geo_rect.lb))
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
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.geo_rect is None:
        self.geo_rect = rockauto_msgs.msg.GeometricRectangle()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.position.x, _x.position.y, _x.position.z, _x.orientation, _x.velocity, _x.geo_rect.wl, _x.geo_rect.wr, _x.geo_rect.lf, _x.geo_rect.lb,) = _get_struct_3d6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d6f = None
def _get_struct_3d6f():
    global _struct_3d6f
    if _struct_3d6f is None:
        _struct_3d6f = struct.Struct("<3d6f")
    return _struct_3d6f
