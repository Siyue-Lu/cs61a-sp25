(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  (define (helper i lst)
    (if (null? lst) '()
                    (cons (list i (car lst))
                          (helper (+ i 1) (cdr lst)))))
  (helper 0 s))
;; Problem 16

;; Merge two lists S1 and S2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? s1 s2)
  (cond ((null? s1) s2)
        ((null? s2) s1)
        ((ordered? (car s1) (car s2))
                    (cons (car s1)
                          (merge ordered? (cdr s1) s2)))
        (else
         (cons (car s2)
               (merge ordered? s1 (cdr s2)))))
  )

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         expr
         )
        ((quoted? expr)
          expr
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
               (cons form (cons params (map let-to-lambda body)))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
               (let ((zips (zip values)))
                    ; ((lambda form body) args)
                    (cons
                      (cons 'lambda
                            (cons (car zips)  ; form
                                  (map let-to-lambda body)))  ; body
                      (map let-to-lambda (cadr zips))))  ; args
           ))
        (else
          (cons (car expr) (map let-to-lambda (cdr expr)))
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  (if (null? pairs)
      '(() ())
      (if (null? (car pairs))
          '()  ; ←─────────────────────────────────────────────┐
          (cons (map car pairs)  ;       ┃ |x1...xy| ┃ ↧ ┃     │
                (zip (map cdr pairs))))))  ; (zip (()1...()y)) ┘