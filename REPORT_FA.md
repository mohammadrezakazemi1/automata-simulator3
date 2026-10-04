# گزارش کار پروژه شبیه‌ساز زبان‌ها و ماشین‌ها

## 1. معرفی پروژه

این پروژه یک نرم‌افزار دسکتاپ آموزشی برای درس نظریه زبان‌ها و ماشین‌ها است که با Python و PySide6 پیاده‌سازی شده است.

هدف پروژه تبدیل مفاهیم نظری درس به یک محیط گرافیکی، تعاملی و قابل آزمایش است.

دو آزمایشگاه اصلی برنامه عبارت‌اند از:

- Automata Lab: طراحی، شبیه‌سازی و تبدیل DFA و NFA
- Grammar Lab: ویرایش گرامر، آزمایش رشته، Parse Tree و Derivation

ساختار اصلی پروژه:

- main.py: رابط گرافیکی و کنترل تعامل کاربر
- automata.py: مدل و الگوریتم‌های ماشین متناهی
- grammar.py: مدل گرامر و الگوریتم Parsing
- tests/: تست‌های خودکار

---

# بخش اول: آزمایشگاه گرامر

## 2. گرامر مستقل از متن چیست؟

گرامر مستقل از متن یا CFG روشی رسمی برای تعریف ساختار رشته‌های یک زبان است.

یک CFG با چهار جزء زیر بیان می‌شود:

    G = (V, Σ, P, S)

V مجموعه Nonterminalها، Σ مجموعه Terminalها، P مجموعه Productionها و S نماد شروع است.

مثال:

    S -> a A
    A -> b A | ε

در این مثال S و A غیرپایانه و a و b پایانه هستند.

## 3. ویرایشگر گرامر

کاربر می‌تواند قواعد را در Grammar Editor وارد یا ویرایش کند.

فرمت:

    Nonterminal -> production1 | production2

مثال:

    E -> E + T | T
    T -> T * F | F
    F -> ( E ) | id

علامت | برای چند Production جایگزین استفاده می‌شود.

برنامه متن را به Productionهای مستقل تبدیل می‌کند. هر Production شامل یک سمت چپ و دنباله‌ای از نمادهای سمت راست است.

Production تهی با ε مشخص می‌شود:

    A -> ε

در مدل داخلی، سمت راست چنین Productionی خالی در نظر گرفته می‌شود.

## 4. اعتبارسنجی گرامر

قبل از Parsing ساختار گرامر بررسی می‌شود؛ از جمله:

- خالی نبودن گرامر
- معتبر بودن نام Nonterminalها
- وجود نماد شروع
- معتبر بودن Productionها
- بررسی Nonterminalهای غیرقابل دسترس
- صحیح بودن Production تهی

## 5. رشته ورودی

کاربر یک رشته ورودی وارد می‌کند. برنامه آن را بر اساس نمادهای گرامر Tokenize کرده و به Parser می‌دهد.

روند:

    Grammar
       ↓
    Input String
       ↓
    Parser
       ↓
    Accepted / Rejected
       ↓
    Parse Tree + Derivation

## 6. الگوریتم Parsing

هسته Parsing از یک ساختار Earley-style Chart Parsing استفاده می‌کند.

هر وضعیت اطلاعات Production، محل نقطه پردازش و موقعیت شروع را نگه می‌دارد.

سه مفهوم اصلی:

### Prediction
وقتی نماد بعدی Nonterminal باشد، Productionهای مربوط به آن وارد Chart می‌شوند.

### Scanning
وقتی نماد بعدی Terminal باشد، با ورودی مقایسه می‌شود و در صورت تطابق پردازش جلو می‌رود.

### Completion
وقتی یک Production کامل شد، نتیجه آن به Productionهایی که منتظر آن Nonterminal بوده‌اند منتقل می‌شود.

اگر Production مربوط به نماد شروع از ابتدای ورودی تا انتهای آن کامل شود، رشته پذیرفته می‌شود.

