(set 'x '(40 112 114 105 110 116 108 110 32 34 40 115 101 116 32 39 120 32 39 34 32 120 32 
 34 41 34 41 10 40 112 114 105 110 116 108 110 32 40 106 111 105 110 32 40 109 97 
 112 32 99 104 97 114 32 120 41 32 34 34 41 41 10 40 101 120 105 116 41))
(println "(set 'x '" x ")")
(println (join (map char x) ""))
(exit)



;generator

(set 'src "(println \"(set 'x '\" x \")\")\n(println (join (map char x) \"\"))\n(exit)")
(println (map char (explode src)))
(exit)
