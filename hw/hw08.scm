(define (ascending? s)
    ; null? returns #t/#f
    (or (null? s)
        (null? (cdr s))
        ; (if (> (car s) (car (cdr s)))
        ;     #f
        ;     (ascending? (cdr s)))
        (and (<= (car s) (car (cdr s)))
            (ascending? (cdr s)))))

(define (my-filter pred s)
    ; (if (null? s)
    ;     '()
    ;     (if (pred (car s))
    ;         (cons (car s)
    ;             (my-filter pred (cdr s)))
    ;         (my-filter pred (cdr s))))
    
    (cond
        ((null? s)
            '())
        ((pred (car s))
            (cons (car s)
                (my-filter pred (cdr s))))
        (else
            (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
    (cond
        ((null? lst1)
            lst2)
        ((null? lst2)
            lst1)
        (else
            (cons (car lst1)
                (cons (car lst2)
                    (interleave (cdr lst1) (cdr lst2)))))))

(define (no-repeats s)
    ; ; O(n²) for filtering everyone in rest with every first
    ; (if (null? s)
    ;     '()
    ;     ; 1: taking first
    ;     (cons (car s)
    ;         ; 3: having new list in recursive call to check if
    ;         ; new first repeats, taking whole thing as rest
    ;         (no-repeats
    ;             ; 2: filtering rest with first, returning new list
    ;             (filter
    ;                 (lambda (e)
    ;                     (not (= e (car s))))
    ;                     (cdr s)))))

    ; O(n), going through everyone in s while saving seen and checking
    (define (helper s seen)
        (cond
            ((null? s)
                '())
            ((member (car s) seen)
                (helper (cdr s) seen))
            (else
                ; actual returned list, seen just for saving unique (car s)
                (cons
                    (car s)
                    (helper
                        (cdr s)
                        (cons (car s) seen))))))
    (helper s '())
)
