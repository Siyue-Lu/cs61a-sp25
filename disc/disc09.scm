; Return whether there are n perfect squares with no repeats that sum to total
    (define (fit total n)
        (define (f total n k)
            (if (and (= n 0) (= total 0))
                #t
            (if (< total (* k k))
                #f
            ; (if (f (- total (* k k)) (- n 1) (+ k 1))  ; counting (* k k)
            ;     #t
            ;     (f total n (+ k 1)))  ;  not counting (* k k)
            (or (f total n (+ k 1)) (f (- total (* k k)) (- n 1) (+ k 1)))
            )))
        (f total n 1))


(define with-list
        (list  ; automatically forming Link structure
            (list 'a 'b)
            'c
            'd
            (list 'e)
        )
    )

(define with-quote
        '(  ; quoting the whole chunk in brackets
            (a b)
            c
            d
            (e)
        )
    )

(define with-cons
        (cons  ; take car and cdr, used as Link(), (cons a (cons b (cons c)))
            (cons 'a (cons 'b nil))
                (cons 'c
                    (cons 'd
                        (cons (cons 'e nil)
                            nil )))
        )
    )


;;; Return a list of pairs containing the elements of s.
    ;;;
    ;;; scm> (pair-up '(3 4 5 6 7 8))
    ;;; ((3 4) (5 6) (7 8))
    ;;; scm> (pair-up '(3 4 5 6 7 8 9))
    ;;; ((3 4) (5 6) (7 8 9))
    (define (pair-up s)
        (if (<= (length s) 3)
            (list s)  ; return without (list) would be equivalent to (cons a b c)
            (cons
                (list (car s) (car (cdr s)))
                (pair-up (cdr (cdr s))))
        ))