## 7. Parse Tree

در صورت پذیرش رشته، برنامه ساختار Parse Tree را بازسازی می‌کند.

مثال:

    S -> a A
    A -> b A | ε

برای رشته abb:

    S
    ├── a
    └── A
        ├── b
        └── A
            ├── b
            └── ε

## 8. Leftmost Derivation

برنامه اشتقاق چپ‌ترین را نیز نمایش می‌دهد.

مثال:

    S
    ⇒ aA
    ⇒ abA
    ⇒ abb

در هر مرحله اولین Nonterminal موجود در سمت چپ گسترش داده می‌شود.

## 9. وضعیت فعلی Grammar Lab

رابط فعلی Grammar عمداً ساده شده و شامل این موارد است:

- Grammar Editor
- Input String
- Parse Tree
- Derivation
- Analyze

در رابط فعلی این موارد وجود ندارند:

- LL(1) Table
- FIRST
- FOLLOW
- Left Recursion
- Left Factoring
- LL(1)

این موارد جزو قابلیت‌های فعال رابط فعلی نیستند، حتی اگر بخشی از منطق قدیمی آن‌ها در grammar.py باقی مانده باشد.

---

# بخش دوم: آزمایشگاه اتوماتا

## 10. ماشین متناهی

ماشین متناهی مدلی ریاضی برای تشخیص زبان‌ها با تعداد محدودی State است.

ماشین شامل Stateها، Alphabet، Transitionها، Start State و Final Stateهاست.

در برنامه این اطلاعات در کلاس FiniteAutomaton نگهداری می‌شوند.

هر Transition به صورت زیر مدل می‌شود:

    (source, symbol, target)

مثلاً:

    (q0, a, q1)

یعنی از q0 با دریافت a به q1 می‌رویم.

## 11. DFA چیست؟

DFA یا Deterministic Finite Automaton ماشینی است که برای هر State و Symbol حداکثر یک مقصد دارد.

مجاز:

    q0 --a--> q1

غیرمجاز:

    q0 --a--> q1
    q0 --a--> q2

زیرا برای q0 و a دو مقصد وجود دارد.

DFA همچنین ε-transition ندارد.

در برنامه is_deterministic این شرایط را بررسی می‌کند.

## 12. NFA چیست؟

NFA یا Non-deterministic Finite Automaton اجازه می‌دهد برای یک State و یک Symbol چند مقصد وجود داشته باشد.

مثال:

    q0 --a--> q0
    q0 --a--> q1

NFA می‌تواند ε-transition نیز داشته باشد؛ یعنی بدون مصرف Symbol ورودی از یک State به State دیگری برویم.

## 13. Construction Mode

در Designer دو Mode مستقل وجود دارد:

- DFA
- NFA

این Mode مشخص می‌کند کاربر در حال ساخت چه نوع ماشینی است.

در DFA چند مقصد برای یک Source و Symbol مجاز نیست و ε-transition نیز مجاز نیست.

در NFA چند مقصد و ε-transition امکان‌پذیر است.

نکته مهم: تغییر Mode به معنی تبدیل ماشین نیست. برنامه برای DFA و NFA فضای طراحی مستقل نگه می‌دارد.

## 14. طراحی گرافیکی

کاربر می‌تواند ماشین را بدون ورود متن و مستقیماً در Graph View طراحی کند.

امکانات اصلی:

- Add State
- Add Transition
- Start
- Final
- Delete State
- Delete Transition
- جابه‌جایی Stateها
- تغییر Mode بین DFA و NFA

Stateها به صورت Node و Transitionها به صورت Edge نمایش داده می‌شوند.

## 15. اجرای DFA

برای اجرای DFA، ماشین از Start State شروع می‌کند و ورودی را از چپ به راست می‌خواند.

برای هر Symbol:

1. Symbol خوانده می‌شود.
2. Transition یکتا پیدا می‌شود.
3. ماشین به State مقصد می‌رود.
4. این کار تا پایان ورودی ادامه دارد.

