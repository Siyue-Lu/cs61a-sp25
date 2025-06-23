(define (curry-cook formals body)
  (if (null? formals)
      body
      ; extra parentheses to put parameter in list for building lambda
      `(lambda (,(car formals)) ,(curry-cook (cdr formals) body))))

(define (curry-consume curry args)
  (if (null? args)
      curry
      (curry-consume (curry (car args)) (cdr args))))

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons `cond
        (map (lambda (option)
                              ; (car (<expr> <options>)) -> <expr>
               (cons `(equal? ,(car (cdr switch-expr))
                              ; #t option
                              ,(car option))
                              ; #f option
                              (cdr option)))
            ; (car (cdr (<expr> <options>))) -> (car (<options>)) -> <options>
             (car (cdr (cdr switch-expr))))))
