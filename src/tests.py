# -*- coding: utf-8 -*-
"""Presse le catalogue BBQ dans un vrai navigateur.

Ce qui compte ici, dans cet ordre :

  1. AUCUN NOM DE FABRICANT. Le brief demandait « presentation des
     fabricants ». Le test liste les marques les plus courantes du secteur et
     verifie qu'aucune n'apparait. Une marque absente du document ne peut pas
     etre lue comme une marque distribuee.
  2. AUCUNE VALEUR CHIFFREE ni conformite affirmee. Le gaz et l'electrique
     sont reglementes : « conforme » est une declaration que seul le fabricant
     peut faire.
  3. Le catalogue entier est dans le HTML servi.
  4. Les trois axes se croisent et le compte suit ce qui est VISIBLE.
  5. Les deux bords, la colonne, le contraste.

Usage :
  python3 tests.py                      la vraie page
  python3 tests.py page-truquee.html    CONTROLE NEGATIF : doit echouer
"""
import os, re, sys
from playwright.sync_api import sync_playwright
import data as D

ICI = os.path.dirname(os.path.abspath(__file__))
CONTROLE = len(sys.argv) > 1
PAGE = os.path.abspath(sys.argv[1]) if CONTROLE else os.path.join(ICI, 'index.html')
if not os.path.exists(PAGE):
    PAGE = os.path.join(os.path.dirname(ICI), 'index.html')
if not os.path.exists(PAGE):
    raise SystemExit('index.html introuvable — lancer build.py d’abord')
URL = 'file://' + PAGE
ok = ko = 0


def t(nom, cond, detail=''):
    global ok, ko
    if cond:
        ok += 1; print('  OK    %s' % nom)
    else:
        ko += 1; print('  ECHEC %s   %s' % (nom, detail))


