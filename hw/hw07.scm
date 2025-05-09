(define (square n) (* n n))

(define (pow base exp)
  ; (if (zero? exp)
  ;     1
  ;     (if (= (modulo exp 2) 0)
  ;         (square (pow base (/ exp 2)))
  ;         (* base (pow base (- exp 1)))))

  (cond ((= exp 0) 1)
        ; one less pair of () causes exp to return and stop the procedure
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (pow base (- exp 1))))
        )
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
