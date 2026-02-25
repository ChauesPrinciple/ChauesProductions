import re
import os

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_js = """        const I = {
            main: 'assets/images/bg.jpg',
            portrait: 'assets/images/image07.png',
            bonsai: 'assets/images/image01.png',
            bunbun: 'assets/images/image02.png'
        };

        const SECTIONS = [
            {
                label: 'TOKYO : OPENING', days: [
                    {
                        n: 1, date: 'Thu Jul 31', loc: 'Tokyo', emoji: '✈️', type: 'arrival',
                        title: 'Arrive Tokyo', img: I.main,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Land Haneda or Narita: check in to Sequence Miyashita Park, Shibuya',
                            'Welcome lunch: Udatsu Sushi \u26a0\ufe0f confirm group capacity',
                            'Easy evening: ramen, Kabukicho or Shibuya Crossing',
                            'Get on Japan time by walking, not sleeping'
                        ],
                        prose: `<p class="prose-p">We check into Sequence Miyashita Park in Shibuya. The hotel sits directly above Miyashita Park. Shibuya is our home base for the opening days.</p><p class="prose-p">We open at Udatsu for counter omakase with Chef Toru Udatsu. You need to stay active this evening to adjust to the local time. We will walk through Shibuya Crossing at dusk.</p>`
                    },
                    {
                        n: 2, date: 'Fri Aug 1', loc: 'Tokyo', emoji: '🎭', type: 'partner',
                        title: 'TeamLab, BunBun, Shibuya Sky', img: I.bunbun,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Morning: TeamLab (book timed entry in advance)',
                            'Optional: Kimono dressing/sale with local business partner',
                            'Midday to afternoon: Tokyo BunBun acting partner',
                            'Evening: Shibuya Sky night viewing (Scramble Square rooftop)'
                        ],
                        prose: `<p class="prose-p">We start the day at TeamLab, which is a full-body immersive installation. Book timed entry ahead of time because it sells out. We have an optional stop for kimono dressing with a local business.</p><p class="prose-p">In the afternoon, we work with BunBun. This requires physical acting participation from the entire group. The night closes at Shibuya Sky on the Scramble Square rooftop, which provides an unobstructed view of the crossing.</p>`
                    },
                    {
                        n: 3, date: 'Sat Aug 2', loc: 'Tokyo', emoji: '🏎️', type: 'partner',
                        title: 'Bonsai Racing (Confirmed Partner)', img: I.bonsai,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Full day with Bonsai Racing partner',
                            'Evening at leisure in Tokyo'
                        ],
                        prose: `<p class="prose-p">We spend the full day with Bonsai Racing. This is a confirmed production partner. You will document the racing environment. The material recorded here will be part of the final project.</p>`
                    }
                ]
            },
            {
                label: 'JOURNEY NORTH', days: [
                    {
                        n: 4, date: 'Sun Aug 3', loc: 'Morioka', emoji: '🥁', type: 'travel',
                        title: 'Tokyo to Morioka, Sansa Festival', img: I.main,
                        lat: 39.7014, lng: 141.1349, zoom: 13, city: 'morioka',
                        events: [
                            'Tohoku Shinkansen ~2h20m: reserve group block (JR Pass)',
                            '\u26a0\ufe0f Possible stop: Ebisu brewery in Fukushima (user to confirm)',
                            'Kitakami River walk: Mt. Iwate over the city',
                            'Azumaya: wanko soba until you tap out',
                            'Nagasawa Coffee or Clammbon',
                            'EVENING: Morioka Sansa Festival'
                        ],
                        prose: `<p class="prose-p">We take the Tohoku Shinkansen north. There is a potential stop at an Ebisu site in Fukushima depending on our timing. Our primary destination today is Morioka. The city is dense and functional, split by the Kitakami River. We will eat wanko soba at Azumaya.</p><p class="prose-p">We stop here for the Sansa Festival. It is a large taiko drum procession with 10,000 performers. When the night closes, the procession opens to the public. You will join the dancers.</p>`
                    },
                    {
                        n: 5, date: 'Mon Aug 4', loc: 'Aomori', emoji: '🎏', type: 'travel',
                        title: 'Morioka to Aomori, Nebuta Night 3', img: I.main,
                        lat: 40.8244, lng: 140.7400, zoom: 13, city: 'aomori',
                        events: [
                            'Shinkansen Morioka to Aomori ~1hr (JR Pass)',
                            'Check in: first parade night, arrive with energy',
                            'A-FACTORY waterfront: apple cider, bay views',
                            'Rassera Land: floats up close at builder huts',
                            '6:45pm: Nebuta Night 3',
                            'Haneto costume (join the procession)'
                        ],
                        prose: `<p class="prose-p">We ride the shinkansen one hour north to Aomori. The city organizes its summer around the Nebuta festival. Teams pull large lantern floats through the streets while Haneto dancers circle them.</p><p class="prose-p">Tonight is our first parade night. We will rent the required costumes. We will participate directly in the Haneto dance instead of just observing.</p>`
                    }
                ]
            },
            {
                label: 'AOMORI, NEBUTA FESTIVAL', days: [
                    {
                        n: 6, date: 'Tue Aug 5', loc: 'Aomori', emoji: '🍣', type: 'cultural',
                        title: 'Aomori Cultural Day, Nebuta Night 4', img: I.main,
                        lat: 40.8244, lng: 140.7400, zoom: 13, city: 'aomori',
                        events: [
                            '7am: Nokke-don at Furukawa Market',
                            'Nebuta no Ie Wa Rasse: float museum, costume try-on',
                            'Aomori Museum of Art: Yoshitomo Nara Aomori Dog',
                            'Sannai-Maruyama Jomon Site (UNESCO, bus ~20min)',
                            '6:45pm: Nebuta Night 4'
                        ],
                        prose: `<p class="prose-p">We visit Furukawa Market early in the morning. You buy a bowl of rice and walk the market to choose custom sashimi toppings from local stalls. We will later visit Wa Rasse to look at the internal wire armatures and lighting arrays of a nebuta float.</p><p class="prose-p">In the afternoon, we take a bus to Sannai-Maruyama. This is an active 5,500 year old Jomon settlement with UNESCO status. The evening concludes with another parade session at 6:45 pm.</p>`
                    },
                    {
                        n: 7, date: 'Wed Aug 6', loc: 'Hirosaki / Goshogawara', emoji: '🔴', type: 'festival',
                        title: 'Hirosaki to Goshogawara, Tachineputa Overnight', img: I.main,
                        lat: 40.8065, lng: 140.4390, zoom: 13, city: 'goshogawara',
                        events: [
                            'Morning: Hirosaki Castle (Edo original) and MOCA',
                            'Gono Line to Goshogawara (~40min from Hirosaki)',
                            'Tachineputa no Yakata: 23m giants year-round',
                            '19:00 to 21:00: Goshogawara Tachineputa',
                            'Floats 23m tall, 19 tons: stand at corners for the pivot',
                            '\u26a0\ufe0f Overnight: last train to Aomori departs 19:33'
                        ],
                        prose: `<p class="prose-p">We spend the morning at Hirosaki Castle, which is an original Edo period fortress structure. We also visit the MOCA, housed in a converted sake brewery. We then catch the Gono Line west to Goshogawara.</p><p class="prose-p">In Goshogawara, local teams navigate 23-meter Tachineputa floats through narrow intersections. We will position ourselves at a street corner on the parade route to watch the teams pivot the structures. We must secure local accommodation tonight because the final returning train to Aomori leaves before the parade begins.</p>`
                    },
                    {
                        n: 8, date: 'Thu Aug 7', loc: 'Hachinohe', emoji: '🦅', type: 'festival',
                        title: 'Hachinohe Coast, Nebuta Award Night', img: I.main,
                        lat: 40.5122, lng: 141.4884, zoom: 12, city: 'hachinohe',
                        events: [
                            'Goshogawara to Hachinohe ~2hrs (JR Pass)',
                            'Kabushima Shrine: 30,000 tame gulls, 92 stairs',
                            'Tanesashi Coast: rugged Pacific coastline trail',
                            'Miroku Yokocho izakaya: fresh seafood lunch',
                            'Hachinohe to Aomori ~40min',
                            '6:45pm: Nebuta Night 5 (AWARD NIGHT)'
                        ],
                        prose: `<p class="prose-p">Hachinohe is a cold-water fishing port on the Pacific side of the region. We visit Kabushima Shrine, which hosts a large colony of black-tailed gulls. Be prepared for aggressive bird populations on the stairs and bring an umbrella.</p><p class="prose-p">We hike the Tanesashi Coast along the east face of Honshu. We return to Aomori before dark for Award Night. This is the final ceremonial procession for the winning floats.</p>`
                    },
                    {
                        n: 9, date: 'Fri Aug 8', loc: 'Aomori', emoji: '🎆', type: 'finale',
                        title: 'Nebuta Finale, Marine Procession', img: I.main,
                        lat: 40.8244, lng: 140.7400, zoom: 13, city: 'aomori',
                        events: [
                            'Morning: rest, final market run, pack',
                            '1:00pm: Final daytime parade',
                            'Afternoon: luggage to station lockers',
                            '7:15pm: Marine Procession (floats on boats in Aomori Bay)',
                            'Fireworks over the bay'
                        ],
                        prose: `<p class="prose-p">On August 8, the festival transitions to the bay. Teams mount the lit floats onto boats to process on the water while Aomori launches fireworks overhead. We will view the final daytime parade at 1:00 pm, which is much less crowded.</p><p class="prose-p">We need to pack up and move our luggage to the station lockers before the fireworks begin. This marks our final night in Aomori and the end of the festival segment of the trip.</p>`
                    }
                ]
            },
            {
                label: 'HOKKAIDO, RAIL NORTH', days: [
                    {
                        n: 10, date: 'Sat Aug 9', loc: 'Hakodate', emoji: '🦀', type: 'travel',
                        title: 'Aomori to Hakodate, Seikan Tunnel', img: I.main,
                        lat: 41.7688, lng: 140.7289, zoom: 12, city: 'hakodate',
                        events: [
                            'Hokkaido Shinkansen: Shin-Aomori to Shin-Hakodate-Hokuto ~1hr',
                            'SEIKAN TUNNEL: 54km undersea, longest rail tunnel',
                            'Hakodate morning market: fresh crab, uni',
                            'Goryokaku star fort (1864): Western-style bastion',
                            'Mt. Hakodate ropeway: evening view of the isthmus'
                        ],
                        prose: `<p class="prose-p">The Hokkaido Shinkansen travels through the Seikan Tunnel, which runs 54 kilometers underwater below the Tsugaru Strait. We emerge on the northern island and arrive in Hakodate. This was one of the first Japanese ports opened to international trade in 1854.</p><p class="prose-p">We explore Goryokaku, an early Western-style star fort built in 1864. We will also visit the morning port market and take the Mt. Hakodate ropeway at night to view the isthmus from elevation.</p>`
                    },
                    {
                        n: 11, date: 'Sun Aug 10', loc: 'Sapporo', emoji: '🍺', type: 'travel',
                        title: 'Hakodate to Sapporo', img: I.main,
                        lat: 43.0642, lng: 141.3469, zoom: 12, city: 'sapporo',
                        events: [
                            'Ltd. express train: Hakodate to Sapporo ~3.5hrs',
                            'Sapporo Beer Museum: Akarenga 1890 brick brewery',
                            'Beer garden: all-you-can-eat Genghis Khan lamb BBQ',
                            'Odori Park: Hokkaido central axis',
                            'Susukino: miso ramen at Ramen Alley'
                        ],
                        prose: `<p class="prose-p">We take the limited express train three and a half hours north to Sapporo. American agricultural engineers established the Sapporo grid plan in the 1870s. This makes the city noticeably more spacious than other Japanese cities.</p><p class="prose-p">We walk through Odori Park and visit the Beer Museum, housed in the original 1890 Akarenga brick brewery. We will eat local miso ramen in Susukino. We also have a confirmed dinner reservation at the beer garden for the Genghis Khan lamb BBQ.</p>`
                    },
                    {
                        n: 12, date: 'Mon Aug 11', loc: 'Otaru / Lake Toya', emoji: '🚤', type: 'cultural',
                        title: 'Otaru or Lake Toya Day Trip', img: I.main,
                        lat: 43.1907, lng: 140.9947, zoom: 13, city: 'otaru',
                        events: [
                            'OPTION 1: Otaru (~35min train), canal, Blue Cave cruise',
                            'Yoichi Nikka Distillery (~25min past Otaru, tasting)',
                            'OPTION 2: Lake Toya (~1.5hr train), caldera lake',
                            'Lake Toya evening fireworks (nightly from lakeshore)'
                        ],
                        prose: `<p class="prose-p">We have two logistical options for today. Option 1 is Otaru, a 35 minute train ride west on the coast. We can survey the intact canal district and secure a boat to access the Blue Cave. We can also tour the Nikka Distillery in Yoichi further down the rail line.</p><p class="prose-p">Option 2 is Lake Toya, a 1.5 hour trip. Lake Toya is a massive caldera lake. We can take the Mt. Usu ropeway and observe the fireworks launched directly over the water at night.</p>`
                    }
                ]
            },
            {
                label: 'TOKYO, CLOSING', days: [
                    {
                        n: 13, date: 'Tue Aug 12', loc: 'Tokyo', emoji: '🌃', type: 'travel',
                        title: 'Sapporo to Tokyo, Return', img: I.main,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Flight: New Chitose to Haneda ~1.5hrs',
                            'Check in: closing hotel base',
                            'Evening: Golden Gai, Shinjuku, Shibuya'
                        ],
                        prose: `<p class="prose-p">We process a 90 minute flight from New Chitose directly to Haneda. We check into our final hotel base back in Tokyo to drop our gear.</p><p class="prose-p">We spend the evening in Golden Gai in Shinjuku. These drinking alleys have operated continuously since the post-war period. Each small establishment seats a strict maximum of eight people.</p>`
                    },
                    {
                        n: 14, date: 'Wed Aug 13', loc: 'Tokyo', emoji: '🎌', type: 'cultural',
                        title: 'Tokyo Closing Day', img: I.main,
                        lat: 35.6812, lng: 139.7671, zoom: 12, city: 'tokyo',
                        events: [
                            'Koenji: underground vintage/thrift, 60+ stores',
                            'OR: Shimokitazawa, Akihabara, Ginza',
                            'Final group lunch',
                            'Shibuya Crossing at dusk',
                            'Departure'
                        ],
                        prose: `<p class="prose-p">We travel to Koenji for vintage clothing shopping. The neighborhood focuses heavily on items from the 1970s through the 1990s. We also have the specific option to visit Shimokitazawa for vinyl records.</p><p class="prose-p">We eat our final scheduled lunch of the trip at a location we researched earlier. Afterward, we return to Shibuya Crossing at dusk before pulling our bags and checking in at the regional airport.</p>`
                    }
                ]
            }
        ];"""

pattern = re.compile(r'        const I = \{.*?\];', re.DOTALL)
new_content = pattern.sub(new_js, content)

# Check if content changed
if content == new_content:
    print("FAILED TO MATCH PATTERN")

new_content = new_content.replace('—', ':')
new_content = new_content.replace('–', 'to')

new_content = new_content.replace('Rassera! : Japan Summer', 'Rassera! Japan Summer')
new_content = new_content.replace('Chaues Productions · Group 8to12', 'Chaues Productions : Group 8 to 12')
new_content = new_content.replace('Chaues Productions · Group 8 to 12', 'Chaues Productions : Group 8 to 12')
new_content = new_content.replace('July 31 to August 13, 2026 · 14 days', 'July 31 to August 13, 2026 : 14 days')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("SUCCESS")
