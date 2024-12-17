## Задачи по теме "Тестирование"
В репозитории находятся условия и код решённых задач.

### Плот / 01_Raft

|Параметр|Значение|
|:--|:--|
|Ограничение времени|1 секунда|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты (x1, y1), северо-восточный угол – координаты (x2, y2).
Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно плыть, чтобы как можно скорее добраться до плота.

### Майки и носки / 02_Tshirts_and_socks

|Параметр|Значение|
|:--|:--|
|Ограничение времени|1 секунда|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Как известно, осенью и зимой светает поздно, и так хочется утром ещё хоть немного поспать, а не идти в школу! Некоторые школьники готовы даже одеваться, не открывая глаз, лишь бы отложить момент пробуждения. Вот и Саша решил, что майку и носки он вполне может вытащить из шкафа на ощупь с закрытыми глазами и только потом включить свет и одеться. В шкафу у Саши есть два ящика. В одном из них лежит A синих и B красных маек, в другом — C синих и D красных пар носков. Саша хочет, чтобы и майка, и носки были одного цвета. Он вслепую вытаскивает M маек и N пар носков. В первое же утро Саша задумался, какое минимальное суммарное количество предметов одежды (M+N) он должен вытащить, чтобы среди них гарантированно оказались майка и носки одного цвета. Какого именно цвета окажутся предметы одежды, для Саши совершенно неважно.

### Надпись на табло / 03_Scoreboard

|Параметр|Значение|
|:--|:--|
|Ограничение времени|1 секунда|
|Ограничение памяти|256Mb|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|

Вы получили доступ к одной из камер наблюдения в особо секретной огранизации. В зоне видимости камеры находится табло, с которого вы постоянно считываете информацию. Теперь вам нужно написать программу, которая по состоянию табло определяет, какая буква изображена на нём в данный момент. Табло представляет из себя квадратную таблицу, разбитую на n×n равных квадратных светодиодов. Каждый диод либо включён, либо выключен. Введём систему координат, направив ось OX вправо, а ось OY — вверх, приняв сторону диода равной 1.

На табло могут быть изображены только следующие буквы:

- I — прямоугольник из горящих диодов.
- O — прямоугольник из горящих диодов с углами (x1,y1) и (x2,y2), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x3,y3) и (x4,y4). При этом границы выключенного прямоугольника не должны касаться внешнего, то есть x1<x3<x4<x2 и y1<y3<y4<y2.
- C — прямоугольник из горящих диодов с углами (x1,y1) и (x2,y2), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x3,y3) и (x4,y4). При этом правая граница выключенного прямоугольника находится на правой границе внешнего прямоугольника, то есть x1<x3<x4=x2​  и y1<y3<y4<y2.
- L — прямоугольник из горящих диодов с углами (x1,y1) и (x2,y2), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x3,y3) и (x4,y4). При этом правые верхние углы выключенного прямоугольника и внешнего прямоугольника совпадают, то есть x1<x3<x4=x2 и y1<y3<y4=y2.
- H — прямоугольник из горящих диодов с углами (x1,y1) и (x2,y2), внутри которого находятся 2 прямоугольника из выключенных диодов с координатами углов (x3,y3), (x4,y4) у первого и (x5,y5), (x6,y6) у второго. При этом выключенные прямоугольники должны иметь одинаковую ширину, находиться строго один под другим, один прямоугольник должен касаться верхней стороны, а другой прямоугольник должен касаться нижней стороны внешнего прямоугольника, то есть x1<x3=x5<x4=x6<x2 и y1=y3<y4<y5<y6=y2.
- P — прямоугольник из горящих диодов с углами (x1,y1) и (x2,y2), внутри которого находятся 2 прямоугольника из выключенных диодов с координатами углов (x3,y3), (x4,y4) у первого и (x5,y5), (x6,y6) у второго. При этом правый нижний угол первого выключенного прямоугольника должен совпадать с правым нижним углом внешнего прямоугольника, а другой выключенный прямоугольник должен находиться строго выше и не касаться границ других прямоугольников, также левые границы двух выключенных прямоугольников должны совпадать, то есть x1<x3=x5<x6<x4=x2 и y1=y3<y4<y5<y6<y2.
- Любое другое состояние табло считается буквой X.

По виду табло определите, какая буква на нём изображена.


### Кондиционер / 04_Conditioner
На соревновании участникам была предложена следующая задача:

——

В офисе, где работает программист Петр, установили кондиционер нового типа. Этот кондиционер отличается особой простотой в управлении. У кондиционера есть всего лишь два управляемых параметра: желаемая температура и режим работы.

Кондиционер может работать в следующих четырех режимах:

«freeze» — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и так не больше желаемой, то он выключается.

«heat» — нагрев. В этом режиме кондиционер может только увеличивать температуру. Если температура в комнате и так не меньше желаемой, то он выключается.

«auto» — автоматический режим. В этом режиме кондиционер может как увеличивать, так и уменьшать температуру в комнате до желаемой.

«fan» — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха и не изменяет температуру в комнате.

Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы он за час доводит температуру в комнате до желаемой.

Требуется написать программу, которая по заданной температуре в комнате troom, установленным на кондиционере желаемой температуре tcond и режиму работы определяет температуру, которая установится в комнате через час.

——

Вам предстоит разработать набор тестов (только входных данных) для этой задачи, тщательно проверяющий решения участников.

### Наибольшее произведение двух чисел / 05_Max_product
На соревновании участникам была предложена следующая задача:

——

Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально. Выведите эти числа в порядке неубывания.

Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

Решение должно иметь сложность O(n), где n - размер списка.

——

Вам предстоит разработать набор тестов (только входных данных) для этой задачи, тщательно проверяющий решения участников.

Формат вывода
Сдавать следует не программу, а текстовый файл.
В первой строке файла запишите число N (1<=N<=20) — количество тестов, которые вы разработали.
В следующих N строках запишите по одному тесту. Каждый тест должен состоять из одной строки, в которой записано число K (2≤K≤10) — количество чисел в последовательности, а затем K чисел ai​  (−100≤ai≤100).