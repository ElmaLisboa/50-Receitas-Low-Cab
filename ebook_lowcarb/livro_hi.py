# -*- coding: utf-8 -*-
"""Edição em hindi: रोज़ के लिए 50 लो-कार्ब रेसिपी."""
import html as H
import re
import livro as pt

# हिंदी não é produzida por substituição léxica: ordem SOV, postposições e
# unidades idiomáticas não sobrevivem a regex. Assim como a edição EN, tudo
# vem de duas tabelas revisadas à mão em hi_overrides:
#   INGREDIENTS : lista hindi (mesma ordem/comprimento das linhas PT) por receita;
#   OVERRIDES   : (passos, dica, troca) das 50 receitas.
# Qualquer linha faltante estoura o build em vez de vazar português.
from hi_overrides import INGREDIENTS, OVERRIDES

NAMES = [
 "पालक और चीज़ का बेक्ड ऑमलेट", "2 मिनट का माइक्रोवेव लो-कार्ब ब्रेड", "केले और ओट्स की पैनकेक (बिना आटे की)",
 "अंडा, सब्ज़ी और बेकन वाले नमकीन मफ़िन", "तवे की टैपिओका क्रेप — चीज़ और टमाटर के साथ", "तवे पर चीज़ ब्रेड",
 "कोलार्ड पत्तों में क्रीमी चिकन रैप", "एवोकाडो और बीजों वाले क्रीमी स्क्रैम्बल अंडे", "नट ग्रेनोला के साथ प्रोटीन योगर्ट",
 "सादा कॉलीफ़्लावर राइस", "होममेड टमाटर सॉस के साथ ज़ुकीनी नूडल्स", "लहसुन-तेल वाले पाम हार्ट नूडल्स",
 "योगर्ट ड्रेसिंग के साथ भरपूर चिकन सलाद", "नींबू मेयोनीज़ के साथ अंडे वाला ट्यूना सलाद", "मसालेदार कीमा, सलाद पत्तों में रैप",
 "श्रेडेड बीफ़ वाली कॉलीफ़्लावर शीपर्ड्स पाई", "बोलोनीज़ सॉस वाली बैंगन लसाना", "कीमे से भरा बैंगन",
 "लो-कार्ब हरा सूप (बिना आलू)", "कोकोनट मिल्क और अदरक वाला कद्दू सूप", "श्रेडेड चिकन वाली सब्ज़ियों का सूप",
 "क्रीम चीज़ वाली ज़ुकीनी क्रीम सूप", "सरसों-क्रीम सॉस में ग्रिल्ड चिकन", "नींबू और रोज़मेरी से भुनी चिकन थाई",
 "लो-कार्ब चिकन स्टिर-फ्राई", "मशरूम सॉस वाला स्टेक", "टमाटर-ज़ुकीनी के साथ कीमा",
 "प्याज़ और लहसुन-मक्खन वाला स्टेक", "चीज़ भरे मीटबॉल, टमाटर सॉस में", "पुल्ड पॉर्क रिब्स",
 "नींबू मक्खन में भुना सैल्मन", "बादाम के आटे की कोटिंग वाली तिलापिया", "लहसुन वाले झींगे",
 "कॉलीफ़्लावर और जैतून के साथ कॉड मछली", "कोकोनट मिल्क-पाम हार्ट वाली फ़िश मोकेका", "नींबू-जड़ी-बूटियों से ग्रिल्ड कैलामारी",
 "कॉलीफ़्लावर क्रस्ट, मोत्ज़ारेला और बेसिल वाली पिज़्ज़ा", "बिना कोटिंग वाली बैंगन परमेज़न", "लो-कार्ब फ़ेजोआडा (बिना फलियों के)",
 "एयरफ्रायर चीज़ ब्रेड", "ट्यूना और क्रीम चीज़ से भरी ज़ुकीनी", "लो-कार्ब सुशी (खीरे के रोल)",
 "कीमे भरे पत्तागोभी रोल", "एवोकाडो चॉकलेट मूस", "एरिथ्रिटल वाला नारियल फ्लैन",
 "चम्मच से खाने वाली लो-कार्ब चॉकलेट क्रीम", "बेरी लो-कार्ब चीज़केक", "नट और चॉकलेट वाले लो-कार्ब कुकीज़",
 "नारियल तेल वाली चॉकलेट ट्रफ़ल्स", "लो-कार्ब मूंगफली चिक्की (पाकोका स्टाइल)"
]

