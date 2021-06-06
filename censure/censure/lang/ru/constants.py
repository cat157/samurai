# -*- coding: utf-8 -*-
from __future__ import unicode_literals


EXCLUDES_DATA = {
    'а': [
        'автомоб',
        'амеб',
        'амудар',
        'ансамбл',
        'ансибл',
        'архиманд',
        'аспид',
        'атрибут',
        'ахнет',
        'ахнул',
        'ахтуб'
    ],
    'б': [
        '(бал?)',
        '(бу?)(бу?)+',
        'бебел',
        'бедр',
        'белибер',
        'бермуд',
        'блюхер',
        'блямб',
        'бляпан[н]?',
        'бляронс',
        'блях[аеиу]?$',
        'бляха[йю]',
        'бляхо(?!([мпс]))',
        'бляше',
        'бляшк',
        'богохул',
        'боскреб',
        'бронеб',
        'быстро'
    ],
    'в': [
        'вдребез',
        'веб',
        'веб.?об',
        'вебер',
        'вебсер',
        'вебстер',
        'верх',
        'вздох',
        'влюбля',
        'волшеб',
        'востреб',
        'враждеб',
        'врачеб',
        'вроде',
        'все.?$',
        'все?т[ао]',
        'встрепан',
        'всуху',
        'втиху',
        'выгреб',
        'вытрях',
        'выхлеб'
    ],
    'г': [
        'где.+нибу',
        'гербарий',
        'гибел',
        'гидро[кт]',
        'глеб',
        'голов',
        'гомеоп',
        'горох',
        'граб',
        'греб[еклноушя]',
        'гриб'
    ],
    'д': [
        'две',
        'деб[еи]л',
        'деба[г|ж]',
        'дебаркад',
        'дебет',
        'дебош',
        'дезокси',
        'дерябну',
        'дирижаб',
        'дох[л|н]',
        'дребед',
        'дротик',
        'дрыхн',
        'дубля'
    ],
    'е': [
        'евпатори',
        'еле-еле',
        'епан[н]?ч',
        'епарх'
    ],
    'ж': [
        'ж[е|и]реб',
        'жебы',
        'жили?',
        'жулеб'
    ],
    'з': [
        'за[дс]ох',
        'завихрен',
        'загиб',
        'заглубля',
        'загреб[ану]?',
        'задолбил',
        'заколеб',
        'закрепл',
        'замах',
        'зашиб',
        'зеб[ру]',
        'злоупотребля',
        'зяб'
    ],
    'и': [
        '(ипат$)|(ипат((и)|(у)|(о)))',
        'избал',
        'изгиб',
        'икебан',
        'имбеци',
        'иметь',
        'инкассат',
        'испан',
        'испар',
        'истреб',
        'исчерп',
        'их$'
    ],
    'к': [
        'кабел',
        'как..-[лн]и[бк]',
        'как..-т[ао]',
        'кан[н]?[еи]бал',
        'кипуч',
        'клебанов',
        'клеп',
        'кобел',
        'ков((ре)|(ер))',
        'коктебе',
        'колеб',
        'констеб',
        'корабля',
        'кракозяб',
        'крик',
        'куй$',
        'купидон',
        'кухн'
    ],
    'л': [
        'ламборд',
        'лапидар',
        'либер',
        'липидо',
        'липуч',
        'лихую'
    ],
    'м': [
        '^мандел((а)|(ой))$',
        'м-да',
        'м[ао]хер',
        'мандари',
        'мандат(?!(в))',
        'мандоли',
        'мебел',
        'муданьцзян',
        'мудехары',
        'мыши'
    ],
    'н': [
        'нагреб',
        'наибол',
        'наибыс',
        'наколеб',
        'напереб',
        'нахмурил',
        'наябед',
        'неблаг',
        'небы',
        'неплох',
        'нет$',
        'нибу[дт]',
        'новосиб',
        'нотебук',
        'ноябр'
    ],
    'о': [
        'обд[и|е]р',
        'обляпа[лн]',
        'обсох',
        'обтяг',
        'оглобл',
        'одномандат',
        'озлобля',
        'октябр',
        'опозд',
        'оскорбл',
        'ослабл',
        'отдохн',
        'отребье',
        'отсебя',
        'отскреб',
        'отхлеб',
        'отчебуч',
        'охи((вз)|(ах))',
        'охудеп',  # oxygen
        'ошиб'
    ],
    'п': [
        'п[р]?одебош',
        'парикмахер',
        'пасиб',
        'пассат',
        'пахн[еу]',
        'пахуч',
        'педагог',
        'педал',
        'педант',
        'педераст',
        'педолог',
        'педофил',
        'педро$',
        'переб[еиор]',
        'перебло',
        'перемудр',
        'перепал',
        'пидопригор',
        'пистол',
        'пихнул',
        'пищеблок',
        'плебисц',
        'плебс',
        'плох[ио]',
        'плят(!(ь))',
        'поб[ае]р',
        'побабь',
        'побыст',
        'погиб',
        'погреб',
        'подгреб',
        'подох',
        'подсобля',
        'поколеб',
        'поперх',
        'попух',
        'потре[бп]',
        'похи[тщ]',
        'похлеб',
        'поху[дж]',
        'пошле',
        'пр[еи]б[аы]в',
        'пребел',
        'пребол',
        'препин',
        'приб[иы][лт]',
        'прибаут',
        'прибе',
        'прибли[жз]',
        'прибо[ейря]',
        'прибра',
        'припизднюват',
        'приспособля',
        'прозяб',
        'протреп',
        'протух',
        'прохуд',
        'прошиб',
        'пятибал'
    ],
    'р': [
        'равнобедр',
        'разгиб',
        'разгреб',
        'раздроблят',
        'рас[с]?лабля',
        'растреп',
        'расхлеб',
        'расшиб',
        'ребе$',
        'ребен',
        'ребер',
        'ребло',
        'ребр',
        'ребу[ст]',
        'ребя',
        'ренессанс',
        'репин',
        'рибосом',
        'розет',
        'рубля',
        'рябина'
    ],
    'с': [
        '(сабля$)|(сабля(!(к)))|(сабл[ие])',
        '(спид[а]?$)|(спидо)',
        'салат',
        'сбербан',
        'свадеб',
        'свирепст',
        'сгреб',
        'себ',
        'сентябр',
        'сердце',
        'серебр',
        'сиб',
        'скипидар',
        'скобля',
        'скопид',
        'скреб',
        'скрипуч',
        'служеб',
        'смахи',
        'соскобля',
        'спасиб',
        'ссутул',
        'стеб',
        'стебл[ея]',
        'степа',
        'стибрит',
        'стриптизбар',
        'судеб',
        'сукачев',
        'сшиб'
    ],
    'т': [
        'талмуд',
        'твоя$',
        'телепат',
        'тереб',
        'тибер',
        'типун',
        'торпед',
        'треб((у)|(ов))',
        'треба$',
        'трепа((нг)|([лт]))',
        'трибун'
    ],
    'у': [
        '^уед',
        '^уеха',
        'убил',
        'углуб',
        'уже',
        'уподоб',
        'упорхн',
        'употреб',
        'усугуб',
        'ух[ао]йд[ао]к',
        'учеб'
    ],
    'ф': [
        'фидо(?!(ра))',
        'фламанд',
        'фон'
    ],
    'х': [
        'хайдфил',
        'херберт',
        'херес',
        'херомант',
        'херсон',
        'херувим',
        'хлеб',
        'хли[вф]кие',
        'хмур',
        'хотябы',
        'хреб[ет]',
        'хреновый',
        'хубер',
        'худе[лт]',
        'худо',
        'худющ',
        'худяк',
        'хуже',
        'хуизху',
        'хули[ло]',
        'хулиган',
        'хулит(?!(ол))',
        'хунвеэбин'
    ],
    'ц': [
        'целебн',
        'церебрал'
    ],
    'ч': [
        'чебок', 'чебур'
    ],
    'ш': [
        'шебурш',
        'шиб',
        'шле',
        'штуч',
        'шумахер'
    ],
    'щ': [
        'щебе[нт]',
        'щедрот',
        'щелбан'
    ],
    'э': [
        'эберт',
        'эби.?нур',
        'эбнер',
        'эбонит',
        'экебан',
        'эпистал',
        'эреб'
    ],
    'ю': [
        'ютитс'
    ],
    'я': [
        'ябло[кнч]',
        'ястреб'
    ]
}


