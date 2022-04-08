# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rockauto_msgs/VehicleCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import rockauto_msgs.msg
import std_msgs.msg

class VehicleCmd(genpy.Message):
  _md5sum = "153301368e83526f24c12f8e8cddf283"
  _type = "rockauto_msgs/VehicleCmd"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
rockauto_msgs/SteerCmd steer_cmd
rockauto_msgs/AccelCmd accel_cmd
rockauto_msgs/BrakeCmd brake_cmd
rockauto_msgs/LampCmd lamp_cmd
int32 gear
int32 mode
geometry_msgs/TwistStamped twist_cmd
rockauto_msgs/ControlCommand ctrl_cmd
int32 emergency

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
MSG: rockauto_msgs/SteerCmd
Header header
int32 steer

================================================================================
MSG: rockauto_msgs/AccelCmd
Header header
int32 accel

================================================================================
MSG: rockauto_msgs/BrakeCmd
Header header
int32 brake

================================================================================
MSG: rockauto_msgs/LampCmd
Header header
int32 l
int32 r

================================================================================
MSG: geometry_msgs/TwistStamped
# A twist with reference coordinate frame and timestamp
Header header
Twist twist

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: rockauto_msgs/ControlCommand
float64 linear_velocity
float64 linear_acceleration #m/s^2
float64 steering_angle
"""
  __slots__ = ['header','steer_cmd','accel_cmd','brake_cmd','lamp_cmd','gear','mode','twist_cmd','ctrl_cmd','emergency']
  _slot_types = ['std_msgs/Header','rockauto_msgs/SteerCmd','rockauto_msgs/AccelCmd','rockauto_msgs/BrakeCmd','rockauto_msgs/LampCmd','int32','int32','geometry_msgs/TwistStamped','rockauto_msgs/ControlCommand','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,steer_cmd,accel_cmd,brake_cmd,lamp_cmd,gear,mode,twist_cmd,ctrl_cmd,emergency

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VehicleCmd, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.steer_cmd is None:
        self.steer_cmd = rockauto_msgs.msg.SteerCmd()
      if self.accel_cmd is None:
        self.accel_cmd = rockauto_msgs.msg.AccelCmd()
      if self.brake_cmd is None:
        self.brake_cmd = rockauto_msgs.msg.BrakeCmd()
      if self.lamp_cmd is None:
        self.lamp_cmd = rockauto_msgs.msg.LampCmd()
      if self.gear is None:
        self.gear = 0
      if self.mode is None:
        self.mode = 0
      if self.twist_cmd is None:
        self.twist_cmd = geometry_msgs.msg.TwistStamped()
      if self.ctrl_cmd is None:
        self.ctrl_cmd = rockauto_msgs.msg.ControlCommand()
      if self.emergency is None:
        self.emergency = 0
    else:
      self.header = std_msgs.msg.Header()
      self.steer_cmd = rockauto_msgs.msg.SteerCmd()
      self.accel_cmd = rockauto_msgs.msg.AccelCmd()
      self.brake_cmd = rockauto_msgs.msg.BrakeCmd()
      self.lamp_cmd = rockauto_msgs.msg.LampCmd()
      self.gear = 0
      self.mode = 0
      self.twist_cmd = geometry_msgs.msg.TwistStamped()
      self.ctrl_cmd = rockauto_msgs.msg.ControlCommand()
      self.emergency = 0

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
      buff.write(_get_struct_3I().pack(_x.steer_cmd.header.seq, _x.steer_cmd.header.stamp.secs, _x.steer_cmd.header.stamp.nsecs))
      _x = self.steer_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i3I().pack(_x.steer_cmd.steer, _x.accel_cmd.header.seq, _x.accel_cmd.header.stamp.secs, _x.accel_cmd.header.stamp.nsecs))
      _x = self.accel_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i3I().pack(_x.accel_cmd.accel, _x.brake_cmd.header.seq, _x.brake_cmd.header.stamp.secs, _x.brake_cmd.header.stamp.nsecs))
      _x = self.brake_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i3I().pack(_x.brake_cmd.brake, _x.lamp_cmd.header.seq, _x.lamp_cmd.header.stamp.secs, _x.lamp_cmd.header.stamp.nsecs))
      _x = self.lamp_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4i3I().pack(_x.lamp_cmd.l, _x.lamp_cmd.r, _x.gear, _x.mode, _x.twist_cmd.header.seq, _x.twist_cmd.header.stamp.secs, _x.twist_cmd.header.stamp.nsecs))
      _x = self.twist_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_9di().pack(_x.twist_cmd.twist.linear.x, _x.twist_cmd.twist.linear.y, _x.twist_cmd.twist.linear.z, _x.twist_cmd.twist.angular.x, _x.twist_cmd.twist.angular.y, _x.twist_cmd.twist.angular.z, _x.ctrl_cmd.linear_velocity, _x.ctrl_cmd.linear_acceleration, _x.ctrl_cmd.steering_angle, _x.emergency))
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
      if self.steer_cmd is None:
        self.steer_cmd = rockauto_msgs.msg.SteerCmd()
      if self.accel_cmd is None:
        self.accel_cmd = rockauto_msgs.msg.AccelCmd()
      if self.brake_cmd is None:
        self.brake_cmd = rockauto_msgs.msg.BrakeCmd()
      if self.lamp_cmd is None:
        self.lamp_cmd = rockauto_msgs.msg.LampCmd()
      if self.twist_cmd is None:
        self.twist_cmd = geometry_msgs.msg.TwistStamped()
      if self.ctrl_cmd is None:
        self.ctrl_cmd = rockauto_msgs.msg.ControlCommand()
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
      end += 12
      (_x.steer_cmd.header.seq, _x.steer_cmd.header.stamp.secs, _x.steer_cmd.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.steer_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.steer_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.steer_cmd.steer, _x.accel_cmd.header.seq, _x.accel_cmd.header.stamp.secs, _x.accel_cmd.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.accel_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.accel_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.accel_cmd.accel, _x.brake_cmd.header.seq, _x.brake_cmd.header.stamp.secs, _x.brake_cmd.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.brake_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.brake_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.brake_cmd.brake, _x.lamp_cmd.header.seq, _x.lamp_cmd.header.stamp.secs, _x.lamp_cmd.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.lamp_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.lamp_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.lamp_cmd.l, _x.lamp_cmd.r, _x.gear, _x.mode, _x.twist_cmd.header.seq, _x.twist_cmd.header.stamp.secs, _x.twist_cmd.header.stamp.nsecs,) = _get_struct_4i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.twist_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.twist_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.twist_cmd.twist.linear.x, _x.twist_cmd.twist.linear.y, _x.twist_cmd.twist.linear.z, _x.twist_cmd.twist.angular.x, _x.twist_cmd.twist.angular.y, _x.twist_cmd.twist.angular.z, _x.ctrl_cmd.linear_velocity, _x.ctrl_cmd.linear_acceleration, _x.ctrl_cmd.steering_angle, _x.emergency,) = _get_struct_9di().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.steer_cmd.header.seq, _x.steer_cmd.header.stamp.secs, _x.steer_cmd.header.stamp.nsecs))
      _x = self.steer_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i3I().pack(_x.steer_cmd.steer, _x.accel_cmd.header.seq, _x.accel_cmd.header.stamp.secs, _x.accel_cmd.header.stamp.nsecs))
      _x = self.accel_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i3I().pack(_x.accel_cmd.accel, _x.brake_cmd.header.seq, _x.brake_cmd.header.stamp.secs, _x.brake_cmd.header.stamp.nsecs))
      _x = self.brake_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i3I().pack(_x.brake_cmd.brake, _x.lamp_cmd.header.seq, _x.lamp_cmd.header.stamp.secs, _x.lamp_cmd.header.stamp.nsecs))
      _x = self.lamp_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4i3I().pack(_x.lamp_cmd.l, _x.lamp_cmd.r, _x.gear, _x.mode, _x.twist_cmd.header.seq, _x.twist_cmd.header.stamp.secs, _x.twist_cmd.header.stamp.nsecs))
      _x = self.twist_cmd.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_9di().pack(_x.twist_cmd.twist.linear.x, _x.twist_cmd.twist.linear.y, _x.twist_cmd.twist.linear.z, _x.twist_cmd.twist.angular.x, _x.twist_cmd.twist.angular.y, _x.twist_cmd.twist.angular.z, _x.ctrl_cmd.linear_velocity, _x.ctrl_cmd.linear_acceleration, _x.ctrl_cmd.steering_angle, _x.emergency))
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
      if self.steer_cmd is None:
        self.steer_cmd = rockauto_msgs.msg.SteerCmd()
      if self.accel_cmd is None:
        self.accel_cmd = rockauto_msgs.msg.AccelCmd()
      if self.brake_cmd is None:
        self.brake_cmd = rockauto_msgs.msg.BrakeCmd()
      if self.lamp_cmd is None:
        self.lamp_cmd = rockauto_msgs.msg.LampCmd()
      if self.twist_cmd is None:
        self.twist_cmd = geometry_msgs.msg.TwistStamped()
      if self.ctrl_cmd is None:
        self.ctrl_cmd = rockauto_msgs.msg.ControlCommand()
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
      end += 12
      (_x.steer_cmd.header.seq, _x.steer_cmd.header.stamp.secs, _x.steer_cmd.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.steer_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.steer_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.steer_cmd.steer, _x.accel_cmd.header.seq, _x.accel_cmd.header.stamp.secs, _x.accel_cmd.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.accel_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.accel_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.accel_cmd.accel, _x.brake_cmd.header.seq, _x.brake_cmd.header.stamp.secs, _x.brake_cmd.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.brake_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.brake_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.brake_cmd.brake, _x.lamp_cmd.header.seq, _x.lamp_cmd.header.stamp.secs, _x.lamp_cmd.header.stamp.nsecs,) = _get_struct_i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.lamp_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.lamp_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.lamp_cmd.l, _x.lamp_cmd.r, _x.gear, _x.mode, _x.twist_cmd.header.seq, _x.twist_cmd.header.stamp.secs, _x.twist_cmd.header.stamp.nsecs,) = _get_struct_4i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.twist_cmd.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.twist_cmd.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.twist_cmd.twist.linear.x, _x.twist_cmd.twist.linear.y, _x.twist_cmd.twist.linear.z, _x.twist_cmd.twist.angular.x, _x.twist_cmd.twist.angular.y, _x.twist_cmd.twist.angular.z, _x.ctrl_cmd.linear_velocity, _x.ctrl_cmd.linear_acceleration, _x.ctrl_cmd.steering_angle, _x.emergency,) = _get_struct_9di().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4i3I = None
def _get_struct_4i3I():
    global _struct_4i3I
    if _struct_4i3I is None:
        _struct_4i3I = struct.Struct("<4i3I")
    return _struct_4i3I
_struct_9di = None
def _get_struct_9di():
    global _struct_9di
    if _struct_9di is None:
        _struct_9di = struct.Struct("<9di")
    return _struct_9di
_struct_i3I = None
def _get_struct_i3I():
    global _struct_i3I
    if _struct_i3I is None:
        _struct_i3I = struct.Struct("<i3I")
    return _struct_i3I