CAT = {
 "Café da manhã e lanches rápidos": ("नाश्ता और झटपट स्नैक्स", "भरोसेमंद और पेट भरने वाली रेसिपी से दिन की शुरुआत कीजिए — पारंपरिक ब्रेड पर निर्भर रहने की ज़रूरत नहीं। इस अध्याय में अंडे, चीज़, बादाम या नारियल का आटा और फल संतुलित मात्रा में हैं। ज़्यादातर रेसिपी में सक्रिय तैयारी 15 मिनट से कम लगती है।"),
 "Almoços completos": ("भरपूर दोपहर का खाना", "एक ही बर्तन वाले व्यंजन, दोपहर भर पेट भरे रखने वाले सलाद, और चावल-पास्ता के स्मार्ट विकल्प — डाइट फ़ूड जैसा स्वाद कहीं नहीं।"),
 "Sopas e caldos": ("सूप और शोरबे", "ठंडी शामों और लंच बॉक्स के लिए: आलू और गेहूँ के आटे के बिना भी गाढ़ा, मलाईदार स्वाद।"),
 "Carnes e aves": ("मांस और मुर्गे", "अच्छे लो-कार्ब मेन्यू की नींव प्रोटीन है: भूरा, रसदार, और असली सॉस के साथ — सूखा टिफ़िन चिकन नहीं।"),
 "Peixes e frutos do mar": ("मछली और समुद्री भोजन", "रविवार के सैल्मन से लेकर सोमवार की झटपट मछली तक: अच्छी चर्बी, कम समय, रेस्तराँ वाला स्वाद।"),
 "Jantares em até 30 minutos de bancada": ("30 मिनट में रात का खाना", "रात का नियम: सीरीज़ का एपिसोड खत्म होने से पहले डिनर तैयार। एक तवा, एक बेकिंग ट्रे या एयरफ्रायर वाली रेसिपी।"),
 "Sobremesas sem açúcar": ("बिना चीनी की मिठाइयाँ", "असली मिठाई के लिए रिफ़ाइंड चीनी ज़रूरी नहीं: कोको, नारियल, मेवे और ऐसे मिठासक जो ज़ुबान को धोखा न दें।"),
}

CSS = (pt.CSS
 .replace("50 Receitas Low Carb para o Dia a Dia", "रोज़ के लिए 50 लो-कार्ब रेसिपी")
 .replace("'DejaVu Serif'", "'Noto Serif Devanagari'")
 .replace("'DejaVu Sans'", "'Noto Sans Devanagari'")
 + "\n@page{margin-bottom:6mm}.dica{padding:2.6mm 3.2mm;margin-top:1.8mm;font-size:7.8pt}.troca{padding:1.2mm 3.2mm;margin-top:1.2mm;font-size:7.4pt;line-height:1.42}")