EXCLUDES_CORE = {
    'боле': 'боле',
    'гре#1': '^.{0,3}греб$',
    'гре#2': '^.{0,3}греб[аеклноушя]',
    'команд': 'команд',
    'мандат': 'мандат(?!(в))',
    'неб': 'неб[еиоу]',
    'пасиб': 'пасиб',
    'псих': 'психу',
    'страх': (
        '(страху(?!([еи])))|(^((за)|(пере)|(под))страхуя$)|(^((за)|(пере)|(под))'
        'страхуй((те(с.)?)|(ся))?$)|(^((за)|(пере)|(под))страхуем(ся)?$)'
    ),
    'теб': '[с|т][е|и]б^([оу][кш])+',
    'хлеб': '^.{0,3}хлеб',
    'хули': 'хулиган(?!(х))',
    'шлеп': 'шлеп',
    'штрих': 'штриху'
}

FOUL_CORE = {
    'бзд': 'бзд',
    'бля':
        '(б[еи]?л[у]?я)|(бля)|(блиад)|(бл[еи]д[иу])|([кю]ляд)|([бп][и]?л[ая][дт]ь$)|(билат.?$)|'
        '(блдс)',
    'гондон': '(уао)*г[ао]нд[ао][енш]',
    'долб':
        '(д[ао]лб[ао]дя)|(д[ао]л[бп][ао]манд)|(д[ао](д[ао])?лб[ао]л[еия]х)|(((д[ао])|'
        '(об))д[ао]лб[ао]н)',
    'дроч': '(др[ою][ктч])|(драчис)',
    'еб#1':
        '(^е[бп][а]?$)|([еиэ][б][аеиу][лнктрщчм])|(е.?[бп][аы][лнрт])|([еи][б]авш)|(еб[ст]ел)|'
        '(^ебят)',
    'еб#2':
        '(ебну)|([еи][б][ыу]р)|(е[б][лносуц])|(е.?[бп][аы]мат)',
    'еб#3': '(в.?[ея]б+)|(.а[ъь]?[еия][б])|([еия][б]в)|(п[ао]д[ьъ][е]б)|(^ебя$)|(27[\d]*.?.?ба)',
    'еб#4':
        '(йо[б])|(епин)|(епст)|([еи][п]у[нч])|(((твою)|(тебя))еб)|(ибиом)|(^ебт.$)|(вы[ея]вы)'
        '|((вы)?йаб)',
    'жоп': '(ж[ео]п)',
    'залуп': 'залуп',
    'лядс': 'лядс',
    'муда': '(м[\у]д[аеиоюыянл\#])|(.удозв)|(мудвин)|(мудчи)|(м[у]драк)|(\#удак)',
    'падл': '(падл[аоыю])|(пипид)',
    'перд':
        '([^су]перн((у)|(ет)))|(выпер[дж])|(пердан)|(^перд$)|(перд[ея][жлнт])|'
        '(перд[ия][млтщ])|(пердн[еу])|(перд((ли)|(ол)|(у)))|(перд[ью])|(пердо$)|'
        '([^су]п[еи]рну)',
    'пидар':
        '([бп][\#еиы]?д[аеио]?р)|(п[еия]д[ао]г)|(педик)|(пидеатр)|([гф][еи]д[ео]рас)|'
        '(пудура)|(п[еи]т[ае]рас)',
    'пизд#1': '(п[ийы]?[с]?[жзс][дж])|(п[еия][зс]?[ьъ]?д[ао])|'
              '(пист[ае])|(пи[тд]за)|(пизта)|(п[еи][зс]д)|(кизд)|(капец)|(звезди)|(физд[еи])',
    'пизд#2': '(п[\w]?[сз]д[ао][бт])|(пивд)|(пиз((ад)|(оп)))|(пита$)|(бл[ею]зд)|(ф[л]?[ею]зд)|'
              '(пиз[еу][днц])|(приздроп)|(з14[\d]*.?.?[з]?д[аеы])|(п[еи]рзд)',
    'сать':
        '(^сс?ать)|(ссат)|(^ссу$)|(ссут)|(^ссы$)|(^сс?ыку)|(^ссыте?$)|(^ссыш)|(ссан)|(((обо)|'
        '(пере)|(недо))сс?а[лт])',
    'сран':
        '(сран[н]?[адекоыь])|(сра[лч]ь?)|(срать)|(срет.?(ся)?$)|(^сри$)|(^сру$)|(срун)|(срут)|'
        '(^срю$)|(((об)|(под))сер[еи]в)|(сраст)|(сраты)',
    'хуй#1':
        '(х.?у[^дя]?[еийыюя])|(х[\#]+)$|(^[мх][\-у][\-у]?[еийыюя])|(х[у][у]?л[еиья])|(^аху$)'
        '|(ахай)',
    'хуй#2': '(^аху$)|(ахай)|(х[о]й[дл])|(куй)|([хм][у]йня)|(хн[еюя])|(ху[еюя])|(^[х]+у[еийыюя])',
    'член': 'члено((вид)|(воз)|(вре)|(гл)|(мет)|(ног)|(прием)|(сос)|(под)|(плет)|(рыл)|(грыз))',
    'япуч': 'яп[п]?уч'
}


