# Az archívum újrabesorolása — jóváhagyás

- **Dátum:** 2026-09-28
- **Mit:** az archívum és a külső tételek újrabesorolása a befagyasztott kalibrációval
  (`analysis/temalista_kalibracio.json`), a kapu (`gate_result.json`) sikeres egyszeri
  futtatása után.
- **Ki:** a szerző, a munkamenetben ("deploy the new themes").
- **Az áthelyezési lista ellenőrzőösszege** (`out/athelyezesek.json`, sha256):
  `78c1e7c6f7fd48e31f22cf5b2cfae529bcfb06414ac88ffc4563695ac8b46571`
- **Összesen 818 írás:** változatlan 113, bővül 77, szűkül 34, módosul 346, témát kap 29,
  téma nélkül marad 218, továbbra is téma nélkül 1.

## A jóváhagyott lista óta hozott döntések

A szerző a 2026-09-24-i listára (`df76cd5f…`) két kérdésben az asszisztens javaslatát fogadta el:

1. **Lapszemle-összefoglalók:** a szerző saját `lapszemle` címkéjét viselő írások nem kapnak
   tárgyi témát (`SUBJECTLESS_LABELS` az `assign.py`-ban). 22 írást érint; ettől változott
   az ellenőrzőösszeg.
2. **δ = 0,15** marad. A laza másodlagos témák szűkítése új dev-futtatást és új kaput igényelne.

## Megjegyzés a kapu eredményéhez

A `gate_result.json` az előregisztráció commitját `54128db…` néven rögzíti. 2026-09-28-án az
ág a `main`-re került (rebase), ezért ugyanaz a commit most `3f13d21`. A befagyasztott fájlok
(`temalista_kalibracio.json`, `temalista.yaml`) a két commit között bájtra azonosak
(`git diff 54128db 3f13d21` üres volt, amíg a régi commit elérhető volt).