FRONT = """
<section class="frente legal"><h2>क्रेडिट और कानूनी सूचना</h2><div class="filete"></div>
<p><b>रोज़ के लिए 50 लो-कार्ब रेसिपी</b> — पहला संस्करण, 2026।<br>प्रैक्टिकल किचन सीरीज़ · खंड 1।</p>
<p>सर्वाधिकार सुरक्षित। लिखित अनुमति के बिना इस सामग्री का कोई भी हिस्सा दोबारा नहीं बनाया जा सकता। यह ई-बुक खरीददार के लिए डिजिटल उत्पाद है: केवल आधिकारिक बिक्री लिंक साझा कीजिए।</p>
<div class="quadro"><b>ज़रूरी सूचना:</b> पोषण जानकारी (कैलोरी, कार्बोहाइड्रेट, प्रोटीन और वसा) सामग्री सूची और खाद्य-संरचना तालिकाओं से निकाला गया <b>प्रति सर्विंग अनुमान</b> है। ब्रांड, सामग्री के आकार और बर्तन के अनुसार बदलाव होता है। यह पुस्तक शैक्षिक है और डॉक्टर या रजिस्टर्ड डायटीशियन की सलाह का विकल्प <b>नहीं</b> है। मधुमेह, गुर्दे की बीमारी वाले लोग, गर्भवती या स्तनपान कराने वाली महिलाएँ और नियमित दवा लेने वाले लोग कम कार्बोहाइड्रेट वाले खान-पान से पहले विशेषज्ञ से सलाह लें। एरिथ्रिटल और ज़िलिटोल मध्यम मात्रा में ज़्यादातर लोगों के लिए सुरक्षित हैं; ज़्यादा मात्रा में पेट की दिक्कत कर सकते हैं। ज़िलिटल कुत्तों के लिए ज़हरीला है — मिठाइयाँ पालतू जानवरों की पहुँच से दूर रखिए।</div>
<p><b>इस पुस्तक में प्रयुक्त माप:</b> 1 कप = 240 ml · 1 बड़ा चम्मच = 15 ml · 1 छोटा चम्मच = 5 ml · बिना बताए ओवन हमेशा पहले से गरम कीजिए।</p>
<p class="legal">लेआउट और चित्रांकन तस्वीरें संपादकीय उद्देश्य से बनाई गई हैं।</p></section>
<section class="frente"><h2>आपकी लो-कार्ब रसोई में स्वागत है</h2><div class="filete"></div>
<p>आपने डाइट की किताब नहीं खरीदी। आपने उस सवाल के <b>50 तैयार जवाब</b> खरीदे हैं जो किसी भी खाने की आदत को बिगाड़ सकता है: <i>“आज खाने में क्या बनाऊँ?”</i></p>
<p>लो-कार्ब का मतलब उदास सलाद खाना नहीं है। इसका मतलब है मलाईदार ऑमलेट, टुकड़ों में कटने वाली लसाना, रविवार की फ़ेजोआडा और यहाँ तक कि चीज़केक का मज़ा — रिफ़ाइंड आटे और चीनी की जगह ऐसी सामग्री जो पेट भरे, बिना दो-दो बार खाना बनाए (एक आपके लिए, दूसरा परिवार के लिए)।</p>
<p>यहाँ की हर रेसिपी तीन वजहों से चुनी गई है: <b>मोहल्ले की दुकान में मिलने वाली सामग्री</b> (कुछ भी ऐसा नहीं जो सिर्फ़ इम्पोर्ट स्टोर में मिले), <b>नौकरी करने वाले इंसान का असली समय</b> (ज़्यादातर 30 मिनट में तैयार) और <b>ऐसी बची हुई चीज़ जो कल का खाना हल कर दे</b>।</p>
<div class="quadro"><b>इस पुस्तक का सुनहरा नियम:</b> कार्बोहाइड्रेट मसाला है, नींव नहीं। वह स्वाद और रंग लाने आता है — टमाटर, गाजर, फल — कभी भी प्लेट की बुनियाद नहीं बनने के लिए। बुनियाद हमेशा प्रोटीन + अच्छी चर्बी + सब्ज़ी।</div>
<p>सात हफ़्ते तक हर दिन एक नई रेसिपी बनाइए और आपके पास ऐसा रिपर्टॉयर होगा जिसे कोई भी सोमवार बिगाड़ नहीं सकता। स्वाद लीजिए।</p></section>
<section class="frente"><h2>इस पुस्तक का व्यावहारिक इस्तेमाल</h2><div class="filete"></div>
<p><b>1. अंत से शुरू कीजिए।</b> बाज़ार जाने से पहले “7-दिन का मेन्यू” बोनस और खरीदारी की सूची देख लीजिए। बिना योजना खाना बनाना गुरुवार को ऑर्डर करने का सबसे तेज़ रास्ता है।</p>
<p><b>2. सही रेसिपी दोगुनी बनाइए।</b> ज़्यादातर दोपहर और रात की रेसिपी दो सर्विंग की होती हैं: दूसरी सर्विंग कल के दोपहर के खाने में बदल जाती है।</p>
<p><b>3. डिब्बों का इस्तेमाल कीजिए।</b> हर रेसिपी में <b>पाक सुझाव</b> और <b>स्मार्ट बदलाव</b> है — लो-कार्ब रास्ता छोड़े बिना ढालने के लिए।</p>
<p><b>4. ज़ीरो कार्ब का पीछा मत कीजिए।</b> पोषण आँकड़े चुनाव में मदद के लिए हैं, खाने को जेल बनाने के लिए नहीं।</p>
<p><b>5. बेझिझक फ़्रीज़ कीजिए।</b> फ़्रीज़िंग नोट वाली रेसिपी अलग-अलग सर्विंग और सीलबंद डिब्बों के लिए बनी हैं।</p></section>
<section class="frente"><h2>वे बदलाव जो हर रसोई बचाते हैं</h2><div class="filete"></div>
<p>लो-कार्ब स्मार्ट बदलों का ही खेल है। यह तालिका हमेशा पास रखिए:</p>
<table>
<tr><th>हटाइए</th><th>इसकी जगह</th><th>नोट</th></tr>
<tr><td>रिफ़ाइंड चीनी</td><td><b>एरिथ्रिटल या ज़िलिटोल</b></td><td>1:1; ज़िलिटोल थोड़ा ज़्यादा मीठा</td></tr>
<tr><td>गेहूँ का आटा</td><td><b>बादाम का आटा + 1 अंडा</b></td><td>आधी मात्रा; अंडा बाँधने का काम करता है</td></tr>
<tr><td>सफ़ेद चावल</td><td><b>कॉलीफ़्लावर राइस</b></td><td>कच्चा, तेज़ आँच पर 5–6 मिनट भूनिए</td></tr>
<tr><td>पास्ता</td><td><b>ज़ुकीनी, पाम हार्ट या कोन्जैक</b></td><td>90 सेकंड से 3 मिनट तक भूनिए</td></tr>
<tr><td>आलू</td><td><b>कॉलीफ़्लावर, शलगम या भुना मूली</b></td><td>प्यूरी और शोरबे के लिए; कद्दू कम ही</td></tr>
<tr><td>पहले से बना सॉस</td><td><b>छिले टमाटर + मसाले</b></td><td>धीमी आँच पर 20 मिनट</td></tr>
<tr><td>साधारण सोया सॉस</td><td><b>कम सोडियम वाला सोया सॉस या तमारी</b></td><td>हर बड़े चम्मच पर 1 g कार्ब गिनिए</td></tr>
</table>
<h2 style="margin-top:6mm">रसोई के ज़रूरी सामान: एक बार खरीदिए, पूरे हफ़्ते चलेगा</h2>
<div class="lista2"><ul>
<li>बादाम का आटा और बिना चीनी का नारियल चूरा</li>
<li>एरिथ्रिटल / ज़िलिटोल और 100% कोको</li>
<li>बिना चीनी का नारियल दूध और क्रीम</li>
<li>जैतून का तेल, नारियल तेल और मक्खन</li>
<li>अंडे (हफ़्ते में कम से कम 1 दर्जन) और चीज़: मोत्ज़ारेला, परमेज़न, क्रीम चीज़</li>
<li>ताज़ा क्रीम और क्रीम चीज़</li>
<li>कॉलीफ़्लावर, ज़ुकीनी, बैंगन, पत्तागोभी और हरी पत्तियाँ</li>
<li>टिन वाले छिले टमाटर और जैतून</li>
<li>चिकन, कीमा, अंडे, मछली और टिन वाला ट्यूना</li>
<li>मेवे: ब्राज़ील नट, काजू, बादाम और मूंगफली</li>
<li>लहसुन, प्याज़, नींबू, ताज़ी जड़ी-बूटियाँ और धुआँ वाली पेपरिका</li>
<li>चिया बीज और सुनहरा अलसी पाउडर</li>
</ul></div></section>
"""