FOUL_DATA = {
    'а': [
        '^абанамат',
        '^анахну',
        '^архипиздрит',
        '^аст[ао]еб',
        '^аст[ао]п[еи]зд',
        '^аст[ао]хер',
        '^ат[ъь]?[ея]б',
        '^атасас'
    ],
    'б': [
        '^б[еи]л[еи]ат',
        '^бабоеб',
        '^басран',
        '^баться',
        '^бзд',
        '^бзжу',
        '^бл[ьъ]?я',
        '^блев[ао]',
        '^блежник',
        '^блюдов',
        '^блюзд'
    ],
    'в': [
        '^вафл?е?ё?л',
        '^вафлезл[ао]',
        '^великодрюч',
        '^вз[ъь]еб',
        '^взбзд',
        '^висл[ао]хеу',
        '^влагопр[ао]',
        '^влагопр[о]?еб',
        '^восьмипроеб',
        '^вп[еи]рдол',
        '^впендюр',
        '^врот.?[еи][б]',
        '^вротзапил',
        '^вротскреб',
        '^выбл[еию]',
        '^выдрюч',
        '^выеть',
        '^выешкив',
        '^выйобыв',
        '^вып[еи]здр',
        '^выпенд[ю]?р',
        '^выподв',
        '^высерусь',
        '^высира',
        '^высра',
        '^высса',
        '^выссу'
    ],
    'г': [
        '^г[ао][вм]н',
        '^гвоздедроч',
        '^гноильн',
        '^говен',
        '^говешка',
        '^гомик',
        '^гомино',
        '^гомосек[\w]{0,2}$',
        '^гонолуп',
        '^греб[ао]н',
        '^гребзд',
        '^гнид[аоы]?'
    ],
    'д': [
        '^долбо',
        '^д[ао](д[ао])?лб[ао]л[еия]х',
        '^д[ао][ея]б',
        '^д[ао]д[ао]лб[ао]н',
        '^д[ао]л[бп][ао]манд',
        '^д[ао]лб[ао]дя',
        '^д[ао]лбое',
        '^д[ао]пи[зж]',
        '^д[еи]б[еи]дозуб',
        '^д[еи]бил',
        '^данунах',
        '^двужоп',
        '^дермо',
        '^дерьм',
        '^длиннохер',
        '^додр[ою]ч',
        '^домохнот',
        '^дрисн',
        '^дрисс',
        '^дрист',
        '^дрищ',
        '^дроч[ук]',
        '^дрочан',
        '^дрочена',
        '^дрочи[лтш]',
        '^дрочк',
        '^дыдл',
        '^д[ао]ркн[эе]т'
    ],
    'е': [
        '^(?<!(им))еть',
        '^е[бп][с]?тит',
        '^е[бп]аши',
        '^е[бп]е[нмтц]',
        '^е[бп]ки',
        '^е[бп]т[ивы]',
        '^е[бп]твою',
        '^еби(?!(зне))',
        '^ебла',
        '^едрит',
        '^ездец',
        '^елб',
        '^елд',
        '^еп[е]?рн',
        '^епрст$',
        '^епт[аю]$',
        '^ептать$',
        '^ет',
        '^ехнут'
    ],
    'ж': ['^жмуд'],
    'з': [
        '^з[ао]луп',
        '^заблева',
        '^зав[ао]фл',
        '^задрач',
        '^заговнять',
        '^задристать',
        '^задышк',
        '^заелдон',
        '^заеп[п]?ен',
        '^заеть',
        '^зажоп',
        '^заман((ал)|(дюк))',
        '^замуда',
        '^замудоха',
        '^занафуяч',
        '^заныка[лт]',
        '^зап[еи]ж',
        '^зап[еи]ндюр',
        '^зап[еи]рдун',
        '^запипи',
        '^записьк',
        '^заподл',
        '^запроеб',
        '^зас[с]?ыха$',
        '^засер',
        '^засир',
        '^засобачи[лт]',
        '^засса',
        '^застебан',
        '^заторчал',
        '^захера',
        '^защекан',
        '^зв[еи]здобол',
        '^зв[еи]здун',
        '^звизд',
        '^здец',
        '^зл[ао][бп][ао]е[бп]',
        '^зл[ао][яе]б',
        '^злоп[ао]х'
    ],
    'и': [
        '^и.?[бп]а[лнрт]',
        '^и.?[бп]аши',
        '^и.?[бп]е[нмтц]',
        '^изговн',
        '^ибонех',
        '^издец',
        '^ипа[ц]+[ао]',
        '^итит([ъь]?)|(!(с))',
        '^их[еи]бут'
    ],
    'й': ['^йобан'],
    'к': [
        '^к[ао]бзд',
        '^к[ао]зл[ао]еб',
        '^к[ао]лд[ао]еб',
        '^к[ао]лдыр',
        '^к[ао]н[ао]еб',
        '^к[еи]рд[еы][кц]',
        '^кабзд',
        '^калоед',
        '^квазиуеб',
        '^кебени',
        '^кизди[тш]',
        '^кисец',
        '^кляпыжит',
        '^коз.бл',
        '^косозалуп',
        '^коца[нт]',
        '^кр[ао]к[ао]еб',
        '^красн[ао]жоп',
        '^крендец',
        '^куякнул',
        '^курв[ао]?',
        '^к[оа]т[ао][кг]'
    ],
    'л': [
        '^лжеб',
        '^лихолох',
        '^лярв'
    ],
    'м': [
        '^м[ао]л[ао]ф',
        '^м[ао]нд[ао][в]',
        '^м[ао]ндатня',
        '^м[ао]нде[йрт]',
        '^м[ао]шонк[ао][ао]?б',
        '^ма[вз][аео].?фак',
        '^манд[а]$',
        '^манд[уыю]',
        '^мандакрыл',
        '^мандар[ао]еб',
        '^манди[лтщ]?(?!(р))',
        '^матоеб',
        '^матозад',
        '^мдак',
        '^междужоп',
        '^мин[ъь]?ет',
        '^мндр[оу]',
        '^мобсел',
        '^мозгоеб',
        '^мозгопроеб',
        '^мокрощ[еи]лк',
        '^моноп[еи]н[еи]с',
        '^мохно((нед)|(муд))',
        '^мундел',
        '^муячеч',
        '^мля',
        '^мр[ао]з'
    ],
    'н': [
        '^на[ц]уй',
        '^набзде[лт]',
        '^наговня',
        '^надр[иы]с',
        '^надр[ою]ч',
        '^надрямс',
        '^назалуп',
        '^намандаш',
        '^напизд',
        '^насал',
        '^насса',
        '^насца',
        '^нах$',
        '^нах[пу]',
        '^нахеза',
        '^н[иеа]х[еи]р',
        '^нахр[еи]н',
        '^н[иеа][кх]у[ая]$',
        '^нед[ао][ея]б',
        '^нед[ао]пи[зж]',
        '^неуе[б]+',
        '^нечленосос',
        '^ниип[ае]'
    ],
    'о': [
        '^обдриста',
        '^обл[еи]м[ао]нд',
        '^обл[еи]муд',
        '^обосца',
        '^обсир',
        '^обспускан',
        '^обуевш',
        '^огрохув',
        '^окуел',
        '^опр[ао]муд',
        '^опрст$',
        '^ост[ао]хер',
        '^отдрюч',
        '^отмудоха',
        '^отпиз',
        '^отсоси$',
        '^отчермуто',
        '^отъеть',
        '^офоршмачи',
        '^офуен[н]?',
        '^ох[еу]жоп',
        '^ох[еу]ндрот',
        '^ох[еу]р',
        '^охулк',
        '^охумев',
        '^ошмудок',
        '^очкун'
    ],
    'п': [
        '^п[ао]бл[еи]ден',
        '^п[ао]бл[ия]душ',
        '^п[еи][сз]ж',
        '^педри[лк]',
        '^пендюр',
        '^пер[е]?колд',
        '^пердлов',
        '^пере[е]?б[ал]',
        '^пере[е]?б[алд]',
        '^перевзб',
        '^передрен',
        '^перекосоеб',
        '^перемат',
        '^перемуд',
        '^перепизну',
        '^пересуч',
        '^перетит',
        '^перехер',
        '^пернет',
        '^перну[влт]',
        '^пи[пс]ис',
        '^пиндос',
        '^пипе[т]?ц',
        '^писк.$',
        '^пист(([ъью])|(?!(он)))',
        '^питишка$',
        '^плеха$',
        '^плыва$',
        '^под[ъь]еб',
        '^подвзб',
        '^подговн',
        '^подзабор',
        '^подзл[ао]еб',
        '^подлоеб',
        '^подре[й]?туз',
        '^подроч[иу]',
        '^подстр[ао]хер',
        '^поеть',
        '^полуеб',
        '^полужоп',
        '^попоеб',
        '^поср[ае]т',
        '^посру',
        '^посс[ауы]',
        '^пох[ъь]е',
        '^похер',
        '^похух',
        '^поц[ау]?$',
        '^поцоват',
        '^пр[ао]п[еиу]рд((ы)|([ао]м[ао]нд[ао]))',
        '^пр[ао]с[с]?уч',
        '^пр[ао]х.блу',
        '^пр[ао]х[ао]еб',
        '^пр[ао]шм[ао]нд',
        '^пр[еи]здун',
        '^пр[еиу]м[ао]нд[ао]',
        '^приебо',
        '^прилабун',
        '^припизд',
        '^прозалуп',
        '^произ[ъь]?еб',
        '^пром[ао]нд',
        '^промуд',
        '^пропизд',
        '^пучезад',
        '^п[ао]д[ао]н[ок][ик]',
        '^п[ао]скуд',
        '^пись?к[аио]?',
        '^п[еи]сюн',
        '^п[ао]с[ао]си?',
        '^п[ао]т[ао]ску[хш]',
        '^пр?[ао]ср[еи]',
        '^п[еи]тух[ао]'
    ],
    'р': [
        '^р[ао][зс][ъь]?е[бпт]',
        '^р[ау][зс]туд[иы]т',
        '^ра[зс][с]?теб',
        '^ра[зс]долба[еий]',
        '^ра[зс]долбое',
        '^ра[зс]дрю',
        '^ра[зс]пидз',
        '^ра[зс]проеб',
        '^ра[зс]проет',
        '^ра[зс]пронаедр',
        '^ра[зс]простоеб',
        '^ра[зс]тр[еи]кв',
        '^ра[зс]тыка',
        '^ра[зс]членх',
        '^расп[ао]хаб',
        '^распроторазд',
        '^рах[ъь]?ед'
    ],
    'с': [
        '^[с]?суч((ий)|(ка))',
        '^[с]?суч[к]?ар',
        '^[с]?суче((х)|(нок))',
        '^с[ъь]еб',
        '^сака',
        '^самоеб',
        '^сахер',
        '^свином[ао]нд',
        '^сговня',
        '^секел',
        '^семироеб',
        '^серепер',
        '^серун',
        '^серька',
        '^сест[\w]?[ао]еб',
        '^сика',
        '^сикат',
        '^сикел',
        '^сипов',
        '^сирать',
        '^сирывать',
        '^ском[м]?унизд',
        '^скурви',
        '^скурех',
        '^скурея',
        '^скуряг',
        '^скуряж',
        '^с[ао]си',
        '^сосомол',
        '^состать$',
        '^спермот[ао]в[ао]з',
        '^спиж',
        '^спизд',
        '^срак$',
        '^срак[ауо]',
        '^сруль',
        '^ссака',
        '^ссаки',
        '^ссан[н]?о',
        '^струк$',
        '^суперзаеб',
        '^сухобзд',
        '^суходроч',
        '^сц[аиы]к[аиу]',
        '^сцавинье',
        '^сцание',
        '^сцать',
        '^сциха',
        '^сцуль',
        '^сцыха',
        '^сыкун',
        '^с[сц]?у[кч][ьък]?[еаои]',
        '^сре[шщ]ь?'
    ],
    'т': [
        '^тарачлен',
        '^твоюмат',
        '^трандец$',
        '^триквант',
        '^трим[ао]н[ао]?д',
        '^тринитроеб',
        '^трипиз[ао][бп]лд',
        '^трипробзд',
        '^трих[ао]м[ао]н[ао]?д',
        '^трах[ано][тну]',
        '^троедолбо',
        '^троедром',
        '^троедруч',
        '^трындоп[еи]нд',
        '^туебен',
        '^тварь?'
    ],
    'у': [
        '^ублюд',
        '^угреб[и]',
        '^угробищ',
        '^уеть',
        '^ум[аоу]дох',
        '^упизд',
        '^усса[лт]',
        '^уссыш',
        '^усцаться',
        '^у[шщ]л[её]п[ао]к'
    ],
    'ф': [
        '^фак\$',
        '^факин',
        '^факну',
        '^факошит',
        '^факуд',
        '^фидераст',
        '^фопа',
        '^фуй$',
        '^фуцк'
    ],
    'х': [
        '^х[еи]ров',
        '^хезать',
        '^хер',
        '^хера',
        '^хере',
        '^херн[еияю]',
        '^хером',
        '^хитрожоп',
        '^хитрозад',
        '^хлабал',
        '^хлюха',
        '^хуканут',
        '^хурл',
        '^хуров',
        '^хабибд?и'
    ],
    'ц': [
        '^ц[сц]?у[кч][ьък]?[аои]'
    ],
    'ч': [
        '^черебзд',
        '^чернож[ео]п',
        '^чикс.',
        '^членяр',
        '^чмо$',
        '^чмыр[еья]'
    ],
    'ш': [
        '^шваль',
        '^швинд',
        '^шизд[ао]х',
        '^шлюх'
    ],
    'э': [
        '^э[бп]а[лнрт]',
        '^э[бп]аши',
        '^э[бп]е[нмтц]',
        '^эб[илносуц]'
    ],
    'ю': [
        '^юхан',
    ],
    'я': [
        '^я.?[бп]а[лнрт]',
        '^я.?[бп]аши',
        '^я.?[бп]е[нмтц]',
        '^я[бп]тв',
        '^яб[илносуц]',
        '^ялд[аоу]',
        '^япу'
    ]
}


BAD_SEMI_PHRASES = (
    'анепош[е]?л[и]?бы[вт]ы',
    'еханыйбабай',
    'идинахуй',
    'имел[аи]?тебя(?!(ввид))',
    'отс[ао]сатьу',
    'отс[ао]сичлен',
    'редк..педальност',
    'сучийпотрох',
    'тебяимел[аи]?(?!(ввид))',
    'тык[ао]зел',
)

BAD_PHRASES = ()

TRANS_TAB = dict((ord(a), b) for a, b in zip(
    'gcxyaeopkhbtmnu 036 ёdiz',
    'дсхуаеоркнвтмпи озб едиз'
))
