
(cl:in-package :asdf)

(defsystem "dimos_test-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Sonar" :depends-on ("_package_Sonar"))
    (:file "_package_Sonar" :depends-on ("_package"))
  ))