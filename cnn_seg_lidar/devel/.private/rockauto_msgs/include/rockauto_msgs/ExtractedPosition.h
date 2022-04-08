// Generated by gencpp from file rockauto_msgs/ExtractedPosition.msg
// DO NOT EDIT!


#ifndef ROCKAUTO_MSGS_MESSAGE_EXTRACTEDPOSITION_H
#define ROCKAUTO_MSGS_MESSAGE_EXTRACTEDPOSITION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rockauto_msgs
{
template <class ContainerAllocator>
struct ExtractedPosition_
{
  typedef ExtractedPosition_<ContainerAllocator> Type;

  ExtractedPosition_()
    : signalId(0)
    , u(0)
    , v(0)
    , radius(0)
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , hang(0.0)
    , type(0)
    , linkId(0)
    , plId(0)  {
    }
  ExtractedPosition_(const ContainerAllocator& _alloc)
    : signalId(0)
    , u(0)
    , v(0)
    , radius(0)
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , hang(0.0)
    , type(0)
    , linkId(0)
    , plId(0)  {
  (void)_alloc;
    }



   typedef int32_t _signalId_type;
  _signalId_type signalId;

   typedef int32_t _u_type;
  _u_type u;

   typedef int32_t _v_type;
  _v_type v;

   typedef int32_t _radius_type;
  _radius_type radius;

   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _z_type;
  _z_type z;

   typedef double _hang_type;
  _hang_type hang;

   typedef int8_t _type_type;
  _type_type type;

   typedef int32_t _linkId_type;
  _linkId_type linkId;

   typedef int32_t _plId_type;
  _plId_type plId;





  typedef boost::shared_ptr< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> const> ConstPtr;

}; // struct ExtractedPosition_

typedef ::rockauto_msgs::ExtractedPosition_<std::allocator<void> > ExtractedPosition;

typedef boost::shared_ptr< ::rockauto_msgs::ExtractedPosition > ExtractedPositionPtr;
typedef boost::shared_ptr< ::rockauto_msgs::ExtractedPosition const> ExtractedPositionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator1> & lhs, const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator2> & rhs)
{
  return lhs.signalId == rhs.signalId &&
    lhs.u == rhs.u &&
    lhs.v == rhs.v &&
    lhs.radius == rhs.radius &&
    lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.hang == rhs.hang &&
    lhs.type == rhs.type &&
    lhs.linkId == rhs.linkId &&
    lhs.plId == rhs.plId;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator1> & lhs, const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rockauto_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0e48067eb51a80d53e09341230ac756f";
  }

  static const char* value(const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0e48067eb51a80d5ULL;
  static const uint64_t static_value2 = 0x3e09341230ac756fULL;
};

template<class ContainerAllocator>
struct DataType< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rockauto_msgs/ExtractedPosition";
  }

  static const char* value(const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This message defines the information required to describe a lamp (bulb)\n"
"# in a traffic signal, according to the information extracted from the ADAS Map\n"
"# and the extrinsic camera calibration\n"
"\n"
"int32 signalId  # Traffic Signal Lamp ID\n"
"int32 u         # Lamp ROI x in image coords\n"
"int32 v         # Lamp ROI y in image coords\n"
"int32 radius    # Lamp Radius\n"
"float64 x       # X position in map coordinates\n"
"float64 y       # Y position in map coordinates\n"
"float64 z       # Z position in map coordinates\n"
"float64 hang    # Azimuth \"Horizontal Angle\"\n"
"int8 type       # Lamp Type (red, yellow, green, ...)\n"
"int32 linkId    # Closest LinkID (lane) in VectorMap\n"
"int32 plId      # PoleID to which this Lamp belongs to\n"
;
  }

  static const char* value(const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.signalId);
      stream.next(m.u);
      stream.next(m.v);
      stream.next(m.radius);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.hang);
      stream.next(m.type);
      stream.next(m.linkId);
      stream.next(m.plId);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ExtractedPosition_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rockauto_msgs::ExtractedPosition_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rockauto_msgs::ExtractedPosition_<ContainerAllocator>& v)
  {
    s << indent << "signalId: ";
    Printer<int32_t>::stream(s, indent + "  ", v.signalId);
    s << indent << "u: ";
    Printer<int32_t>::stream(s, indent + "  ", v.u);
    s << indent << "v: ";
    Printer<int32_t>::stream(s, indent + "  ", v.v);
    s << indent << "radius: ";
    Printer<int32_t>::stream(s, indent + "  ", v.radius);
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<double>::stream(s, indent + "  ", v.z);
    s << indent << "hang: ";
    Printer<double>::stream(s, indent + "  ", v.hang);
    s << indent << "type: ";
    Printer<int8_t>::stream(s, indent + "  ", v.type);
    s << indent << "linkId: ";
    Printer<int32_t>::stream(s, indent + "  ", v.linkId);
    s << indent << "plId: ";
    Printer<int32_t>::stream(s, indent + "  ", v.plId);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROCKAUTO_MSGS_MESSAGE_EXTRACTEDPOSITION_H
