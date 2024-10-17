(defn fibonacci [n]
  (if (or (= n 0) (= n 1))
    1
    (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(defn find-fib-divisible-by-7 []
  (loop [n 0
         count 0]
    (if (= count 6)
      (println "Six Fibonacci numbers divisible by 7 found.")
      (let [fib (fibonacci n)]
        (if (zero? (mod fib 7))
          (do
            (println "Fibonacci number" count "divisible by 7:" fib)
            (recur (inc n) (inc count)))
          (recur (inc n) count))))))

(find-fib-divisible-by-7)
