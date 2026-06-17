#!/usr/bin/env python3
"""
make_chairs.py — write data/chairs.json: the General Chairs and Program (TPC) Chairs of
every ACM SIGMETRICS conference. Static transcribed data; the website overlays it onto
sigmetrics.json by matching author NAMES (same exact+fuzzy matcher used for awards), so it
marks chairs in the author dashboard without any DBLP refetch.

Sources:
  1973–2024: https://sigmetrics.org/history_conferences.shtml
  2025:      https://www.sigmetrics.org/sigmetrics2025/organization.html
  2026:      https://www.sigmetrics.org/sigmetrics2026/organization.html
  2027:      https://www.sigmetrics.org/sigmetrics2027/pages/organization.html
"""
import json, os, time

# year: (location, [general chairs], [program/TPC chairs])
CONF = [
    (2027,"Atlanta, Georgia, USA",      ["Siva Theja Maguluri","Debankur Mukherjee","Zhi-Li Zhang"], ["Varun Gupta","Longbo Huang","Mahmut Taylan Kandemir"]),
    (2026,"Ann Arbor, Michigan, USA",   ["Vijay Subramanian","Atilla Eryilmaz"],                     ["Nicolas Gast","Stefan Schmid","Weina Wang"]),
    (2025,"Stony Brook, New York, USA", ["Anshul Gandhi","Zhenhua Liu"],                             ["Sewoong Oh","Ramesh Sitaraman","Benny Van Houdt"]),
    (2024,"Venice, Italy",              ["Andrea Marin","Michele Garetto"],                          ["Giulia Fanti","Florin Ciucu","Rhonda Righter"]),
    (2023,"Orlando, Florida, USA",      ["Evgenia Smirni"],                                          ["Konstantin Avrachenkov","Phillipa Gill","Bhuvan Urgaonkar"]),
    (2022,"Mumbai, India",              ["D. Manjunath","Jayakrishnan Nair"],                        ["Niklas Carlsson","Edith Cohen","Philippe Robert"]),
    (2021,"Beijing, China",             ["Andrew C. Yao","Longbo Huang"],                            ["Anshul Gandhi","Negar Kiyavash","Jia Wang"]),
    (2020,"Boston, Massachusetts, USA", ["Edmund Yeh"],                                              ["Athina Markopoulou","Y.C. Tay"]),
    (2019,"Phoenix, Arizona, USA",      ["Erich M. Nahum"],                                          ["Thomas Bonald","Nick Duffield"]),
    (2018,"Irvine, California, USA",     ["Konstantinos Psounis"],                                    ["Aditya Akella","Adam Wierman"]),
    (2017,"Urbana-Champaign, Illinois, USA", ["Bruce Hajek","Sewoong Oh"],                           ["Augustin Chaintreau","Leana Golubchik","Zhi-Li Zhang"]),
    (2016,"Antibes Juan-les-Pins, France", ["Sara Alouf","Alain Jean-Marie"],                        ["Nidhi Hegde","Alexandre Proutière"]),
    (2015,"Portland, Oregon, USA",      ["Bill Lin","Jun (Jim) Xu"],                                 ["Sudipta Sengupta","Devavrat Shah"]),
    (2014,"Austin, Texas, USA",         ["Sujay Sanghavi","Sanjay Shakkottai"],                      ["Marc Lelarge","Bianca Schroeder"]),
    (2013,"Pittsburgh, Pennsylvania, USA", ["Mor Harchol-Balter"],                                   ["John Douceur","Jun Xu"]),
    (2012,"London, UK",                 ["Peter Harrison"],                                          ["Martin Arlitt","Giuliano Casale"]),
    (2011,"San Jose, California, USA",  ["Arif Merchant"],                                           ["Kim Keeton","Dan Rubenstein"]),
    (2010,"New York, New York, USA",    ["Vishal Misra"],                                            ["Paul Barford","Mark Squillante"]),
    (2009,"Seattle, Washington, USA",   ["John Douceur","Albert Greenberg"],                         ["Thomas Bonald","Jason Nieh"]),
    (2008,"Annapolis, Maryland, USA",   ["Zhen Liu"],                                                ["Vishal Misra","Prashant Shenoy"]),
    (2007,"San Diego, California, USA", ["Leana Golubchik"],                                         ["Mostafa Ammar","Mor Harchol-Balter"]),
    (2006,"Saint-Malo, France",         ["Raymond Marie"],                                           ["Peter Key","Evgenia Smirni"]),
    (2005,"Banff, Alberta, Canada",     ["Derek Eager","Carey Williamson"],                          ["Sem Borst","John C.S. Lui"]),
    (2004,"New York, New York, USA",    ["Ed Coffman"],                                              ["Zhen Liu","Arif Merchant"]),
    (2003,"San Diego, California, USA", ["Bill Cheng","Satish Tripathi"],                            ["Jennifer Rexford","William H. Sanders"]),
    (2002,"Marina del Rey, California, USA", ["Richard Muntz"],                                      ["Margaret Martonosi","Edmundo de Souza e Silva"]),
    (2001,"Cambridge, Massachusetts, USA", ["Philip Heidelberger"],                                  ["Ernst Biersack","Leana Golubchik"]),
    (2000,"Santa Clara, California, USA", ["Alexander Brandwajn"],                                    ["Jim Kurose","Philippe Nain"]),
    (1999,"Atlanta, Georgia, USA",      ["Daniel Menasce"],                                          ["Carey Williamson"]),
    (1998,"Madison, Wisconsin, USA",    ["Mary Vernon"],                                             ["Garth Gibson","Guy Latouche"]),
    (1997,"Seattle, Washington, USA",   ["John Zahorjan"],                                           ["Albert Greenberg"]),
    (1996,"Philadelphia, Pennsylvania, USA", ["Daniel A. Reed"],                                     ["David Nicol"]),
    (1995,"Ottawa, Ontario, Canada",    ["Murray Woodside"],                                         ["Satish Tripathi","Isi Mitrani"]),
    (1994,"Nashville, Tennessee, USA",  ["Larry Dowdy"],                                             ["Rick Bunt"]),
    (1993,"Santa Clara, California, USA", ["Susan Owicki"],                                          ["Richard Muntz"]),
    (1992,"Newport, Rhode Island, USA", ["Linda S. Wright"],                                         ["Philip Heidelberger","Don Towsley"]),
    (1991,"San Diego, California, USA", ["Michael K. Molloy"],                                       ["John Zahorjan"]),
    (1990,"Boulder, Colorado, USA",     ["Gary J. Nutt"],                                            ["Mary Vernon"]),
    (1989,"Berkeley, California, USA",  ["Domenico Ferrari"],                                        ["Alan Jay Smith"]),
    (1988,"Santa Fe, New Mexico, USA",  ["Connie U. Smith"],                                         ["Kenneth C. Sevcik"]),
    (1987,"Banff, Alberta, Canada",     ["Rick Bunt"],                                               ["Derek Eager"]),
    (1986,"Raleigh, North Carolina, USA", ["H.G. Perros"],                                           ["W.J. Stewart","K.S. Trivedi"]),
    (1985,"Austin, Texas, USA",         ["Herb D. Schwetman"],                                       ["Jeffrey A. Brumfield","Daniel A. Reed"]),
    (1984,"Cambridge, Massachusetts, USA", ["Herb D. Schwetman"],                                    ["James P. Bouhana","Ray Bryant"]),
    (1983,"Minneapolis, Minnesota, USA", ["Herb D. Schwetman"],                                      ["Steven Bruell","Larry Dowdy"]),
    (1982,"Seattle, Washington, USA",   ["John Zahorjan"],                                           ["Edward Lazowska"]),
    (1981,"Las Vegas, Nevada, USA",     ["Herb D. Schwetman"],                                       ["Stephen W. Sherman"]),
    (1980,"Toronto, Ontario, Canada",   ["Kenneth C. Sevcik"],                                       ["G. Scott Graham"]),
    (1979,"Boulder, Colorado, USA",     ["Paul F. Roth"],                                            ["Gary J. Nutt"]),
    (1977,"Washington, D.C., USA",      ["Robert J. Bishop"],                                        ["Robert L. Morrison"]),
    (1976,"Cambridge, Massachusetts, USA", ["Jeff Buzen","Arnold Ockene"],                           ["P.P.S. Chen","Mark Franklin"]),
    (1974,"Montreal, Quebec, Canada",   ["James D. Connell"],                                        ["John H. Howard"]),
    (1973,"Palo Alto, California, USA", ["Don Madden"],                                              ["Tad Pinkerton"]),
]

out = {
    "generatedAt": int(time.time()*1000),
    "source": "https://sigmetrics.org/history_conferences.shtml (+ 2025–2027 organization pages)",
    "conferences": [{"year": y, "location": loc, "general": g, "program": p} for (y, loc, g, p) in CONF],
}
os.makedirs("data", exist_ok=True)
with open("data/chairs.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
gset={n for _,_,g,_ in CONF for n in g}; pset={n for _,_,_,p in CONF for n in p}
print(f"Wrote data/chairs.json: {len(CONF)} conferences ({CONF[-1][0]}–{CONF[0][0]}), "
      f"{len(gset)} distinct general chairs, {len(pset)} distinct program chairs")
