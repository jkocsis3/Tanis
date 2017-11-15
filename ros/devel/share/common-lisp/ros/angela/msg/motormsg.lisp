; Auto-generated. Do not edit!


(cl:in-package angela-msg)


;//! \htmlinclude motormsg.msg.html

(cl:defclass <motormsg> (roslisp-msg-protocol:ros-message)
  ((rate
    :reader rate
    :initarg :rate
    :type cl:float
    :initform 0.0)
   (direction
    :reader direction
    :initarg :direction
    :type cl:float
    :initform 0.0))
)

(cl:defclass motormsg (<motormsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motormsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motormsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name angela-msg:<motormsg> is deprecated: use angela-msg:motormsg instead.")))

(cl:ensure-generic-function 'rate-val :lambda-list '(m))
(cl:defmethod rate-val ((m <motormsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader angela-msg:rate-val is deprecated.  Use angela-msg:rate instead.")
  (rate m))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <motormsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader angela-msg:direction-val is deprecated.  Use angela-msg:direction instead.")
  (direction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motormsg>) ostream)
  "Serializes a message object of type '<motormsg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'direction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motormsg>) istream)
  "Deserializes a message object of type '<motormsg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rate) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'direction) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motormsg>)))
  "Returns string type for a message object of type '<motormsg>"
  "angela/motormsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motormsg)))
  "Returns string type for a message object of type 'motormsg"
  "angela/motormsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motormsg>)))
  "Returns md5sum for a message object of type '<motormsg>"
  "153a52f0077559b064690b516499badc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motormsg)))
  "Returns md5sum for a message object of type 'motormsg"
  "153a52f0077559b064690b516499badc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motormsg>)))
  "Returns full string definition for message of type '<motormsg>"
  (cl:format cl:nil "float32 rate~%float32 direction~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motormsg)))
  "Returns full string definition for message of type 'motormsg"
  (cl:format cl:nil "float32 rate~%float32 direction~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motormsg>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motormsg>))
  "Converts a ROS message object to a list"
  (cl:list 'motormsg
    (cl:cons ':rate (rate msg))
    (cl:cons ':direction (direction msg))
))
