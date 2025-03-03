# Hozzájárulás

Ez a projekt örömmel fogadja a hozzájárulásokat és javaslatokat. A legtöbb hozzájáruláshoz szükséges egy Hozzájárulói Licencszerződés (Contributor License Agreement, CLA) elfogadása, amelyben kijelented, hogy jogodban áll, és ténylegesen meg is adod nekünk a jogokat a hozzájárulásod felhasználására. További részletekért látogass el a következő oldalra: [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Amikor egy pull requestet nyújtasz be, egy CLA bot automatikusan meghatározza, hogy szükséges-e CLA-t benyújtanod, és ennek megfelelően megjelöli a PR-t (pl. állapotellenőrzés, megjegyzés). Csak kövesd a bot által adott utasításokat. Ezt csak egyszer kell megtenned minden olyan repó esetében, amely a CLA-t használja.

## Magatartási kódex

Ez a projekt elfogadta a [Microsoft Nyílt Forráskódú Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/). További információért olvasd el a [Magatartási Kódex GYIK-et](https://opensource.microsoft.com/codeofconduct/faq/) vagy lépj kapcsolatba az [opencode@microsoft.com](mailto:opencode@microsoft.com) címen, ha további kérdéseid vagy megjegyzéseid vannak.

## Figyelmeztetések problémák létrehozásakor

Kérjük, ne nyiss GitHub problémát általános támogatási kérdések miatt, mivel a GitHub listát a funkciókérések és hibajelentések számára tartjuk fenn. Így könnyebben tudjuk nyomon követni a tényleges problémákat vagy hibákat a kódból, és különválaszthatjuk az általános megbeszéléseket a tényleges kódtól.

## Hogyan járulhatsz hozzá

### Pull Request irányelvek

Amikor pull requestet (PR-t) nyújtasz be a Phi-3 CookBook repóhoz, kövesd az alábbi irányelveket:

- **Forkold a repót**: Mindig forkold a repót a saját fiókodba, mielőtt módosításokat végeznél rajta.

- **Külön pull requestek (PR-ek)**:
  - Minden változtatást külön PR-ben nyújts be. Például a hibajavításokat és a dokumentáció frissítéseket külön PR-ben küldd be.
  - Helyesírási hibák javítását és kisebb dokumentációfrissítéseket egy PR-be is összevonhatsz, ha indokolt.

- **Merge konfliktusok kezelése**: Ha a pull requested merge konfliktusokat mutat, frissítsd a helyi `main` ágadat, hogy tükrözze a fő repót, mielőtt módosításokat végeznél.

- **Fordítások benyújtása**: Ha fordítási PR-t nyújtasz be, győződj meg róla, hogy a fordítási mappa tartalmazza az eredeti mappa összes fájljának fordítását.

### Fordítási irányelvek

> [!IMPORTANT]
>
> Ne használj gépi fordítást a repóban található szövegek fordításakor. Csak olyan nyelveken vállalj fordítást, amelyeken jártas vagy.

Ha jártas vagy egy nem angol nyelvben, segíthetsz a tartalom fordításában. Az alábbi lépéseket követve biztosíthatod, hogy a fordításaid megfelelően integrálódjanak:

- **Fordítási mappa létrehozása**: Navigálj a megfelelő szekció mappájába, és hozz létre egy fordítási mappát a nyelvhez, amelyhez hozzájárulsz. Például:
  - Bevezető szekció esetén: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Gyorsindítás szekció esetén: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Folytasd ezt a mintát a többi szekcióra (03.Inference, 04.Finetuning, stb.).

- **Relatív útvonalak frissítése**: Fordítás közben állítsd be a mappaszerkezetet úgy, hogy hozzáadd a `../../` előtagot a relatív útvonalak elejére a markdown fájlokban, hogy a linkek megfelelően működjenek. Például, változtasd meg az alábbiak szerint:
  - `(../../imgs/01/phi3aisafety.png)` változtatása `(../../../../imgs/01/phi3aisafety.png)`-re.

- **Fordítások rendszerezése**: Minden lefordított fájlt helyezz el a megfelelő szekció fordítási mappájába. Például, ha a bevezető szekciót fordítod spanyolra, hozz létre egy ilyen mappát:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Teljes PR benyújtása**: Győződj meg róla, hogy egy szekció összes lefordított fájlja benne van egy PR-ben. Nem fogadunk el részleges fordításokat egy szekcióhoz. Fordítási PR benyújtásakor győződj meg róla, hogy a fordítási mappa tartalmazza az eredeti mappa összes fájljának fordítását.

### Írási irányelvek

A következetesség biztosítása érdekében az összes dokumentumban, kérjük, kövesd az alábbi irányelveket:

- **URL-formázás**: Az összes URL-t zárójelbe tedd szögletes zárójelben, amit zárójelek követnek, extra szóközök nélkül körülöttük vagy bennük. Például: `[example](https://www.microsoft.com)`.

- **Relatív linkek**: Használj `./`-t a jelenlegi könyvtárban lévő fájlokra vagy mappákra mutató relatív linkekhez, és `../`-t a szülő könyvtárban lévőkre. Például: `[example](../../path/to/file)` vagy `[example](../../../path/to/file)`.

- **Nem ország-specifikus helyi beállítások**: Győződj meg róla, hogy a linkjeid nem tartalmaznak ország-specifikus helyi beállításokat. Például kerüld a `/en-us/` vagy `/en/` használatát.

- **Képek tárolása**: Minden képet az `./imgs` mappában tárolj.

- **Leíró képfájlnevek**: Nevezd el a képeket leíróan angol karakterek, számok és kötőjelek használatával. Például: `example-image.jpg`.

## GitHub Munkafolyamatok

Amikor pull requestet nyújtasz be, a következő munkafolyamatok aktiválódnak, hogy érvényesítsék a változtatásokat. Az alábbi utasításokat követve biztosíthatod, hogy a pull requested megfeleljen a munkafolyamat-ellenőrzéseknek:

- [Hibás relatív útvonalak ellenőrzése](../..)
- [URL-ek helyi beállítások nélküli ellenőrzése](../..)

### Hibás relatív útvonalak ellenőrzése

Ez a munkafolyamat biztosítja, hogy az összes relatív útvonal a fájljaidban helyes legyen.

1. Annak biztosítása érdekében, hogy a linkjeid megfelelően működjenek, hajtsd végre az alábbi feladatokat a VS Code segítségével:
    - Mutass rá bármely linkre a fájljaidban.
    - Nyomd meg a **Ctrl + Kattintás** kombinációt, hogy a linkre navigálj.
    - Ha egy linkre kattintasz, és az nem működik helyben, akkor a munkafolyamat hibát fog jelezni, és nem fog működni a GitHubon sem.

1. A probléma megoldásához hajtsd végre az alábbi feladatokat a VS Code által adott útvonaljavaslatok segítségével:
    - Írd be a `./` vagy `../` parancsot.
    - A VS Code felkínálja a rendelkezésre álló lehetőségeket az alapján, amit beírtál.
    - Kövesd az útvonalat, kattintva a kívánt fájlra vagy mappára, hogy megbizonyosodj az útvonal helyességéről.

Miután hozzáadtad a helyes relatív útvonalat, mentsd el és töltsd fel a változtatásokat.

### URL-ek helyi beállítások nélküli ellenőrzése

Ez a munkafolyamat biztosítja, hogy a webes URL-ek ne tartalmazzanak ország-specifikus helyi beállításokat. Mivel ez a repó globálisan elérhető, fontos, hogy az URL-ek ne tartalmazzanak ország-specifikus helyi beállításokat.

1. Az URL-ek helyi beállítás nélküli ellenőrzéséhez hajtsd végre az alábbi feladatokat:

    - Ellenőrizd a fájljaidban található URL-eket, hogy tartalmaznak-e például `/en-us/`, `/en/` vagy bármilyen más nyelvi helyi beállítást.
    - Ha ezek nincsenek jelen az URL-jeidben, akkor át fogsz menni ezen az ellenőrzésen.

1. A probléma megoldásához hajtsd végre az alábbi feladatokat:
    - Nyisd meg a munkafolyamat által kiemelt fájl útvonalát.
    - Távolítsd el az URL-ekből az ország-specifikus helyi beállítást.

Miután eltávolítottad a helyi beállítást, mentsd el és töltsd fel a változtatásokat.

### Hibás URL-ek ellenőrzése

Ez a munkafolyamat biztosítja, hogy a fájljaidban található webes URL-ek működjenek, és 200-as állapotkódot adjanak vissza.

1. Az URL-ek helyes működésének ellenőrzéséhez hajtsd végre az alábbi feladatokat:
    - Ellenőrizd a fájljaidban található URL-ek állapotát.

2. A hibás URL-ek javításához hajtsd végre az alábbi feladatokat:
    - Nyisd meg azt a fájlt, amely tartalmazza a hibás URL-t.
    - Frissítsd az URL-t a helyesre.

Miután kijavítottad az URL-eket, mentsd el és töltsd fel a változtatásokat.

> [!NOTE]
>
> Előfordulhatnak olyan esetek, amikor az URL-ellenőrzés sikertelen, még akkor is, ha a link elérhető. Ez több okból is előfordulhat, például:
>
> - **Hálózati korlátozások:** A GitHub akciószerverei hálózati korlátozások miatt nem érhetnek el bizonyos URL-eket.
> - **Időtúllépési problémák:** Azok az URL-ek, amelyek túl sokáig válaszolnak, időtúllépési hibát okozhatnak a munkafolyamatban.
> - **Ideiglenes szerverproblémák:** Alkalmanként előforduló szerverleállás vagy karbantartás miatt egy URL ideiglenesen elérhetetlen lehet az érvényesítés során.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.