with sync_playwright() as pw:
    nav = pw.chromium.launch()

    # ---------------------------------------------------------------- 1
    print('\n1. Sans JavaScript, le catalogue est entier')
    sansjs = nav.new_context(java_script_enabled=False)
    p0 = sansjs.new_page()
    p0.set_viewport_size({'width': 1280, 'height': 900})
    p0.goto(URL, wait_until='load')
    n0 = len(p0.query_selector_all('.o'))
    t('les %d categories sont dans le HTML servi' % len(D.CATEGORIES),
      n0 == len(D.CATEGORIES), '%d rendues' % n0)
    caches = p0.evaluate("""() => [...document.querySelectorAll('.o')]
        .filter(e => e.hidden || getComputedStyle(e).display === 'none').length""")
    t('aucune n’est masquee au chargement', caches == 0, str(caches))
    t('les deux blocs du bas sont en texte, sans script',
      len(p0.query_selector_all('.ref li')) == len(D.FICHE_FABRICANT)
      and len(p0.query_selector_all('ol.chaine li')) == len(D.CHAINE))
    t('la chaine d’approvisionnement est une liste ORDONNEE',
      p0.eval_on_selector('.chaine', 'e=>e.tagName') == 'OL')
    sansjs.close()

    pg = nav.new_page()
    err = []
    pg.on('pageerror', lambda e: err.append(str(e)))
    pg.on('console', lambda m: err.append(m.text) if m.type == 'error' else None)
    pg.set_viewport_size({'width': 1280, 'height': 900})
    pg.goto(URL, wait_until='load')
    corps = pg.eval_on_selector('body', 'e=>e.innerText')

    # ---------------------------------------------------------------- 2
    print('\n2. Aucun fabricant nomme')
    # Les marques les plus courantes du secteur. Aucune ne doit apparaitre.
    MARQUES = ['Weber', 'Napoleon', 'Traeger', 'Big Green Egg', 'Kamado',
               'Char-Broil', 'Broil King', 'Campingaz', 'Cadac', 'Landmann',
               'Ooni', 'Pit Boss', 'Masterbuilt', 'Barbecook', 'Verycook',
               'Forge Adour', 'Eno', 'Krampouz', 'Rösle', 'Tefal', 'Blackstone']
    trouvees = [m for m in MARQUES if re.search(r'\b' + re.escape(m), corps, re.I)]
    t('aucune marque de fabricant n’apparait sur la page',
      not trouvees, str(trouvees))
    t('la page dit explicitement qu’elle n’en nomme aucun',
      'aucun fabricant' in corps.lower())

    print('\n   ... aucune valeur chiffree, aucune conformite affirmee')
    INTERDITS = [
        ('une puissance chiffree', r'[0-9][0-9\s.,]*\s?(kW|W|BTU|kcal)\b'),
        ('une temperature chiffree', r'[0-9][0-9\s.,]*\s?°\s?[CF]\b'),
        ('une surface ou une dimension chiffree',
         r'[0-9][0-9\s.,]*\s?(cm2|cm²|cm|mm|m2|m²)\b'),
        ('un poids chiffre', r'[0-9][0-9\s.,]*\s?(kg|g)\b'),
        ('un nombre de bruleurs', r'\b[0-9]+\s?br[ûu]leurs?\b'),
        ('un prix', r'[0-9][0-9\s.,]*\s?(€|\$|EUR|USD|CAD)\b'),
        ('une quantite minimale chiffree',
         r'\b(minimum de commande|quantit[ée] minimale|MOQ)[^.]{0,20}[0-9]'),
        ('un delai chiffre',
         r'\b(d[ée]lai|livraison|expédition)[^.]{0,25}\b[0-9]+\s?(jours?|semaines?|mois)\b'),
        ('une garantie chiffree', r'\bgarantie[^.]{0,25}\b[0-9]+\s?(ans?|mois)\b'),
    ]
    for nom, rx in INTERDITS:
        m = re.search(rx, corps, re.I)
        t('la page n’affiche jamais %s' % nom, m is None,
          repr(corps[max(0, m.start() - 40):m.end() + 20]) if m else '')

    t('aucune conformite n’est affirmee',
      not re.search(r'\b(est|sont|nos produits sont)\s+conformes?\b', corps, re.I))
    t('aucun classement ni superlatif',
      not re.search(r'\b(top\s*\d|le meilleur|n°\s*1|leader)\b', corps, re.I))
    t('la page dit elle-meme ce qu’elle n’affiche pas',
      'volontairement' in corps.lower())
    t('chaque carte annonce sa grille de champs',
      len(pg.query_selector_all('.o .car b')) == len(D.CATEGORIES))

    # ---------------------------------------------------------------- 3
    print('\n3. Les compteurs sont derives des donnees')
    kpi = pg.eval_on_selector_all('.kpi b', 'e=>e.map(x=>x.textContent)')
    for i, (lab, att) in enumerate([
            ('categories', len(D.CATEGORIES)), ('familles', len(D.FAMILLES)),
            ('energies', len(D.ENERGIES)), ('segments', len(D.SEGMENTS)),
            ('champs', len(D.CHAMPS))]):
        t('le bandeau annonce le vrai nombre de %s' % lab,
          kpi[i] == str(att), '%s vs %d' % (kpi[i], att))
    t('le compte de depart vaut le nombre reel',
      str(len(D.CATEGORIES)) in pg.eval_on_selector('#compte', 'e=>e.textContent'))

    # ---------------------------------------------------------------- 4
    print('\n4. Les trois axes filtrent, et le compte suit ce qui est visible')

    def visibles():
        return pg.evaluate("""() => [...document.querySelectorAll('.o')]
            .filter(e => e.getClientRects().length > 0).length""")

    for code, nom in D.FAMILLES:
        pg.select_option('#f-fam', code); pg.wait_for_timeout(110)
        att = sum(1 for c in D.CATEGORIES if c[0] == code)
        t('famille « %s » : %d' % (nom, att),
          visibles() == att, '%d vs %d' % (visibles(), att))
    pg.click('#raz'); pg.wait_for_timeout(120)

    for code, nom in D.ENERGIES:
        pg.select_option('#f-ene', code); pg.wait_for_timeout(110)
        att = sum(1 for c in D.CATEGORIES if c[1] == code)
        t('energie « %s » : %d' % (nom, att),
          visibles() == att, '%d vs %d' % (visibles(), att))
    pg.click('#raz'); pg.wait_for_timeout(120)

    for code, nom in D.SEGMENTS:
        pg.select_option('#f-seg', code); pg.wait_for_timeout(110)
        att = sum(1 for c in D.CATEGORIES if code in c[3])
        t('segment « %s » : %d' % (nom, att),
          visibles() == att, '%d vs %d' % (visibles(), att))
    pg.click('#raz'); pg.wait_for_timeout(120)

    print('\n   ... et croises a trois')
    for f, en, sg in (('barbecues', 'gaz', 'particulier'),
                      ('fumoirs', 'bois', 'restauration'),
                      ('pieces', 'gaz', 'revente'),
                      ('accessoires', 'aucune', 'restauration')):
        pg.click('#raz'); pg.wait_for_timeout(70)
        pg.select_option('#f-fam', f)
        pg.select_option('#f-ene', en)
        pg.select_option('#f-seg', sg); pg.wait_for_timeout(150)
        att = sum(1 for c in D.CATEGORIES
                  if c[0] == f and c[1] == en and sg in c[3])
        aff = pg.eval_on_selector('#compte', 'e=>e.textContent')
        t('%s + %s + %s : %d' % (f, en, sg, att),
          visibles() == att, '%d vs %d' % (visibles(), att))
        t('  le compte affiche correspond',
          (str(att) in aff) if att else ('Aucune' in aff), '%s / %d' % (aff, att))
        mauvais = pg.evaluate("""([f,en,sg]) => [...document.querySelectorAll('.o')]
            .filter(e => e.getClientRects().length > 0)
            .filter(e => e.dataset.fam !== f || e.dataset.ene !== en
                      || !(' '+e.dataset.seg+' ').includes(' '+sg+' '))
            .map(e => e.querySelector('h3').textContent)""", [f, en, sg])
        t('  aucune carte hors criteres n’est affichee', not mauvais, str(mauvais[:2]))
    pg.click('#raz'); pg.wait_for_timeout(120)

    # ---------------------------------------------------------------- 5
    print('\n5. La recherche ignore les accents')
    pg.fill('#f-q', 'pieces detachees'); pg.wait_for_timeout(170)
    att = sum(1 for c in D.CATEGORIES
              if 'pieces' in (c[0],) or 'pieces' in c[5]
              or 'pièces détachées' in c[4].lower())
    t('« pieces detachees » sans accent ramene des resultats',
      visibles() > 0, str(visibles()))
    pg.fill('#f-q', 'electrique'); pg.wait_for_timeout(170)
    t('« electrique » sans accent trouve « Électrique »',
      visibles() >= sum(1 for c in D.CATEGORIES if c[1] == 'electrique'),
      str(visibles()))
    pg.fill('#f-q', 'zzzzzz'); pg.wait_for_timeout(170)
    t('une recherche sans resultat le dit', visibles() == 0 and
      pg.eval_on_selector('#vide', 'e=>e.getClientRects().length > 0'))
    pg.click('#raz'); pg.wait_for_timeout(120)

    # ---------------------------------------------------------------- 6
    print('\n6. Rendu : les deux bords et la colonne, a trois largeurs')
    JS_BORDS = """
    () => {
      const w = document.documentElement.clientWidth, out = [];
      document.querySelectorAll('body *').forEach(e => {
        if (e.hidden) return;
        const cs = getComputedStyle(e);
        if (cs.display === 'none' || cs.visibility === 'hidden') return;
        const r = e.getBoundingClientRect();
        if (r.width < 1 && r.height < 1) return;
        if (r.left < -1) out.push(['gauche', Math.round(r.left), e.className || e.tagName]);
        else if (r.right > w + 1) out.push(['droite', Math.round(r.right - w), e.className || e.tagName]);
      });
      return out.slice(0, 4);
    }"""
    JS_ALIGN = """
    () => {
      const b = s => { const e = document.querySelector(s);
        const r = e.getBoundingClientRect(); return [r.left, r.right]; };
      const logo = b('.logo'), titre = b('.hero h1'),
            nav = b('.tbar nav a:last-child');
      return {gauche: Math.abs(logo[0] - titre[0]),
              droite: Math.abs((document.documentElement.clientWidth - nav[1]) - titre[0])};
    }"""
    for w in (390, 768, 1280):
        pg.set_viewport_size({'width': w, 'height': 900})
        pg.wait_for_timeout(180)
        bords = pg.evaluate(JS_BORDS)
        t('aucun debordement a %d px, ni a gauche ni a droite' % w,
          not bords, str(bords))
        al = pg.evaluate(JS_ALIGN)
        t('  la barre du haut est alignee sur la colonne a %d px' % w,
          al['gauche'] <= 1 and al['droite'] <= 1, str(al))
    pg.set_viewport_size({'width': 1280, 'height': 900})
    pg.wait_for_timeout(150)

    JS_CONTRASTE = """
    () => {
      const lum = c => { const f = v => { v/=255; return v<=0.03928 ? v/12.92
        : Math.pow((v+0.055)/1.055, 2.4); };
        return 0.2126*f(c[0]) + 0.7152*f(c[1]) + 0.0722*f(c[2]); };
      const parse = s => { const m = s.match(/[\\d.]+/g); return m ? m.slice(0,3).map(Number) : null; };
      const alpha = s => { const m = s.match(/[\\d.]+/g); return m && m.length>3 ? parseFloat(m[3]) : 1; };
      const bg = el => { let e = el;
        while (e) { const c = getComputedStyle(e).backgroundColor;
          if (c && alpha(c) > 0.85) return parse(c); e = e.parentElement; }
        return [255,255,255]; };
      const bas = [];
      document.querySelectorAll('body *').forEach(el => {
        if (el.hidden) return;
        const txt = [...el.childNodes].filter(n => n.nodeType === 3)
          .map(n => n.textContent.trim()).join(' ').trim();
        if (!txt) return;
        const cs = getComputedStyle(el);
        if (cs.visibility === 'hidden' || cs.display === 'none') return;
        const r = el.getBoundingClientRect();
        if (r.width < 2 || r.height < 2) return;
        const fg = parse(cs.color), b = bg(el);
        if (!fg || !b) return;
        const l1 = lum(fg), l2 = lum(b);
        const ratio = (Math.max(l1,l2)+0.05) / (Math.min(l1,l2)+0.05);
        const px = parseFloat(cs.fontSize);
        const gros = px >= 24 || (px >= 18.66 && parseInt(cs.fontWeight,10) >= 700);
        if (ratio < (gros ? 3 : 4.5)) bas.push([txt.slice(0,36), ratio.toFixed(2), px]);
      });
      return bas;
    }"""
    bas = pg.evaluate(JS_CONTRASTE)
    t('contraste : 0 element sous le seuil', not bas, str(bas[:3]))
    t('aucune erreur JS', not err, str(err[:3]))

    # Un controle negatif n'ecrit AUCUNE capture : sinon la page truquee
    # ecrase les images livrables.
    if CONTROLE:
        nav.close()
        print('\n%d OK, %d ECHEC  (controle negatif : aucune capture ecrite)'
              % (ok, ko))
        sys.exit(0 if ko else 1)   # un controle negatif DOIT echouer

    pg.evaluate('() => window.scrollTo(0, 0)'); pg.wait_for_timeout(250)
    pg.screenshot(path='bq_1_haut.png')
    pg.select_option('#f-ene', 'charbon'); pg.wait_for_timeout(250)
    pg.eval_on_selector('.filtres', 'e=>e.scrollIntoView({block:"start"})')
    pg.wait_for_timeout(300)
    pg.screenshot(path='bq_2_charbon.png')
    pg.click('#raz'); pg.wait_for_timeout(150)
    pg.eval_on_selector('#fabricants', 'e=>e.scrollIntoView({block:"start"})')
    pg.wait_for_timeout(350)
    pg.screenshot(path='bq_3_fabricants.png')
    pg.set_viewport_size({'width': 390, 'height': 820})
    pg.evaluate('() => window.scrollTo(0, 0)'); pg.wait_for_timeout(350)
    pg.screenshot(path='bq_4_mobile.png')
    nav.close()

print('\n%d OK, %d ECHEC' % (ok, ko))
sys.exit(1 if ko else 0)