اگر State نهایی باشد رشته Accepted و در غیر این صورت Rejected است.

مثال:

    Input: 0101

    q0 --0--> q1
    q1 --1--> q2
    q2 --0--> q1
    q1 --1--> q2

## 16. اجرای NFA

در NFA ممکن است چند State هم‌زمان فعال باشند.

مثلاً:

    {q0}

با یک Symbol ممکن است تبدیل شود به:

    {q0,q1}

در مرحله بعد حرکت روی تمام Stateهای فعال محاسبه می‌شود.

در پایان اگر حداقل یکی از Stateهای فعال Final باشد، رشته Accepted است.

## 17. ε-Closure

ε-Closure یعنی تمام Stateهایی که از یک State می‌توان بدون مصرف Symbol ورودی و فقط با ε به آن‌ها رسید.

مثال:

    q0 --ε--> q1
    q1 --ε--> q2

پس:

    ε-closure(q0) = {q0,q1,q2}

در برنامه epsilon_closure با پیمایش گراف این مجموعه را محاسبه می‌کند.

---

# بخش سوم: تبدیل NFA به DFA

## 18. الگوریتم Subset Construction

مهم‌ترین الگوریتم پروژه تبدیل NFA یا ε-NFA به DFA است.

ایده اصلی:

> هر State در DFA نماینده یک مجموعه از Stateهای NFA است.

مثلاً یک State از DFA می‌تواند این باشد:

    {q0,q1}

یعنی ماشین DFA در واقع نماینده این است که در NFA هر دو q0 و q1 می‌توانند فعال باشند.

## 19. مرحله اول

ابتدا Start State ماشین NFA را می‌گیریم.

اگر Start برابر q0 باشد:

    {q0}

اگر ε-transition وجود داشته باشد، ابتدا ε-Closure گرفته می‌شود.

مثلاً:

    ε-closure(q0) = {q0,q1}

این مجموعه Start State در DFA می‌شود.

## 20. مرحله دوم: Move

برای هر Symbol از Alphabet، از تمام Stateهای مجموعه حرکت می‌کنیم.

مثلاً:

    Current = {q0,q1}
    Symbol = a

تمام Transitionهای a از q0 و q1 بررسی می‌شوند.

اگر نتیجه:

    {q0,q2}

باشد، یک State جدید در DFA ساخته می‌شود:

    {q0,q2}

پس:

    {q0,q1} --a--> {q0,q2}

## 21. تکرار الگوریتم

برای هر Subset جدید دوباره همین کار انجام می‌شود.

اگر مجموعه جدیدی به دست آمد، آن را به Stateهای DFA اضافه می‌کنیم و بعد آن را پردازش می‌کنیم.

این روند تا زمانی ادامه پیدا می‌کند که دیگر Subset جدیدی وجود نداشته باشد.

خلاصه:

    NFA
     ↓
    Start Set
     ↓
    Move برای هر Symbol
     ↓
    Subset جدید
     ↓
    پردازش Subset جدید
     ↓
    تکرار تا پایان
     ↓
    DFA

## 22. Final Stateهای DFA

اگر یک State از DFA حداقل یک State نهایی NFA را در خود داشته باشد، آن State در DFA نیز Final است.

مثلاً اگر q2 نهایی باشد:

    {q0,q2}

نیز Final خواهد بود.

## 23. Dead State

اگر برای یک Subset و یک Symbol هیچ مقصدی وجود نداشته باشد، نتیجه مجموعه تهی است:

    ∅

این مجموعه در پیاده‌سازی به عنوان Dead State نگه داشته می‌شود تا DFA برای Symbolهای Alphabet انتقال مشخص داشته باشد.

## 24. پیاده‌سازی در automata.py

متد to_dfa مسئول تبدیل است.

مراحل آن:

