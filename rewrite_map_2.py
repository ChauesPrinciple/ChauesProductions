import re

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_js = """        const I = {
            tokyo_arrive: 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=600&q=80',
            tokyo_night: 'https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=600&q=80',
            tokyo_street: 'https://images.unsplash.com/photo-1513407030348-c983a97b98d8?w=600&q=80',
            racing: 'https://images.unsplash.com/photo-1504215680853-026ed2a45def?w=600&q=80',
            shinkansen: 'https://images.unsplash.com/photo-1553342385-111fd6bc6ab3?w=600&q=80',
            morioka: 'https://images.unsplash.com/photo-1528360983277-13d401cdc186?w=600&q=80',
            nebuta: 'https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?w=600&q=80',
            castle: 'https://images.unsplash.com/photo-1493780474015-ba834fd0ce2f?w=600&q=80',
            coast: 'https://images.unsplash.com/photo-1492571350019-22de08371fd3?w=600&q=80',
            fireworks: 'https://images.unsplash.com/photo-1594029242614-66a0e86acb97?w=600&q=80',
            hokkaido: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80',
            sapporo: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80',
            otaru: 'https://images.unsplash.com/photo-1476514525035-f6c0fd5bab88?w=600&q=80',
            vintage: 'https://images.unsplash.com/photo-1535016120720-40c646be5580?w=600&q=80',
        };

        const SECTIONS = [
            {
                label: 'TOKYO : OPENING', days: [
                    {
                        n: 1, date: 'Thu Jul 31', loc: 'Tokyo', emoji: '✈️', type: 'arrival',
                        title: 'Arrive Tokyo', img: I.tokyo_arrive,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Land Haneda or Narita: check in to Sequence Miyashita Park, Shibuya',
                            'Welcome lunch: Udatsu Sushi \u26a0\ufe0f confirm group capacity',
                            'Easy evening: ramen, Kabukicho or Shibuya Crossing',
                            'Get on Japan time by walking, not sleeping'
                        ],
                        prose: `<p class="prose-p">Landing in Tokyo is always a calibration. The city runs at a frequency you haven't encountered, and the first twelve hours don't align with anything. We check into <strong>Sequence Miyashita Park</strong> in Shibuya. The hotel sits directly above Miyashita Park and puts you inside the culture rather than across the street from it. Shibuya is home base for the opening days.</p><p class="prose-p">We open at <strong>Udatsu</strong> for counter omakase with Chef Toru Udatsu, one of Tokyo's serious sushiya. You sit, you eat what appears, and you stop trying to frame it. The evening is deliberately loose. Shibuya Crossing at dusk is not a tourist gesture; it is a functional portrait of organized mass. Get on Japan time by moving, not sleeping. Join us on this adventure and go places you would never go on your own.</p>`
                    },
                    {
                        n: 2, date: 'Fri Aug 1', loc: 'Tokyo', emoji: '🎭', type: 'partner',
                        title: 'TeamLab, BunBun, Shibuya Sky', img: I.tokyo_night,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Morning: TeamLab (book timed entry in advance)',
                            'Optional: Kimono dressing/sale with local business partner',
                            'Midday to afternoon: Tokyo BunBun acting partner',
                            'Evening: Shibuya Sky night viewing (Scramble Square rooftop)'
                        ],
                        prose: `<p class="prose-p"><strong>TeamLab</strong> opens the day. It is a full-body immersive installation art environment where the boundary between viewer and image dissolves entirely. You must book timed entry ahead because it sells out. We also feature an optional stop for <strong>kimono dressing</strong> with a local business. This is a working engagement with our expert partners, not a tourist photo op.</p><p class="prose-p"><strong>BunBun</strong> operates in the register where language stops being useful. It is physical, present, and without the scaffolding of shared vocabulary. Acting in a foreign country strips everything to the body. The whole group enters this one with no half-measures and no parallel scheduling.</p><p class="prose-p">The night closes at <strong>Shibuya Sky</strong>, the rooftop observation deck on Scramble Square 230 meters above the crossing. Tokyo at night from that altitude is the city making its full argument. You must book in advance. The unobstructed glass floor looks straight down onto Shibuya Crossing.</p>`
                    },
                    {
                        n: 3, date: 'Sat Aug 2', loc: 'Tokyo', emoji: '🏎️', type: 'partner',
                        title: 'Bonsai Racing (Confirmed Partner)', img: I.racing,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Full day with Bonsai Racing partner',
                            'Evening at leisure in Tokyo'
                        ],
                        prose: `<p class="prose-p">Racing has a visual grammar of focal length, spatial compression, and the problem of representing speed in a fixed frame. Bonsai Racing is the Japanese execution of it. They are a confirmed expert production partner not because a box was checked, but because what happens there produces material worth keeping.</p><p class="prose-p">This is a full day properly scheduled into the trip architecture. What gets documented here is part of the project. Join an adventure driven filmmaker on a once in a lifetime trip to capture these moments.</p>`
                    }
                ]
            },
            {
                label: 'JOURNEY NORTH', days: [
                    {
                        n: 4, date: 'Sun Aug 3', loc: 'Morioka', emoji: '🥁', type: 'travel',
                        title: 'Tokyo to Morioka, Sansa Festival', img: I.shinkansen,
                        lat: 39.7014, lng: 141.1349, zoom: 13, city: 'morioka',
                        events: [
                            'Tohoku Shinkansen ~2h20m: reserve group block (JR Pass)',
                            '\u26a0\ufe0f Possible stop: Ebisu brewery in Fukushima (user to confirm)',
                            'Kitakami River walk: Mt. Iwate over the city',
                            'Azumaya: wanko soba until you tap out',
                            'Nagasawa Coffee or Clammbon',
                            'EVENING: Morioka Sansa Festival'
                        ],
                        prose: `<p class="prose-p">The Tohoku Shinkansen runs northeast. Within two hours the Tokyo skyline dissolves entirely into cedar ridges and terraced fieldwork. There is a potential stop at an <strong>Ebisu</strong> site in Fukushima depending on timing, but the ultimate destination today is <strong>Morioka</strong>. The NYT ranked Morioka as the #2 of 52 Places on Earth in 2023. This is not because it was constructed for tourism, but because it is compact, real, and still functions primarily for the people who live there.</p><p class="prose-p">The <strong>Sansa Festival</strong> is the reason we stop here tonight. It is the world's largest taiko drum procession featuring 10,000 performers moving through the streets. At the close of the night the procession opens to anyone who wants to join it. Walk into it.</p>`
                    },
                    {
                        n: 5, date: 'Mon Aug 4', loc: 'Aomori', emoji: '🎏', type: 'travel',
                        title: 'Morioka to Aomori, Nebuta Night 3', img: I.nebuta,
                        lat: 40.8244, lng: 140.7400, zoom: 13, city: 'aomori',
                        events: [
                            'Shinkansen Morioka to Aomori ~1hr (JR Pass)',
                            'Check in: first parade night, arrive with energy',
                            'A-FACTORY waterfront: apple cider, bay views',
                            'Rassera Land: floats up close at builder huts',
                            '6:45pm: Nebuta Night 3',
                            'Haneto costume (join the procession)'
                        ],
                        prose: `<p class="prose-p">One more hour north and the shinkansen arrives in Aomori at the northern terminus of Honshu. The city has built its entire civic identity around this festival. The <strong>nebuta</strong> are warrior-figure lantern floats the size of shipping containers. They are internally wired and pulled through streets on wheeled platforms while Haneto dancers circle and the crowd chants <strong>Rassera</strong>.</p><p class="prose-p">Tonight is the first parade night for the group. Rent the costume and get into the procession. The Haneto dance is not performative tourism; it is the participation structure the festival was designed around. You are supposed to be in it.</p>`
                    }
                ]
            },
            {
                label: 'AOMORI, NEBUTA FESTIVAL', days: [
                    {
                        n: 6, date: 'Tue Aug 5', loc: 'Aomori', emoji: '🍣', type: 'cultural',
                        title: 'Aomori Cultural Day, Nebuta Night 4', img: I.nebuta,
                        lat: 40.8244, lng: 140.7400, zoom: 13, city: 'aomori',
                        events: [
                            '7am: Nokke-don at Furukawa Market',
                            'Nebuta no Ie Wa Rasse: float museum, costume try-on',
                            'Aomori Museum of Art: Yoshitomo Nara\u0027s Aomori Dog',
                            'Sannai-Maruyama Jomon Site (UNESCO, bus ~20min)',
                            '6:45pm: Nebuta Night 4'
                        ],
                        prose: `<p class="prose-p"><strong>Furukawa Market</strong> opens before dawn for fishing families. By 7am the Nokke-don stalls are running. You buy a bowl of rice and choose toppings from whatever came off the boats this morning, including sea urchin, salmon roe, scallop, and squid. It is one of the most direct eating experiences in Japan.</p><p class="prose-p"><strong>Wa Rasse</strong> is one of the only places you can read a nebuta float at close range to see the internal wire armature, the layered washi paper, and the engineering of light distribution. <strong>Sannai-Maruyama</strong> is a Jomon settlement 5,500 years old sitting adjacent to the city. It is mostly unvisited, UNESCO-listed, and genuinely worth the bus ride. The parade begins again at 6:45 pm.</p>`
                    },
                    {
                        n: 7, date: 'Wed Aug 6', loc: 'Hirosaki / Goshogawara', emoji: '🔴', type: 'festival',
                        title: 'Hirosaki to Goshogawara, Tachineputa Overnight', img: I.castle,
                        lat: 40.8065, lng: 140.4390, zoom: 13, city: 'goshogawara',
                        events: [
                            'Morning: Hirosaki Castle (Edo original) and MOCA',
                            'Gono Line to Goshogawara (~40min from Hirosaki)',
                            'Tachineputa no Yakata: 23m giants year-round',
                            '19:00 to 21:00: Goshogawara Tachineputa',
                            'Floats 23m tall, 19 tons: stand at corners for the pivot',
                            '\u26a0\ufe0f Overnight: last train to Aomori departs 19:33'
                        ],
                        prose: `<p class="prose-p"><strong>Hirosaki Castle</strong> is one of twelve original Edo-period fortresses still standing in Japan. The rest burned or were demolished in the Meiji modernization. The MOCA occupies a converted sake brewery and takes its programming seriously. Both are worth the morning, but we remain in transit.</p><p class="prose-p">The afternoon Gono Line carries us west across the Tsugaru plains to <strong>Goshogawara</strong>, where the Tachineputa floats stand 23 meters tall and weigh 19 tons each. They navigate streets that were designed for none of that. The best position is a corner of the parade route. Watch the rope teams heave, the float tilt, and 19 tons pivot through an alley. The chant is <strong>Yattemare</strong>. We sleep here tonight because there is no train back to Aomori after the parade starts.</p>`
                    },
                    {
                        n: 8, date: 'Thu Aug 7', loc: 'Hachinohe', emoji: '🦅', type: 'festival',
                        title: 'Hachinohe Coast, Nebuta Award Night', img: I.coast,
                        lat: 40.5122, lng: 141.4884, zoom: 12, city: 'hachinohe',
                        events: [
                            'Goshogawara to Hachinohe ~2hrs (JR Pass)',
                            'Kabushima Shrine: 30,000 tame gulls, 92 stairs',
                            'Tanesashi Coast: rugged Pacific coastline trail',
                            'Miroku Yokocho izakaya: fresh seafood lunch',
                            'Hachinohe to Aomori ~40min',
                            '6:45pm: Nebuta Night 5 (AWARD NIGHT)'
                        ],
                        prose: `<p class="prose-p"><strong>Hachinohe</strong> runs on the Pacific as a fishing port culture that is rougher and colder in character than the festival cities to the west. <strong>Kabushima Shrine</strong> hosts the largest colony of black-tailed gulls in Japan. They have been there long enough to register humans as furniture, and 30,000 birds will not move for you. The shrine requires ninety-two stone stairs on the open ocean, so an umbrella is recommended.</p><p class="prose-p"><strong>Tanesashi Coast</strong> is serious Pacific coastline and one of the less-visited stretches on the east face of Honshu. We are back in Aomori before dark for <strong>Award Night</strong>, the parade where the season's winning floats make their final ceremonial procession. This one carries additional weight. It is the one the city built toward.</p>`
                    },
                    {
                        n: 9, date: 'Fri Aug 8', loc: 'Aomori', emoji: '🎆', type: 'finale',
                        title: 'Nebuta Finale, Marine Procession', img: I.fireworks,
                        lat: 40.8244, lng: 140.7400, zoom: 13, city: 'aomori',
                        events: [
                            'Morning: rest, final market run, pack',
                            '1:00pm: Final daytime parade',
                            'Afternoon: luggage to station lockers',
                            '7:15pm: Marine Procession (floats on boats in Aomori Bay)',
                            'Fireworks over the bay'
                        ],
                        prose: `<p class="prose-p">August 8 the festival turns to face the bay. The float-on-boats procession is not standard Japanese pageantry. It is an internally lit 23-meter warrior lantern mounted on water at night with Aomori's fireworks launching overhead. If you carry one image from this trip intact twenty years from now, it will be this one.</p><p class="prose-p">The <strong>1pm daytime parade</strong> is smaller and more navigable, providing a good final pass when you can actually see the floats without the crowd pressure of the evening. Pack before the fireworks start and move light. This is the last night in Aomori and the end of the festival segment.</p>`
                    }
                ]
            },
            {
                label: 'HOKKAIDO, RAIL NORTH', days: [
                    {
                        n: 10, date: 'Sat Aug 9', loc: 'Hakodate', emoji: '🦀', type: 'travel',
                        title: 'Aomori to Hakodate, Seikan Tunnel', img: I.hokkaido,
                        lat: 41.7688, lng: 140.7289, zoom: 12, city: 'hakodate',
                        events: [
                            'Hokkaido Shinkansen: Shin-Aomori to Shin-Hakodate-Hokuto ~1hr',
                            'SEIKAN TUNNEL: 54km undersea, longest rail tunnel',
                            'Hakodate morning market: fresh crab, uni',
                            'Goryokaku star fort (1864): Western-style bastion',
                            'Mt. Hakodate ropeway: evening view of the isthmus'
                        ],
                        prose: `<p class="prose-p">The Hokkaido Shinkansen descends into the <strong>Seikan Tunnel</strong> 240 meters below the Tsugaru Strait. It runs 54 kilometers underwater as the longest railway tunnel in the world. The transit itself is worth noting. The island arrives quietly.</p><p class="prose-p"><strong>Hakodate</strong> was one of the first Japanese ports opened to international trade in 1854, and it shows in the architecture. <strong>Goryokaku</strong> is a Western-style star fort built in 1864 by a Japan still calibrating what century it was entering. The morning market is serious, and the view from the Mt. Hakodate ropeway at night is exactly why people stop here.</p>`
                    },
                    {
                        n: 11, date: 'Sun Aug 10', loc: 'Sapporo', emoji: '🍺', type: 'travel',
                        title: 'Hakodate to Sapporo', img: I.sapporo,
                        lat: 43.0642, lng: 141.3469, zoom: 12, city: 'sapporo',
                        events: [
                            'Ltd. express train: Hakodate to Sapporo ~3.5hrs',
                            'Sapporo Beer Museum: Akarenga 1890 brick brewery',
                            'Beer garden: all-you-can-eat Genghis Khan lamb BBQ',
                            'Odori Park: Hokkaido central axis',
                            'Susukino: miso ramen at Ramen Alley'
                        ],
                        prose: `<p class="prose-p">The limited express continues three and a half hours north to Sapporo. Sapporo was grid-planned by American agricultural engineers in the 1870s, which is why it reads as spacious and navigable in contrast to every other Japanese city. <strong>Odori Park</strong> is the horizontal axis of the city.</p><p class="prose-p">The <strong>Beer Museum</strong> occupies the original 1890 Akarenga brick brewery where the building makes the argument before anything is poured. Miso ramen was invented here in Susukino's Ramen Alley. The beer garden does Genghis Khan lamb BBQ at a scale that makes a statement.</p>`
                    },
                    {
                        n: 12, date: 'Mon Aug 11', loc: 'Otaru / Lake Toya', emoji: '🚤', type: 'cultural',
                        title: 'Otaru or Lake Toya Day Trip', img: I.otaru,
                        lat: 43.1907, lng: 140.9947, zoom: 13, city: 'otaru',
                        events: [
                            'OPTION 1: Otaru (~35min train), canal, Blue Cave cruise',
                            'Yoichi Nikka Distillery (~25min past Otaru, tasting)',
                            'OPTION 2: Lake Toya (~1.5hr train), caldera lake',
                            'Lake Toya evening fireworks (nightly from lakeshore)'
                        ],
                        prose: `<p class="prose-p"><strong>Otaru</strong> is 35 minutes west and the canal district is genuinely intact with brick warehouses from the herring trade era, low bridges, and salt water. <strong>Sushiya-dori</strong> exists because it is at the port, not because tourists found it. <strong>Nikka Distillery</strong> in Yoichi is another 25 minutes and predates Suntory. Masataka Taketsuru built it in 1934 using methods from Scotland.</p><p class="prose-p">Alternatively, <strong>Lake Toya</strong> is about 1.5 hours away. It is a caldera lake offering a completely different geographical scale, complete with the Mt. Usu ropeway and a summer tradition of nightly fireworks launched directly over the water.</p>`
                    }
                ]
            },
            {
                label: 'TOKYO, CLOSING', days: [
                    {
                        n: 13, date: 'Tue Aug 12', loc: 'Tokyo', emoji: '🌃', type: 'travel',
                        title: 'Sapporo to Tokyo, Return', img: I.tokyo_night,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Flight: New Chitose to Haneda ~1.5hrs',
                            'Check in: closing hotel base',
                            'Evening: Golden Gai, Shinjuku, Shibuya'
                        ],
                        prose: `<p class="prose-p">The return from New Chitose is 90 minutes by air. The train alternative is the better part of eight hours. We fly. Arriving back into Tokyo on the closing leg always registers as re-entry, and the scale recalibrates after ten days in smaller northern spaces.</p><p class="prose-p">The closing hotel base serves as our final check-in. <strong>Golden Gai</strong> is still Golden Gai. It consists of forty-some narrow drinking alleys in Shinjuku, each bar seating eight people maximum, running since the postwar black market that founded it. The evening belongs to wherever momentum takes it.</p>`
                    },
                    {
                        n: 14, date: 'Wed Aug 13', loc: 'Tokyo', emoji: '🎌', type: 'cultural',
                        title: 'Tokyo Closing Day', img: I.vintage,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Koenji: underground vintage/thrift, 60+ stores',
                            'Tokyo in Film location scouting',
                            'Final group lunch',
                            'Shibuya Crossing at dusk',
                            'Departure'
                        ],
                        prose: `<p class="prose-p"><strong>Koenji</strong> is what Harajuku was before it got curated for tourism. It is dense and unpretentious Japanese culture with no performance for outsiders. My ongoing Tokyo in Film location project extensively documents this area. We will scout real filming locations like <strong>Mabashi Inari Shrine</strong>, <strong>Live Music JIROKICHI</strong>, and <strong>KOIWA BUSH BASH</strong>.</p><p class="prose-p">We will hit essential local spots like <strong>Shigekuniya 55 Bakery</strong>, <strong>Floresta Kōenji</strong>, and <strong>Shirohige\u0027s Cream Puff Factory</strong>. For vintage scouting, we visit <strong>KIKI</strong>, <strong>KIKI2</strong>, <strong>Don Don Down</strong>, <strong>Tatouage by ZOOL</strong>, <strong>Treasure Factory Style Used Select</strong>, <strong>BAZZSTORE</strong>, and <strong>Riyususerekutotifana Koenjiten</strong>. We log our final bucket-list lunch at <strong>Koenji Baka Doshi</strong>. <strong>Shibuya Crossing at dusk</strong> is the closing shot. Stand at the center while the city edits itself around you. This is how we close the frame.</p>`
                    }
                ]
            }
        ];"""

pattern = re.compile(r'        const I = \{.*?\n        \];', re.DOTALL)
new_content = pattern.sub(new_js, content)

if content == new_content:
    print("FAILED TO MATCH PATTERN")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("SUCCESS")
