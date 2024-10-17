(ns your-namespace
  (:require [clojure.java.io :as io]               ; Подключение библиотеки для работы с файловой системой
            [clojure.core.async :as async :refer [go <! >! chan close!]]))  ; Подключение библиотеки для работы с асинхронными потоками

(defn scan [path result-chan]
  (if (.isDirectory (io/file path))  ; Если это папка

    (doseq [sub (.list (io/file path))]   
      (let [sub-path (str path "/" sub)]
        (async/go
          (scan sub-path result-chan))))   ; Рекурсивный запуск сканирования для каждого подкаталога

    (let [content (slurp path)]   ; Если это файл, считываем его содержимое
      (when (.contains content "hello")   ; ищем hello
        (async/>! result-chan path)))))   ; Отправляем путь в канал результата

(defn parallel-scan [path]
  (let [result-chan (async/chan)]   ; Создание канала для результатов
    (async/go
      (scan path result-chan))   ; Запуск сканирования в заданной директории
    result-chan))

(defn print-paths [result-chan]
  (async/go
    (loop []
      (when-let [path (<! result-chan)]   ; Получаем пути из канала результатов
        (println path)   ; Вывод пути к фалу
        (recur)))))   ; 

(defn -main []
  (let [result-chan (parallel-scan "test")]   
    (print-paths result-chan)))   ; Выводим найденные пути

(-main)   ; Запускаем функцию -main при запуске программы
