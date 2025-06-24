(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false))

(define (square n) (* n n))

(define (pow-expr base exp)
        (cond ((zero? exp) 1)
              ((odd? exp) `(* ,base ,(pow-expr base (- exp 1))))
              (else `(square ,(pow-expr base (/ exp 2))))))

(define-macro (repeat n expr)
  ; without lambda expr would get evaluated and executed, returning result but not the f itself
  `(repeated-call ,n (lambda () ,expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      ; f is lambda (), needs to be called by (f)
      (f)
      (begin
        (f)
        (repeated-call (- n 1) f))))
