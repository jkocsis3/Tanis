;; Auto-generated. Do not edit!


(when (boundp 'angela::motormsg)
  (if (not (find-package "ANGELA"))
    (make-package "ANGELA"))
  (shadow 'motormsg (find-package "ANGELA")))
(unless (find-package "ANGELA::MOTORMSG")
  (make-package "ANGELA::MOTORMSG"))

(in-package "ROS")
;;//! \htmlinclude motormsg.msg.html


(defclass angela::motormsg
  :super ros::object
  :slots (_rate _direction ))

(defmethod angela::motormsg
  (:init
   (&key
    ((:rate __rate) 0.0)
    ((:direction __direction) 0.0)
    )
   (send-super :init)
   (setq _rate (float __rate))
   (setq _direction (float __direction))
   self)
  (:rate
   (&optional __rate)
   (if __rate (setq _rate __rate)) _rate)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:serialization-length
   ()
   (+
    ;; float32 _rate
    4
    ;; float32 _direction
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _rate
       (sys::poke _rate (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _direction
       (sys::poke _direction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _rate
     (setq _rate (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _direction
     (setq _direction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get angela::motormsg :md5sum-) "153a52f0077559b064690b516499badc")
(setf (get angela::motormsg :datatype-) "angela/motormsg")
(setf (get angela::motormsg :definition-)
      "float32 rate
float32 direction
")



(provide :angela/motormsg "153a52f0077559b064690b516499badc")


