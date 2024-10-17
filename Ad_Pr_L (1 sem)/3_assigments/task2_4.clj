(defn is-prime? [n]
  (loop [i 2]
    (cond
      (> (* i i) n) true
      (= 0 (rem n i)) false
      :else (recur (inc i)))))

(defn generate-primes [n]
  (loop [count 0
         number 2
         primes []]
    (if (= count n)
      primes
      (if (is-prime? number)
        (recur (inc count) (inc number) (conj primes number))
        (recur count (inc number) primes)))))

(def first-100-primes (generate-primes 100))

(doseq [[index prime] (map-indexed vector first-100-primes)]
  (println (str (inc index) " " prime)))