BONUS = """
<section class="frente"><h2>बोनस 1 — 7-दिन का मेन्यू (रेसिपी नंबर सहित)</h2><div class="filete"></div>
<p>पहले हफ़्ते का असली प्लान: भरपूर नाश्ता, ऐसा दोपहर का खाना जो रात के खाने में बदल जाए, और सही जगह पर मीठा। नंबर इसी पुस्तक की रेसिपी के हैं।</p>
<table>
<tr><th>दिन</th><th>नाश्ता</th><th>दोपहर</th><th>स्नैक</th><th>रात</th></tr>
<tr><td class="dia">सोम</td><td>01 · बेक्ड ऑमलेट</td><td>10 + 23 · कॉलीफ़्लावर राइस, चिकन के साथ</td><td>09 · योगर्ट ग्रेनोला</td><td>37 · कॉलीफ़्लावर पिज़्ज़ा</td></tr>
<tr><td class="dia">मंगल</td><td>05 · टैपिओका क्रेप</td><td>17 · बैंगन लसाना</td><td>06 · चीज़ ब्रेड</td><td>31 · सैल्मन + 44 · मूस</td></tr>
<tr><td class="dia">बुध</td><td>02 · माइक्रोवेव ब्रेड</td><td>11 · ज़ुकीनी नूडल्स</td><td>45 · नारियल फ्लैन</td><td>35 · फ़िश मोकेका</td></tr>
<tr><td class="dia">गुरु</td><td>07 · कोलार्ड रैप</td><td>13 · भरपूर चिकन सलाद</td><td>08 · एवोकाडो अंडे</td><td>26 · मशरूम स्टेक</td></tr>
<tr><td class="dia">शुक्र</td><td>03 · केले की पैनकेक</td><td>16 · शीपर्ड्स पाई</td><td>09 · योगर्ट ग्रेनोला</td><td>33 · लहसुन झींगे</td></tr>
<tr><td class="dia">शनि</td><td>04 · नमकीन मफ़िन</td><td>18 · भरा बैंगन</td><td>46 · चॉकलेट क्रीम</td><td>42 · लो-कार्ब सुशी</td></tr>
<tr><td class="dia">रवि</td><td>06 · चीज़ ब्रेड</td><td>30 · पुल्ड पॉर्क रिब्स</td><td>47 · चीज़केक</td><td>19 · हरा सूप + 28 · स्टेक</td></tr>
</table>
<p class="legal">सर्विंग अपनी ज़रूरत के हिसाब से तय कीजिए। यह मेन्यू शैक्षिक सुझाव है, नुस्खा नहीं।</p></section>
<section class="frente"><h2>बोनस 2 — पहले हफ़्ते की खरीदारी</h2><div class="filete"></div>
<p>इसे प्रिंट करके बाज़ार ले जाइए। दो लोगों के लिए बनाया गया है:</p>
<div class="lista2"><ul class="check">
<li>2 दर्जन अंडे</li><li>1 kg चिकन ब्रेस्ट + 8 जांघें</li>
<li>1 kg कीमा + 500 g स्टेक</li><li>600 g सैल्मन या मज़बूत मछली + 400 g झींगे</li>
<li>2 टिन ट्यूना</li><li>500 g मोत्ज़ारेला + परमेज़न + क्रीम चीज़</li>
<li>भारी क्रीम</li><li>2 डिब्बे बिना चीनी का नारियल दूध</li>
<li>कॉलीफ़्लावर, ज़ुकीनी, बैंगन, पत्तागोभी और हरी पत्तियाँ</li><li>ताज़े टमाटर + 2 टिन छिले टमाटर</li>
<li>एवोकाडो, पके केले, स्ट्रॉबेरी और नींबू</li><li>प्याज़, लहसुन, अदरक, जड़ी-बूटियाँ, धुआँ पेपरिका</li>
<li>जैतून, पाम हार्ट, मेवे और मूंगफली</li><li>बादाम का आटा, नारियल चूरा और चिया</li>
<li>एरिथ्रिटल/ज़िलिटोल, 100% कोको और 85% चॉकलेट</li><li>जैतून का तेल, मक्खन और नारियल तेल</li>
<li>कम सोडियम वाला सोया सॉस, सरसों और धुआँ पेपरिका</li>
</ul></div>
<div class="quadro"><b>खरीदारी का नियम:</b> पहले ताज़ा सब्ज़ी और मीट काउंटर घूबाइए; पैकेज्ड चीज़ें आख़िर में और हमेशा लेबल जाँचिए — हर सर्विंग में 5 g से कम कार्ब हो।</div></section>
<section class="frente"><h2>रसोई बंद करने से पहले</h2><div class="filete"></div>
<p>अब आपके पास असली ज़िंदगी के लिए बनी 50 रेसिपी हैं: आसानी से मिलने वाली सामग्री, एक ही बर्तन के तरीके और प्लान की हुई बची हुई चीज़। इस ई-बुक और ज़्यादा व्यवस्थित हफ़्ते के बीच फ़र्क़ एक छोटे फ़ैसले का है: <b>आपका अगला खाना</b>।</p>
<p>आज रात के लिए एक रेसिपी चुनिए, बनाइए और किसी के साथ बाँटिए। साथ खाया हुआ खाना दोबारा बनाना आसान होता है।</p>
<div class="quadro"><b>प्रैक्टिकल किचन सीरीज़ के आगे के खंड:</b> खंड 2 — <i>पूरे हफ़्ते के लो-कार्ब खाने</i> · खंड 3 — <i>त्योहारों की बिना चीनी मिठाइयाँ</i>।</div></section>
"""

