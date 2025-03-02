# Contributing

E projekteh dafanin kontribisyon ek ak sugjestion yo. Pifò kontribisyon mande pou ou dakò ak yon Akò Lisyen Kontribitè (CLA) ki deklare ke ou gen dwa, e aktyèlman fè sa, pou ba nou dwa pou itilize kontribisyon ou. Pou plis detay, vizite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Lè ou soumèt yon pull request, yon bot CLA ap otomatikman detèmine si ou bezwen bay yon CLA epi dekore PR a kòmsadwa (egzanp, verifikasyon estati, kòmantè). Senpleman swiv enstriksyon yo bay pa bot la. Ou pral sèlman bezwen fè sa yon fwa atravè tout depo ki itilize CLA nou an.

## Kòd Kondwit

E projekteh adopte [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Pou plis enfòmasyon, li [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oswa kontakte [opencode@microsoft.com](mailto:opencode@microsoft.com) pou nenpòt lòt kesyon oswa kòmantè.

## Prekosyon pou kreye pwoblèm

Tanpri pa louvri pwoblèm GitHub pou kesyon sipò jeneral paske lis GitHub la ta dwe itilize pou demann karakteristik ak rapò pinèz. Fason sa a, nou ka pi fasil swiv pwoblèm oswa pinèz aktyèl ki soti nan kòd la epi kenbe diskisyon jeneral separe de kòd aktyèl la.

## Kijan Pou Kontribye

### Gid Pou Pull Requests

Lè w ap soumèt yon pull request (PR) nan depo Phi-3 CookBook la, tanpri swiv gid sa yo:

- **Fòke Depo a**: Toujou fòke depo a nan kont ou anvan ou fè modifikasyon ou yo.

- **Separe pull requests (PR)**:
  - Soumèt chak kalite chanjman nan pwòp pull request li yo. Pa egzanp, repare pinèz ak mete ajou dokiman yo ta dwe soumèt nan PR separe.
  - Korije erè tipografik ak ti mete ajou dokiman yo ka konbine nan yon sèl PR kote sa apwopriye.

- **Jere konfli fizyon yo**: Si pull request ou a montre konfli fizyon, mete ajou branch lokal `main` ou a pou reflete depo prensipal la anvan ou fè modifikasyon ou yo.

- **Soumèt tradiksyon yo**: Lè w ap soumèt yon PR tradiksyon, asire w ke dosye tradiksyon an gen tradiksyon pou tout dosye nan katab orijinal la.

### Gid Pou Tradiksyon

> [!IMPORTANT]  
> Lè w ap tradui tèks nan depo sa a, pa itilize tradiksyon machin. Se sèlman volontè ki metrize langaj yo ki ka fè tradiksyon yo.

Si ou metrize yon lang ki pa angle, ou ka ede tradui kontni an. Swiv etap sa yo pou asire kontribisyon tradiksyon ou yo byen entegre:

- **Kreye yon katab tradiksyon**: Ale nan katab seksyon ki apwopriye a epi kreye yon katab tradiksyon pou lang ou ap kontribye a. Pa egzanp:
  - Pou seksyon entwodiksyon: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Pou seksyon kòmanse rapid: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Kontinye modèl sa a pou lòt seksyon yo (03.Inference, 04.Finetuning, elatriye)

- **Mete ajou chemen relatif yo**: Lè w ap tradui, ajiste estrikti katab la pa ajoute `../../` nan kòmansman chemen relatif yo nan dosye markdown yo pou asire lyen yo travay kòrèkteman. Pa egzanp, chanje jan sa a:
  - Chanje `(../../imgs/01/phi3aisafety.png)` pou `(../../../../imgs/01/phi3aisafety.png)`

- **Òganize tradiksyon ou yo**: Chak dosye tradui yo ta dwe mete nan katab tradiksyon seksyon ki koresponn lan. Pa egzanp, si w ap tradui seksyon entwodiksyon an nan lang panyòl, ou ta kreye jan sa a:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Soumèt yon PR konplè**: Asire w ke tout dosye tradui pou yon seksyon enkli nan yon sèl PR. Nou pa aksepte tradiksyon pasyèl pou yon seksyon. Lè w ap soumèt yon PR tradiksyon, asire w ke katab tradiksyon an gen tradiksyon pou tout dosye nan katab orijinal la.

### Gid Pou Ekri

Pou asire konsistans atravè tout dokiman yo, tanpri itilize gid sa yo:

- **Fòmat URL**: Mete tout URL yo nan parantèz kare ki swiv pa parantèz won, san okenn espas anplis alantou oswa andedan yo. Pa egzanp: `[example](https://example.com)`.

- **Lyen relatif**: Sèvi ak `./` pou lyen relatif ki montre dosye oswa katab nan repèrtwar aktyèl la, epi `../` pou sa yo ki nan yon repèrtwar paran. Pa egzanp: `[example](../../path/to/file)` oswa `[example](../../../path/to/file)`.

- **Pa sèvi ak lokal espesifik peyi**: Asire w ke lyen ou yo pa gen lokal espesifik peyi. Pa egzanp, evite `/en-us/` oswa `/en/`.

- **Depo imaj**: Mete tout imaj nan katab `./imgs` la.

- **Non imaj deskriptif**: Bay imaj yo non deskriptif lè w sèvi ak karaktè angle, chif, ak tirè. Pa egzanp: `example-image.jpg`.

## Workflow GitHub yo

Lè w soumèt yon pull request, workflow sa yo pral aktive pou valide chanjman yo. Swiv enstriksyon ki anba yo pou asire pull request ou a pase verifikasyon workflow yo:

- [Verifye Chemen Relatif Ki Kase](../..)
- [Verifye URL San Lokal](../..)

### Verifye Chemen Relatif Ki Kase

Workflow sa a asire ke tout chemen relatif nan dosye ou yo kòrèk.

1. Pou asire lyen ou yo ap travay kòrèkteman, fè travay sa yo lè w ap itilize VS Code:
    - Pase sourit ou sou nenpòt lyen nan dosye ou yo.
    - Peze **Ctrl + Click** pou navige nan lyen an.
    - Si ou klike sou yon lyen epi li pa travay lokalman, sa ap aktive workflow a epi li pap travay sou GitHub.

1. Pou rezoud pwoblèm sa a, fè travay sa yo lè w ap itilize sijesyon chemen yo bay pa VS Code:
    - Tape `./` oswa `../`.
    - VS Code ap pwopoze w chwazi nan opsyon ki disponib yo baze sou sa ou te tape.
    - Swiv chemen an lè w klike sou dosye oswa katab ou vle a pou asire chemen ou kòrèk.

Yon fwa ou te ajoute chemen relatif kòrèk la, sove epi pouse chanjman ou yo.

### Verifye URL San Lokal

Workflow sa a asire ke nenpòt URL entènèt pa gen yon lokal espesifik peyi. Kòm depo sa a aksesib globalman, li enpòtan pou asire ke URL yo pa gen lokal peyi ou.

1. Pou verifye ke URL ou yo pa gen lokal peyi, fè travay sa yo:

    - Tcheke tèks tankou `/en-us/`, `/en/`, oswa nenpòt lòt lokal lang nan URL yo.
    - Si sa yo pa prezan nan URL ou yo, lè sa a ou pral pase verifikasyon sa a.

1. Pou rezoud pwoblèm sa a, fè travay sa yo:
    - Louvri chemen dosye ki make pa workflow a.
    - Retire lokal peyi a nan URL yo.

Yon fwa ou retire lokal peyi a, sove epi pouse chanjman ou yo.

### Verifye URL Ki Kase

Workflow sa a asire ke nenpòt URL entènèt nan dosye ou yo ap travay epi retounen kòd estati 200.

1. Pou verifye ke URL ou yo ap travay kòrèkteman, fè travay sa yo:
    - Tcheke estati URL yo nan dosye ou yo.

2. Pou rezoud nenpòt URL ki kase, fè travay sa yo:
    - Louvri dosye ki gen URL ki kase a.
    - Mete ajou URL a ak yon kòrèk.

Yon fwa ou te ranje URL yo, sove epi pouse chanjman ou yo.

> [!NOTE]  
> Gen ka kote verifikasyon URL la ka echwe menm si lyen an aksesib. Sa ka rive pou plizyè rezon, tankou:
>
> - **Restriksyon rezo**: Sèvè aksyon GitHub yo ka gen restriksyon rezo ki anpeche aksè nan sèten URL.
> - **Pwoblèm tan ekspirasyon**: URL ki pran twòp tan pou reponn ka lakòz yon erè tan ekspirasyon nan workflow la.
> - **Pwoblèm sèvè tanporè**: Entèval sèvè oswa antretyen ka fè yon URL tanporèman endisponib pandan validasyon an.

It seems like you've requested a translation to "mo," but it's unclear what language "mo" refers to. Could you clarify the specific language or dialect you have in mind? For example, are you referring to Māori, Mongolian, or something else?