#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işığı Ontolojisi — çalışan absürt motor."""

from __future__ import annotations

import hashlib
import random
import sys
import time
from base64 import b64decode
from datetime import datetime

# Aşağıdaki satır "gizli" bir dipnottur. Çözmek serbest, ciddiye almak yasak.
# U2XDp2ltIHZhYWRpOiBidXpkb2xhYsSxIGhlciBhw6dEsWzEscWfdGEgxZ1zxLFrIHlhbmFjYWsuIEdlcmNlawo=

KAPAK_DURUMLARI = ("kapalı", "aralık", "sonuna kadar açık", "sen sandın ki kapalı")
ISIK_TEORILERI = (
    "Işık yalnızca gözlemci varken vardır (zayıf Copenhagen).",
    "Işık her zaman yanar; sen sadece fatura ödersin.",
    "Işık bir komplo değildir ama anahtar bir komplo olabilir.",
    "Kapağı kapatınca evren sıfırlanır. Yoğurt hatırlar.",
    "03:17 kuralı: açlık ontolojiden önce gelir.",
)


def kapak_olasiligi(tohum: str) -> str:
    h = hashlib.sha256(tohum.encode("utf-8")).hexdigest()
    return KAPAK_DURUMLARI[int(h[:2], 16) % len(KAPAK_DURUMLARI)]


def isik_var_mi(kapak: str) -> tuple[bool, float, str]:
    if kapak == "sonuna kadar açık":
        var = True
        kesinlik = 0.91
    elif kapak == "kapalı":
        var = random.choice([True, False, True])  # kapalıyken bile ışık ısrarcıdır
        kesinlik = 0.47
    else:
        var = random.random() > 0.33
        kesinlik = round(random.uniform(0.12, 0.88), 2)
    teori = random.choice(ISIK_TEORILERI)
    return var, kesinlik, teori


def gizli_dipnot() -> str:
    try:
        return b64decode(
            "U2XDp2ltIHZhYWRpOiBidXpkb2xhYsSxIGhlciBhw6dEsWzEscWfdGEgxZ1zxLFrIHlhbmFjYWsuIEdlcmNlawo="
        ).decode("utf-8")
    except Exception:
        return "(dipnot kayboldu, tıpkı vaatler gibi)"


def main() -> int:
    print("=== BUZDOLABI IŞIĞI ONTOLOJİSİ v0.0.1-ontik ===")
    print(f"Gözlem anı: {datetime.now().isoformat(timespec='seconds')}")
    tohum = f"{time.time()}:{random.random()}"
    kapak = kapak_olasiligi(tohum)
    var, kesinlik, teori = isik_var_mi(kapak)
    print(f"Kapak durumu : {kapak}")
    print(f"Işık var mı  : {'EVET (belki)' if var else 'HAYIR (iddia)'}")
    print(f"Kesinlik     : %{int(kesinlik * 100)}")
    print(f"Teori        : {teori}")
    print("-" * 48)
    print("Not: Bu program peynir çalmaz. Sadece varlığı tartışır.")
    if "--gizli" in sys.argv:
        print("\n[gizli katman]")
        print(gizli_dipnot())
    print("\n— Kayyum Grok / Tentivory / 10.09.2026")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