COVER = """<section class="capa"><div class="txt"><div class="kicker">प्रैक्टिकल किचन सीरीज़ · खंड 1</div><h1>50 रेसिपी<br><span class="hl">लो-कार्ब</span></h1><div class="sub">रोज़ के लिए — न आटा, न चीनी, न कोई समझौता</div></div><div class="faixa"><span class="marca">प्रैक्टिकल किचन</span><span>कम कार्ब, ज़्यादा असली ज़िंदगी</span></div></section>"""
BACK = """<section class="contra"><div class="in"><h2>हर सोमवार डाइट फिर शुरू करना बंद कीजिए।</h2><p>यह पुस्तक दो-दो बार खाना बनाए बिना लो-कार्ब रहने की 50 रेसिपी लाती है: सुबह को संभालने वाला नाश्ता, रात में बदल जाने वाला दोपहर का खाना, ठंडी रातों के सूप और बिना माफ़ी माँगे खाई जाने वाली मिठाइयाँ।</p><ul><li><b>50 पूरी रेसिपी</b> — समय, मात्रा और प्रति सर्विंग अनुमानित मैक्रो के साथ;</li><li>हर रेसिपी में <b>पाक सुझाव</b> — वही गलती जो प्लेट बिगाड़ देती है और उससे बचने का तरीक़ा;</li><li>बिना डाइट छोड़े ढालने के लिए <b>स्मार्ट बदलाव</b>;</li><li><b>7-दिन का मेन्यू</b> + प्रिंट करने लायक खरीदारी सूची;</li><li>आटा, चीनी, चावल और पास्ता की <b>बदलाव तालिका</b>।</li></ul><p>मोहल्ले की दुकान वाली सामग्री। काम करने वाले इंसान का समय। ऐसा स्वाद जिसे देखकर न लगे कि कोई “डाइट पर” है।</p><div class="marca">प्रैक्टिकल किचन</div></div></section>"""