1. اعتبارسنجی ماشین
2. محاسبه Start Subset
3. ساخت نام برای Subsetها
4. قرار دادن Subset اولیه در Queue
5. پردازش هر Subset
6. محاسبه Move برای هر Symbol
7. محاسبه ε-Closure
8. ساخت Subset جدید در صورت نیاز
9. ایجاد Transition
10. تعیین Final Stateها
11. تکرار تا خالی شدن Queue
12. ساخت DFA جدید

برای جلوگیری از پردازش تکراری، Subsetهای قبلی با یک نگاشت ذخیره می‌شوند.

## 25. مثال ساده تبدیل

فرض کنیم NFA این Transitionها را داشته باشد:

    q0 --a--> q0
    q0 --a--> q1
    q1 --b--> q2

q0 شروع و q2 نهایی است.

در ابتدا:

    A = {q0}

با a:

    {q0} --a--> {q0,q1}

پس:

    B = {q0,q1}

از B با b:

    {q0,q1} --b--> {q2}

پس:

    C = {q2}

چون C شامل q2 است، C نهایی است.

این مثال نشان می‌دهد که Stateهای DFA در واقع Subsetهایی از Stateهای NFA هستند.

---

# بخش چهارم: صفحه Conversion

## 26. نحوه استفاده

صفحه Conversion مخصوص NFA → DFA است.

روند استفاده:

    Designer Mode = NFA
           ↓
    ساخت NFA
           ↓
    Conversion
           ↓
    Load Current Machine
           ↓
    Source: NFA
           ↓
    Convert NFA → DFA
           ↓
    Result: DFA

اگر ماشین فعلی DFA باشد، تبدیل فعال نمی‌شود؛ زیرا الگوریتم این صفحه برای NFA به عنوان Source طراحی شده است.

## 27. Snapshot ماشین ورودی

وقتی کاربر Load Current Machine را می‌زند، یک Clone از ماشین فعلی ساخته می‌شود.

به این ترتیب Conversion روی یک Snapshot مستقل اجرا می‌شود و تغییرات بعدی Designer روی ماشین ورودی الگوریتم اثر نمی‌گذارد.

با تغییر Mode بین DFA و NFA، Snapshot قبلی Conversion نیز پاک می‌شود تا ماشین قبلی اشتباهاً باقی نماند.

## 28. نمایش Source و Result

در صفحه Conversion دو Graph View وجود دارد:

- Source Graph
- Result Graph

برای NFA:

    Source: NFA

و پس از تبدیل:

    Result: DFA

گراف نتیجه به صورت خودکار Layout می‌شود و Stateهای DFA حاصل قابل جابه‌جایی هستند.

---

# بخش پنجم: شبیه‌سازی مرحله‌ای

## 29. Run، Step، Previous و Reset

برنامه چهار کنترل اصلی برای Simulation دارد:

- Run: اجرای خودکار رشته
- Step: اجرای یک مرحله
- Previous: برگشت یک مرحله
- Reset: شروع دوباره

مدت زمان اجرای مرحله‌ای نیز قابل تنظیم است و مقدار پیش‌فرض آن 2 ثانیه است.

در NFA وضعیت فعال ممکن است یک مجموعه باشد، مانند:

    {q0,q1} --b--> {q0,q2}

Transitionهای فعال نیز با سه جزء Source، Symbol و Target دنبال می‌شوند تا اگر چند Transition بین دو State وجود داشت، مسیر اشتباه نمایش داده نشود.

---

# بخش ششم: Transition Table

## 30. جدول انتقال

برای ماشین فعلی یک Transition Table نمایش داده می‌شود.

- هر سطر یک State است.
- هر ستون یک Symbol است.
- مقدار سلول مقصد Transition است.
- Start و Final بودن Stateها نیز مشخص می‌شود.
- اگر ε-transition وجود داشته باشد، ستون ε نیز اضافه می‌شود.

---

# بخش هفتم: اعتبارسنجی و معماری

## 31. اعتبارسنجی ماشین

