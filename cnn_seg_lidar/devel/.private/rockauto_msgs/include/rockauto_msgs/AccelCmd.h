// Generated by gencpp from file rockauto_msgs/AccelCmd.msg
// DO NOT EDIT!


#ifndef ROCKAUTO_MSGS_MESSAGE_ACCELCMD_H
#define ROCKAUTO_MSGS_MESSAGE_ACCELCMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace rockauto_msgs
{
template <class ContainerAllocator>
struct AccelCmd_
{
  typedef AccelCmd_<ContainerAllocator> Type;

  AccelCmd_()
    : header()
    , accel(0)  {
    }
  AccelCmd_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , accel(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _accel_type;
  _accel_type accel;





  typedef boost::shared_ptr< ::rockauto_msgs::AccelCmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rockauto_msgs::AccelCmd_<ContainerAllocator> const> ConstPtr;

}; // struct AccelCmd_

typedef ::rockauto_msgs::AccelCmd_<std::allocator<void> > AccelCmd;

typedef boost::shared_ptr< ::rockauto_msgs::AccelCmd > AccelCmdPtr;
typedef boost::shared_ptr< ::rockauto_msgs::AccelCmd const> AccelCmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rockauto_msgs::AccelCmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rockauto_msgs::AccelCmd_<ContainerAllocator1> & lhs, const ::rockauto_msgs::AccelCmd_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.accel == rhs.accel;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rockauto_msgs::AccelCmd_<ContainerAllocator1> & lhs, const ::rockauto_msgs::AccelCmd_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rockauto_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rockauto_msgs::AccelCmd_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rockauto_msgs::AccelCmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rockauto_msgs::AccelCmd_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a93722f4689381b03f4eb4c0b2c4a748";
  }

  static const char* value(const ::rockauto_msgs::AccelCmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa93722f4689381b0ULL;
  static const uint64_t static_value2 = 0x3f4eb4c0b2c4a748ULL;
};

template<class ContainerAllocator>
struct DataType< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rockauto_msgs/AccelCmd";
  }

  static const char* value(const ::rockauto_msgs::AccelCmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"int32 accel\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::rockauto_msgs::AccelCmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.accel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct AccelCmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rockauto_msgs::AccelCmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rockauto_msgs::AccelCmd_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "accel: ";
    Printer<int32_t>::stream(s, indent + "  ", v.accel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROCKAUTO_MSGS_MESSAGE_ACCELCMD_H
