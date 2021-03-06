// Generated by gencpp from file depthGet/BboxLes.msg
// DO NOT EDIT!


#ifndef DEPTHGET_MESSAGE_BBOXLES_H
#define DEPTHGET_MESSAGE_BBOXLES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <std_msgs/Header.h>
#include <depthGet/BboxL.h>

namespace depthGet
{
template <class ContainerAllocator>
struct BboxLes_
{
  typedef BboxLes_<ContainerAllocator> Type;

  BboxLes_()
    : header()
    , image_header()
    , bboxl()  {
    }
  BboxLes_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , image_header(_alloc)
    , bboxl(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::std_msgs::Header_<ContainerAllocator>  _image_header_type;
  _image_header_type image_header;

   typedef std::vector< ::depthGet::BboxL_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::depthGet::BboxL_<ContainerAllocator> >::other >  _bboxl_type;
  _bboxl_type bboxl;





  typedef boost::shared_ptr< ::depthGet::BboxLes_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::depthGet::BboxLes_<ContainerAllocator> const> ConstPtr;

}; // struct BboxLes_

typedef ::depthGet::BboxLes_<std::allocator<void> > BboxLes;

typedef boost::shared_ptr< ::depthGet::BboxLes > BboxLesPtr;
typedef boost::shared_ptr< ::depthGet::BboxLes const> BboxLesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::depthGet::BboxLes_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::depthGet::BboxLes_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::depthGet::BboxLes_<ContainerAllocator1> & lhs, const ::depthGet::BboxLes_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.image_header == rhs.image_header &&
    lhs.bboxl == rhs.bboxl;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::depthGet::BboxLes_<ContainerAllocator1> & lhs, const ::depthGet::BboxLes_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace depthGet

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::depthGet::BboxLes_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::depthGet::BboxLes_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::depthGet::BboxLes_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::depthGet::BboxLes_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::depthGet::BboxLes_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::depthGet::BboxLes_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::depthGet::BboxLes_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ce61082c6ddb14fe169b5449bc98b437";
  }

  static const char* value(const ::depthGet::BboxLes_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xce61082c6ddb14feULL;
  static const uint64_t static_value2 = 0x169b5449bc98b437ULL;
};

template<class ContainerAllocator>
struct DataType< ::depthGet::BboxLes_<ContainerAllocator> >
{
  static const char* value()
  {
    return "depthGet/BboxLes";
  }

  static const char* value(const ::depthGet::BboxLes_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::depthGet::BboxLes_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"Header image_header\n"
"BboxL[] bboxl\n"
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
"\n"
"================================================================================\n"
"MSG: depthGet/BboxL\n"
"float64 minx\n"
"float64 miny\n"
"float64 maxx\n"
"float64 maxy\n"
"float64 navi\n"
"float64 centerx\n"
"float64 centery\n"
;
  }

  static const char* value(const ::depthGet::BboxLes_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::depthGet::BboxLes_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.image_header);
      stream.next(m.bboxl);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BboxLes_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::depthGet::BboxLes_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::depthGet::BboxLes_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "image_header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.image_header);
    s << indent << "bboxl[]" << std::endl;
    for (size_t i = 0; i < v.bboxl.size(); ++i)
    {
      s << indent << "  bboxl[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::depthGet::BboxL_<ContainerAllocator> >::stream(s, indent + "    ", v.bboxl[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEPTHGET_MESSAGE_BBOXLES_H
