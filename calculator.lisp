
(defvar A ) 
(defvar B ) 
(defvar C ) 
(defvar D)

(defun bits (value)
  (format t "~v,'~B" 64 value))

(write-line "Welcome To Calculator") 


(write-line "Enter A: ") 
(setq A (read)) 
(bits A)
(terpri)

(write-line "Enter B: ") 
(setq B (read)) 
(bits B)
 
(sb-thread:make-thread (lambda () (progn (sleep 2)
(setq C (+ A B)) 
(write-line "Addition Of Two Numbers: ") 
(bits C)
(terpri))))

(sb-thread:make-thread (lambda () (progn (sleep 3)
(setq c (- A B)) 
(write-line "Substraction Of Two Numbers: ") 
(bits C)
(terpri))))
	 
(sb-thread:make-thread (lambda () (progn (sleep 4)
(setq c (* A B)) 
(write-line "Multiplication Of Two Numbers: ") 
(bits C)
(terpri))))

(sb-thread:make-thread (lambda () (progn (sleep 5)
(setq c (/ A B)) 
(write-line "Division Of Two Numbers: ") 
(bits C)
(terpri))))

