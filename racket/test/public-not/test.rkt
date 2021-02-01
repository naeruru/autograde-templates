#lang racket

(require "../../not.rkt")

(with-output-to-file "output"
                     (lambda ()
                       (print (no #t))))
