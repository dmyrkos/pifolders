;; Auto-generated. Do not edit!


(when (boundp 'dimos_test::Sonar)
  (if (not (find-package "DIMOS_TEST"))
    (make-package "DIMOS_TEST"))
  (shadow 'Sonar (find-package "DIMOS_TEST")))
(unless (find-package "DIMOS_TEST::SONAR")
  (make-package "DIMOS_TEST::SONAR"))

(in-package "ROS")
;;//! \htmlinclude Sonar.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass dimos_test::Sonar
  :super ros::object
  :slots (_header _distance ))

(defmethod dimos_test::Sonar
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _distance (float __distance))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _distance
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _distance
     (setq _distance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get dimos_test::Sonar :md5sum-) "927a6968211c82bd71bee6aee6c4b1b6")
(setf (get dimos_test::Sonar :datatype-) "dimos_test/Sonar")
(setf (get dimos_test::Sonar :definition-)
      "Header header
float64 distance
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

")



(provide :dimos_test/Sonar "927a6968211c82bd71bee6aee6c4b1b6")


