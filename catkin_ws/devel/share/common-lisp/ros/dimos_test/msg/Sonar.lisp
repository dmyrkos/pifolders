; Auto-generated. Do not edit!


(cl:in-package dimos_test-msg)


;//! \htmlinclude Sonar.msg.html

(cl:defclass <Sonar> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass Sonar (<Sonar>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Sonar>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Sonar)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dimos_test-msg:<Sonar> is deprecated: use dimos_test-msg:Sonar instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Sonar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dimos_test-msg:header-val is deprecated.  Use dimos_test-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <Sonar>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dimos_test-msg:distance-val is deprecated.  Use dimos_test-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Sonar>) ostream)
  "Serializes a message object of type '<Sonar>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Sonar>) istream)
  "Deserializes a message object of type '<Sonar>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Sonar>)))
  "Returns string type for a message object of type '<Sonar>"
  "dimos_test/Sonar")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Sonar)))
  "Returns string type for a message object of type 'Sonar"
  "dimos_test/Sonar")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Sonar>)))
  "Returns md5sum for a message object of type '<Sonar>"
  "927a6968211c82bd71bee6aee6c4b1b6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Sonar)))
  "Returns md5sum for a message object of type 'Sonar"
  "927a6968211c82bd71bee6aee6c4b1b6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Sonar>)))
  "Returns full string definition for message of type '<Sonar>"
  (cl:format cl:nil "Header header~%float64 distance~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Sonar)))
  "Returns full string definition for message of type 'Sonar"
  (cl:format cl:nil "Header header~%float64 distance~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Sonar>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Sonar>))
  "Converts a ROS message object to a list"
  (cl:list 'Sonar
    (cl:cons ':header (header msg))
    (cl:cons ':distance (distance msg))
))
