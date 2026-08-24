# -*- coding: utf-8 -*-
"""Rend UNE page autonome : le catalogue BBQ et matériel de cuisson.

Meme mecanique que les pages eclairage et foresterie : un seul fichier, rien
de recharge, et SANS JAVASCRIPT le catalogue entier est deja dans le HTML.

Trois axes : la famille, l'ENERGIE et le SEGMENT. L'energie parce que c'est le
premier filtre reel d'un acheteur — elle decide de l'installation, de
l'autorisation d'exploiter et du cout d'usage. Le segment parce qu'un barbecue
de jardin et un gril de brasserie ne se vendent pas au meme client.
"""
import html, sys
import data as D

SORTIE = sys.argv[1] if len(sys.argv) > 1 else 'index.html'


def verifier():
    """Une faute de frappe dans un code de filtre ne casse rien a l'oeil :
    elle rend une carte introuvable pour toujours. On refuse de construire."""
    fam = {c for c, _ in D.FAMILLES}
    ene = {c for c, _ in D.ENERGIES}
    seg = {c for c, _ in D.SEGMENTS}
    ch = {c for c, _ in D.CHAMPS}
    err = []
    for f, e_, nom, segs, desc, champs in D.CATEGORIES:
        if f not in fam:
            err.append('%s : famille inconnue %r' % (nom, f))
        if e_ not in ene:
            err.append('%s : energie inconnue %r' % (nom, e_))
        if not segs:
            err.append('%s : aucun segment' % nom)
        for s in segs:
            if s not in seg:
                err.append('%s : segment inconnu %r' % (nom, s))
        for k in champs:
            if k not in ch:
                err.append('%s : champ inconnu %r' % (nom, k))
        if len(set(segs)) != len(segs):
            err.append('%s : segment en double' % nom)
        if len(set(champs)) != len(champs):
            err.append('%s : champ en double' % nom)
    noms = [c[2] for c in D.CATEGORIES]
    for n in set(noms):
        if noms.count(n) > 1:
            err.append('categorie en double : %s' % n)
    for c, nom in D.FAMILLES:
        if not any(x[0] == c for x in D.CATEGORIES):
            err.append('famille sans aucune categorie : %s' % nom)
    for c, nom in D.ENERGIES:
        if not any(x[1] == c for x in D.CATEGORIES):
            err.append('energie jamais employee : %s' % nom)
    for c, nom in D.SEGMENTS:
        if not any(c in x[3] for x in D.CATEGORIES):
            err.append('segment jamais employe : %s' % nom)
    for c, nom in D.CHAMPS:
        if not any(c in x[5] for x in D.CATEGORIES):
            err.append('champ jamais employe : %s' % nom)
    if err:
        raise SystemExit('DONNEES INVALIDES :\n  - ' + '\n  - '.join(err))


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{--bg:__BG__;--c:__C__;--l:__L__;--e:__E__;--tx:__TX__;--mu:__MU__;
      --ac:__AC__;--acd:__ACD__}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--tx);
  font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,
  "Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--ac)}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
h1,h2,h3{color:var(--e);line-height:1.16;letter-spacing:-.02em;margin:0 0 12px;font-weight:800}