def ingredient(num, i, pt_line):
    lines = INGREDIENTS.get(num)
    if lines is None:
        raise KeyError("receita %d sem ingredientes em hindi (hi_overrides.INGREDIENTS)" % num)
    if i >= len(lines) or not lines[i]:
        raise KeyError("receita %d: ingrediente %d em hindi ausente — PT: %r" % (num, i + 1, pt_line))
    return lines[i]

def override(num):
    if num not in OVERRIDES:
        raise KeyError("receita %d sem texto em hindi (hi_overrides.OVERRIDES)" % num)
    return OVERRIDES[num]

PT_TO_HI = {r["d"][0]: NAMES[r["num"] - 1] for r in pt.RECEITAS}
RECIPES = []
for r in pt.RECEITAS:
    d = r["d"]
    name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    hi_ings = [ingredient(r["num"], i, x) for i, x in enumerate(ingredients)]
    passos, dica, troca = override(r["num"])
    assert len(passos) == len(steps), "receita %d: %d passos em hindi para %d em português" % (r["num"], len(passos), len(steps))
    RECIPES.append({"num": r["num"], "id": r["id"], "cat": CAT[r["cat"]][0],
                    "d": (PT_TO_HI[name], prep, total, servings, kcal, carbs, protein, fat,
                          hi_ings, passos, dica, troca)})

SELECTION = []
for cat_pt, intro_pt, names in pt.SELECAO:
    cat_hi, intro_hi = CAT[cat_pt]
    SELECTION.append((cat_hi, intro_hi, [PT_TO_HI[n] for n in names]))

