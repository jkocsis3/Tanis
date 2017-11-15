
(cl:in-package :asdf)

(defsystem "angela-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "motormsg" :depends-on ("_package_motormsg"))
    (:file "_package_motormsg" :depends-on ("_package"))
  ))