.demo{background:var(--e);color:#e6dedb;font-size:12.5px;padding:9px 16px;text-align:center}
.demo b{color:#ffb489}

header.top{background:var(--c);border-bottom:1px solid var(--l);position:sticky;top:0;z-index:30}
/* padding-inline EXPLICITE, jamais le raccourci « padding:15px 0 ». Le meme
   <div> porte « wrap » et « tbar » : le raccourci effacerait le padding
   horizontal de .wrap (meme specificite, declaree plus bas) et collerait le
   logo au bord de l'ecran. Rien ne deborderait, donc aucun test de
   debordement ne le verrait. Trois pages ont ete livrees comme ca. */
.tbar{display:flex;align-items:center;gap:20px;padding-block:15px;flex-wrap:wrap}
.logo{font-weight:800;font-size:15.5px;letter-spacing:.04em;color:var(--e)}
.tbar nav{margin-left:auto;display:flex;gap:18px;font-size:14.5px}
.tbar nav a{color:var(--mu);text-decoration:none}
.tbar nav a:hover{color:var(--ac)}

.hero{background:var(--c);border-bottom:1px solid var(--l);padding:44px 0 38px}
.hero h1{font-size:clamp(27px,4vw,42px);max-width:20ch}
.hero p{font-size:17.5px;color:var(--mu);max-width:68ch;margin:0 0 20px}
.kpi{display:flex;flex-wrap:wrap;gap:10px 34px;margin-top:22px}
.kpi div b{display:block;font-size:26px;font-weight:800;color:var(--e);
  font-variant-numeric:tabular-nums;line-height:1.1}
.kpi div span{font-size:13px;color:var(--mu)}

main{padding:26px 0 60px}

.filtres{background:var(--c);border:1px solid var(--l);border-radius:12px;
  padding:16px;margin:0 0 18px;display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
.f{display:flex;flex-direction:column;gap:6px;min-width:0}
.f label{font-size:12.5px;font-weight:700;color:var(--e);letter-spacing:.02em}
.f select,.f input{width:100%;min-width:0;font:inherit;font-size:15px;color:var(--e);
  background:#fff;border:1px solid var(--l);border-radius:8px;padding:10px 11px}
.f select:focus,.f input:focus{outline:2px solid var(--ac);outline-offset:1px}
.barre{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:0 0 14px}
.compte{font-size:16px;font-weight:700;color:var(--e)}
.raz{font:inherit;font-size:14px;cursor:pointer;background:transparent;color:var(--ac);
  border:1px solid var(--l);border-radius:8px;padding:7px 13px}
.raz:hover{border-color:var(--ac)}

.liste{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.o{background:var(--c);border:1px solid var(--l);border-radius:12px;padding:17px 18px;
  display:flex;flex-direction:column;gap:9px;min-width:0}
.o[hidden]{display:none}
.o h3{font-size:16.5px;margin:0;line-height:1.3}
.o .ou{font-size:13px;color:var(--mu);margin:0;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.o .ou .fam{font-weight:600;color:var(--tx)}
.o p.d{font-size:14.5px;color:var(--tx);margin:0;flex:1 1 auto}

.en{font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
  padding:3px 9px;border-radius:99px;white-space:nowrap;
  background:#f7ece3;color:#7d3d10;border:1px solid #ecd6c5}
.en-charbon{background:#eceaea;color:#3d3634;border-color:#dcd7d5}
.en-electrique{background:#e9eff7;color:#1d4463;border-color:#cfdeeb}
.en-bois{background:#edf1e8;color:#3c5227;border-color:#d8e2cd}
.en-mixte{background:#f1ecf5;color:#4b2f66;border-color:#e0d5ea}
.en-aucune{background:#f2f1f0;color:#4a4340;border-color:#e0dcda}

.tags{display:flex;flex-wrap:wrap;gap:5px;margin:0}
.tags span{font-size:11.5px;font-weight:600;padding:3px 9px;border-radius:99px;
  background:#f3f0ee;color:#463c37;border:1px solid #e2dcd8;white-space:nowrap}

.car{margin:0;border-top:1px dashed var(--l);padding-top:9px}
.car b{display:block;font-size:11px;font-weight:800;letter-spacing:.04em;
  text-transform:uppercase;color:var(--mu);margin:0 0 6px}
.car ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:5px}
.car li{font-size:11.5px;padding:3px 9px;border-radius:6px;background:#f7f5f4;
  color:var(--tx);border:1px solid var(--l);white-space:nowrap}

.vide{grid-column:1/-1;background:var(--c);border:1px dashed var(--l);border-radius:12px;
  padding:26px;color:var(--mu);margin:0}

.bloc{background:var(--c);border:1px solid var(--l);border-radius:12px;
  padding:20px 22px;margin:22px 0 0}
.bloc h2{font-size:19px;margin:0 0 6px}
.bloc > p{color:var(--mu);font-size:14.5px;margin:0 0 15px;max-width:76ch}
.ref{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:repeat(2,1fr);gap:12px}
.ref li{border:1px solid var(--l);border-radius:10px;padding:13px 15px;background:#fbfaf9}
.ref b{display:block;color:var(--e);font-size:14.5px;margin:0 0 4px}
.ref span{font-size:13.5px;color:var(--tx)}
/* La chaine est ORDONNEE : une liste numerotee, pas des puces. L'ordre est
   l'information. */
ol.chaine{margin:0;padding:0 0 0 1.35em;display:grid;
  grid-template-columns:repeat(2,1fr);gap:12px 26px}
ol.chaine li{padding:0 0 0 4px}
ol.chaine b{display:block;color:var(--e);font-size:14.5px;margin:0 0 3px}
ol.chaine span{font-size:13.5px;color:var(--tx)}

.note{background:var(--c);border:1px solid var(--l);border-left:4px solid var(--ac);
  border-radius:0 10px 10px 0;padding:15px 18px;margin:24px 0 0;font-size:14.5px;color:var(--tx)}
.note b{display:block;color:var(--e);margin-bottom:4px}
.avert{background:#fdf8ec;border:1px solid #e8d9b0;border-left:4px solid #8a6410;
  border-radius:0 10px 10px 0;padding:15px 18px;margin:14px 0 0;font-size:14px;color:#54400f}
.avert b{display:block;margin-bottom:4px}

footer{border-top:1px solid var(--l);background:var(--c);padding:22px 0 44px;
  color:var(--mu);font-size:13.5px}

@media (max-width:980px){
  .filtres{grid-template-columns:1fr 1fr}
  .liste{grid-template-columns:1fr}
  .ref,ol.chaine{grid-template-columns:1fr}
}
@media (max-width:560px){
  .filtres{grid-template-columns:1fr}
  .kpi{gap:10px 22px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

JS = """
const $ = s => document.querySelector(s);

/* Sans accents : « electrique » doit trouver « Électrique », et « pieces
   detachees » doit trouver « pièces détachées ». */
const plat = s => (s || '').toLowerCase()
  .normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');

function filtrer(){
  const fam = $('#f-fam').value, ene = $('#f-ene').value,
        seg = $('#f-seg').value, q = plat($('#f-q').value.trim());
  let n = 0;
  document.querySelectorAll('.o').forEach(el => {
    const d = el.dataset;
    let ok = true;
    if (fam && d.fam !== fam) ok = false;
    if (ok && ene && d.ene !== ene) ok = false;
    /* Une categorie porte PLUSIEURS segments : appartenance, pas egalite. */
    if (ok && seg && !(' ' + d.seg + ' ').includes(' ' + seg + ' ')) ok = false;
    if (ok && q && !plat(d.rech).includes(q)) ok = false;
    el.hidden = !ok;
    if (ok) n++;
  });
  const c = $('#compte');
  c.textContent = n === 0 ? 'Aucune catégorie ne correspond'
    : n === 1 ? '1 catégorie' : n + ' catégories';
  $('#vide').hidden = n !== 0;
}

['#f-fam', '#f-ene', '#f-seg'].forEach(s => $(s).addEventListener('change', filtrer));
$('#f-q').addEventListener('input', filtrer);
$('#raz').addEventListener('click', () => {
  $('#f-fam').value = ''; $('#f-ene').value = '';
  $('#f-seg').value = ''; $('#f-q').value = '';
  filtrer();
});
filtrer();
"""


def e(s):
    return html.escape(str(s), quote=True)


def options(paires, vide):
    o = ['<option value="">%s</option>' % e(vide)]
    for code, nom in paires:
        o.append('<option value="%s">%s</option>' % (e(code), e(nom)))
    return ''.join(o)


def carte(cat):
    fam, ene, nom, segs, desc, champs = cat
    lfam = dict(D.FAMILLES)
    lene = dict(D.ENERGIES)
    lseg = dict(D.SEGMENTS)
    lch = dict(D.CHAMPS)

    tags = ''.join('<span>%s</span>' % e(lseg[s]) for s in segs)
    liste = ''.join('<li>%s</li>' % e(lch[k]) for k in champs)
    rech = ' '.join([nom, lfam[fam], lene[ene], desc]
                    + [lseg[s] for s in segs] + [lch[k] for k in champs])

    return (
      '<article class="o" data-fam="%s" data-ene="%s" data-seg="%s" data-rech="%s">'
      '<p class="ou"><span class="en en-%s">%s</span>'
      '<span class="fam">%s</span></p>'
      '<h3>%s</h3>'
      '<p class="d">%s</p>'
      '<p class="tags">%s</p>'
      '<div class="car"><b>Champs à renseigner sur la fiche</b><ul>%s</ul></div>'
      '</article>'
      % (e(fam), e(ene), e(' '.join(segs)), e(rech),
         e(ene), e(lene[ene]), e(lfam[fam]), e(nom), e(desc), tags, liste))


def page():
    css = (CSS.replace('__BG__', D.FOND).replace('__C__', D.CARTE)
              .replace('__L__', D.LIGNE).replace('__E__', D.ENCRE)
              .replace('__TX__', D.TEXTE).replace('__MU__', D.MUET)
              .replace('__AC__', D.ACCENT).replace('__ACD__', D.ACCENT_D))

    cartes = '\n'.join(carte(c) for c in D.CATEGORIES)
    fab = ''.join('<li><b>%s</b><span>%s</span></li>' % (e(a), e(b))
                  for a, b in D.FICHE_FABRICANT)
    chaine = ''.join('<li><b>%s</b><span>%s</span></li>' % (e(a), e(b))
                     for a, b in D.CHAINE)

    n_cat, n_fam = len(D.CATEGORIES), len(D.FAMILLES)
    n_ene, n_seg, n_ch = len(D.ENERGIES), len(D.SEGMENTS), len(D.CHAMPS)

    return """<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(m)s — %(t)s</title>
<meta name="description" content="Catalogue barbecue et matériel de cuisson : barbecues au gaz, au charbon et électriques, grils professionnels, fumoirs, planchas, fours, cuisine extérieure, accessoires, combustibles et pièces détachées. Filtrable par famille, par énergie et par segment.">
<meta name="robots" content="noindex,nofollow">
<style>%(css)s</style>
</head><body>

<div class="demo">Maquette de démonstration &mdash; <b>%(m)s</b> est un intitulé
provisoire. Aucun fabricant n&rsquo;est nommé et aucune valeur chiffrée ne
figure sur cette page.</div>

<header class="top"><div class="wrap tbar">
  <span class="logo">%(m)s</span>
  <nav>
    <a href="#catalogue">Catalogue</a>
    <a href="#fabricants">Fabricants</a>
    <a href="#chaine">Approvisionnement</a>
  </nav>
</div></header>

<section class="hero"><div class="wrap">
  <h1>Barbecue et matériel de cuisson, du jardin à la brasserie</h1>
  <p>Un seul catalogue. Barbecues au gaz, au charbon et électriques, grils
  professionnels, fumoirs, planchas, fours, cuisine extérieure, accessoires,
  combustibles et pièces détachées. Filtrez par famille, par énergie et par
  segment&nbsp;; chaque catégorie annonce les champs qui doivent figurer sur
  une fiche produit sérieuse.</p>
  <div class="kpi">
    <div><b>%(n)d</b><span>catégories</span></div>
    <div><b>%(nf)d</b><span>familles</span></div>
    <div><b>%(ne)d</b><span>énergies</span></div>
    <div><b>%(ns)d</b><span>segments</span></div>
    <div><b>%(nc)d</b><span>champs de fiche</span></div>
  </div>
</div></section>

<main class="wrap">

  <div id="catalogue"></div>

  <div class="filtres">
    <div class="f"><label for="f-fam">Famille</label>
      <select id="f-fam">%(ofam)s</select></div>
    <div class="f"><label for="f-ene">Énergie</label>
      <select id="f-ene">%(oene)s</select></div>
    <div class="f"><label for="f-seg">Segment</label>
      <select id="f-seg">%(oseg)s</select></div>
    <div class="f"><label for="f-q">Recherche</label>
      <input id="f-q" type="search" placeholder="fumoir, plancha, granulés, brûleur&hellip;"></div>
  </div>

  <div class="barre">
    <span class="compte" id="compte">%(n)d catégories</span>
    <button class="raz" id="raz" type="button">Tout afficher</button>
  </div>

  <div class="liste">
%(cartes)s
    <p class="vide" id="vide" hidden>Aucune catégorie ne correspond à ces
    critères. Élargissez la famille ou l&rsquo;énergie.</p>
  </div>

  <section class="bloc" id="fabricants"><h2>Ce qu&rsquo;une fiche fabricant doit contenir</h2>
  <p><strong>Aucun fabricant n&rsquo;est nommé sur cette page.</strong> Citer
  une marque sans accord de distribution est un problème juridique, et
  afficher des marques qu&rsquo;on ne distribue pas trompe l&rsquo;acheteur.
  Voici donc les cases à remplir&nbsp;; aucune n&rsquo;est remplie ici.</p>
  <ul class="ref">%(fab)s</ul></section>

  <section class="bloc" id="chaine"><h2>Approvisionnement et distribution</h2>
  <p>Les étapes, dans l&rsquo;ordre. Aucun délai, aucun volume, aucune
  quantité minimale&nbsp;: ces valeurs dépendent du fabricant retenu et du
  marché visé.</p>
  <ol class="chaine">%(chaine)s</ol></section>

  <div class="note" id="methode"><b>Comment lire ce catalogue</b>
  %(note)s</div>

  <div class="avert"><b>Ce que la page n&rsquo;affiche pas, volontairement</b>
  %(avert)s</div>

</main>

<footer><div class="wrap">%(m)s &mdash; maquette de démonstration. Les champs
listés sont des informations à renseigner, pas des valeurs mesurées.</div></footer>

<script>%(js)s</script>
</body></html>""" % {
        'm': e(D.MARQUE), 't': e(D.TITRE), 'css': css, 'js': JS,
        'n': n_cat, 'nf': n_fam, 'ne': n_ene, 'ns': n_seg, 'nc': n_ch,
        'ofam': options(D.FAMILLES, 'Toutes les familles'),
        'oene': options(D.ENERGIES, 'Toutes les énergies'),
        'oseg': options(D.SEGMENTS, 'Tous les segments'),
        'cartes': cartes, 'fab': fab, 'chaine': chaine,
        'note': e(D.NOTE), 'avert': e(D.AVERTISSEMENT),
    }


if __name__ == '__main__':
    verifier()
    with open(SORTIE, 'w', encoding='utf-8') as f:
        f.write(page())
    par_ene = {}
    for c in D.CATEGORIES:
        par_ene[c[1]] = par_ene.get(c[1], 0) + 1
    print('%d categories (%s), %d familles, %d segments, %d champs -> %s'
          % (len(D.CATEGORIES),
             ', '.join('%s %d' % (k, v) for k, v in par_ene.items()),
             len(D.FAMILLES), len(D.SEGMENTS), len(D.CHAMPS), SORTIE))
