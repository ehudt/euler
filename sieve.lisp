(defun filter (pred lst)
	(cond ((null lst) nil)
		((funcall pred (car lst)) (cons (car lst) (filter (pred (cdr lst)))))
		(t (filter pred (cdr lst)))))

(defun car_str (stream)
	(car stream))

(defun cdr_str (stream)
	(funcall (cdr stream))
)

(defun cons_str (x stream)
	(list x (lambda () stream)))

(defun empty-streamp (stream)
	(null stream))

(defun make-empty-stream () 
	nil)

(defun filter_stream (pred stream)
	(cond 	((empty-streamp stream) (make-empty-stream))
			((funcall pred (car_str stream))
				(cons_str (car_str stream) 
					(filter_stream pred (cdr_str stream))))
			(t (filter_stream pred (cdr_str stream)))))

(defun int_stream (from)
	(cons_str from (int_stream (1+ from))))

(defun sieve (stream)
	(cons_str (car_str stream) 
		(filter_stream (lambda (x) (not (= (mod x (car_str stream)) 0))) 
			(cdr_str stream))
	))

(defun get_items(stream n)
	(if (= n 0) '() 
		(cons (car_str stream) (get_items (cdr_str stream) (1- n)))
		))

(defun sieve_test (x) (get_items (sieve (int_stream 2)) x))

;;; (sieve_test 5)

;;;(get_items (filter_stream (lambda (x) (= (mod x 2) 1)) (int_stream 1)) 20) 
(get_items (int_stream 2) 5)