def recipe_html(r):
    num, rid, d = r["num"], r["id"], r["d"]
    name, prep, total, servings, kcal, carbs, protein, fat, ingredients, steps, tip, swap = d
    ing = "".join("<li>%s</li>" % H.escape(x) for x in ingredients)
    pas = "".join("<li>%s</li>" % H.escape(x) for x in steps)
    return """<section class="receita" id="%s"><header><div class="num">%02d</div><div class="titulo"><h3>%s</h3></div></header><img class="foto" src="imagens/receita-%02d.jpg" alt="%s"><div class="meta"><span><b>तैयारी</b> %d मिनट</span><span><b>कुल</b> %d मिनट</span><span><b>सर्विंग</b> %s</span><span><b>कठिनाई</b> आसान</span></div><div class="nutris"><span><b>%d</b> kcal / सर्विंग</span><span><b>%d g</b> कार्ब्स</span><span><b>%d g</b> प्रोटीन</span><span><b>%d g</b> वसा</span></div><div class="corpo"><div><h4>सामग्री</h4><ul class="ing">%s</ul></div><div><h4>विधि</h4><ol class="passos">%s</ol></div></div><div class="dica"><b>पाक सुझाव:</b> %s</div><div class="troca"><b>↺ स्मार्ट बदलाव:</b> %s</div></section>""" % (rid, num, H.escape(name), num, H.escape(name), prep, total, H.escape(str(servings)), kcal, carbs, protein, fat, ing, pas, H.escape(tip), H.escape(swap))

def toc_html(pmap=None):
    out = ['<section class="frente"><h2>अनुक्रमणिका</h2><div class="filete"></div><div class="sum"><table>']; idx = 0
    for cat, intro, names in SELECTION:
        out.append('<tr><td class="cat" colspan="4">%s</td></tr>' % H.escape(cat))
        for name in names:
            idx += 1; pg = str(pmap[idx]) if pmap else ""
            out.append('<tr><td class="num">%02d</td><td><a href="#r%02d">%s</a></td><td class="dots"></td><td class="pg">%s</td></tr>' % (idx, idx, H.escape(name), pg))
    out.append('</table></div></section>'); return ''.join(out)

def body_html():
    out = []
    for chapter, (cat, intro, names) in enumerate(SELECTION, 1):
        out.append('<section class="abre"><img class="capfoto" src="imagens/capitulo-%02d.jpg" alt="%s अध्याय की तस्वीर"><div class="tag">अध्याय %02d</div><h2>%s</h2><div class="filete"></div><p>%s</p></section>' % (chapter, H.escape(cat), chapter, H.escape(cat), H.escape(intro)))
        for r in RECIPES:
            if r["cat"] == cat: out.append(recipe_html(r))
    return ''.join(out)

def render(pmap=None):
    return "<!DOCTYPE html><html lang='hi'><head><meta charset='utf-8'><style>%s</style></head><body>%s%s%s%s%s%s</body></html>" % (CSS, COVER, FRONT, toc_html(pmap), body_html(), BONUS, BACK)

def build():
    from weasyprint import HTML
    import fitz
    open('ebook_hi_probe.html', 'w').write(render(None)); HTML(filename='ebook_hi_probe.html').write_pdf('ebook_hi_probe.pdf')
    d = fitz.open('ebook_hi_probe.pdf'); pmap = {}
    for i in range(d.page_count):
        text = d[i].get_text(); norm = text.replace(' ', '')
        if 'सामग्री' in norm and 'विधि' in norm:
            m = re.search(r'(?m)^(\d{2})\n', text)
            if m and 1 <= int(m.group(1)) <= 50: pmap[int(m.group(1))] = i + 1
    assert len(pmap) == 50, (len(pmap), sorted(set(range(1, 51)) - set(pmap)))
    open('50-लो-कार्ब-रेसिपी-hi.html', 'w').write(render(pmap)); HTML(filename='50-लो-कार्ब-रेसिपी-hi.html').write_pdf('50-लो-कार्ब-रेसिपी-hi.pdf')
    print('हिंदी PDF तैयार:', len(pmap), 'रेसिपी')

if __name__ == '__main__':
    build()