قبل از اجرای الگوریتم‌ها، موارد زیر بررسی می‌شوند:

- وجود حداقل یک State
- معتبر بودن Start State
- معتبر بودن Final Stateها
- معتبر بودن Source و Target Transition
- معتبر بودن Symbolها
- یکتا بودن Transitionهای DFA

## 32. معماری فایل‌ها

    automata-simulator3/
    ├── main.py
    ├── automata.py
    ├── grammar.py
    ├── requirements.txt
    ├── tests/
    │   ├── test_automata.py
    │   ├── test_grammar.py
    │   └── test_gui.py
    ├── README.md
    ├── README_FA.md
    └── REPORT_FA.md

main.py رابط گرافیکی و کنترل برنامه را مدیریت می‌کند.

automata.py منطق ماشین متناهی را مستقل از GUI پیاده‌سازی می‌کند.

grammar.py مدل CFG و Parsing را پیاده‌سازی می‌کند.

## 33. تست‌های خودکار

برای اطمینان از صحت برنامه تست‌های خودکار نوشته شده‌اند.

موارد مهم شامل:

- DFA Acceptance
- NFA Acceptance
- ε-NFA
- NFA → DFA
- Dead State
- حذف Start State
- ورودی خالی
- Transition ناموجود
- ساخت GUI
- وجود Handlerهای Conversion
- مستقل بودن Modeهای DFA و NFA

تست GUI نیز با Qt در حالت offscreen قابل اجراست.

---

# بخش هشتم: جمع‌بندی الگوریتم‌ها

## اجرای DFA

    Start State
       ↓
    خواندن Symbol
       ↓
    Transition یکتا
       ↓
    State بعدی
       ↓
    پایان ورودی
       ↓
    Final؟
       ↓
    Accepted / Rejected

## اجرای NFA

    Start State
       ↓
    ε-Closure
       ↓
    Move روی Symbol
       ↓
    ε-Closure
       ↓
    مجموعه Stateهای فعال
       ↓
    تکرار
       ↓
    Final در مجموعه؟
       ↓
    Accepted / Rejected

## تبدیل NFA به DFA

    NFA
     ↓
    ε-Closure(Start)
     ↓
    یک Subset به عنوان State DFA
     ↓
    Move برای هر Symbol
     ↓
    ε-Closure
     ↓
    Subset جدید
     ↓
    تکرار
     ↓
    تعیین Final Subsetها
     ↓
    DFA

## Parsing گرامر

    Grammar
       ↓
    Productionها
       ↓
    Input String
       ↓
    Earley-style Chart
       ↓
    Prediction / Scanning / Completion
       ↓
    Parse Tree
       ↓
    Leftmost Derivation

---

# 34. نتیجه‌گیری

این پروژه مفاهیم اصلی درس نظریه زبان‌ها و ماشین‌ها را در قالب یک نرم‌افزار گرافیکی و تعاملی پیاده‌سازی می‌کند.

در بخش Automata، کاربر می‌تواند DFA و NFA را به صورت گرافیکی بسازد، رشته اجرا کند، اجرای ماشین را مرحله‌به‌مرحله مشاهده کند و NFA یا ε-NFA را با الگوریتم Subset Construction به DFA تبدیل کند.

در بخش Grammar، امکان تعریف و ویرایش CFG، وارد کردن رشته، Parsing، نمایش Parse Tree و نمایش Leftmost Derivation وجود دارد.

مهم‌ترین الگوریتم پروژه تبدیل NFA به DFA است. در این الگوریتم هر State در DFA نماینده یک مجموعه از Stateهای NFA است. با استفاده از Move و ε-Closure، مجموعه‌های قابل دسترس ساخته می‌شوند تا در نهایت یک DFA معادل به دست آید.

همچنین جداسازی منطق الگوریتم‌ها از GUI باعث شده است که بخش‌های اصلی پروژه قابل تست و توسعه باشند.

**سازنده پروژه: محمدرضا کاظمی**
