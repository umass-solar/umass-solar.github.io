#!/usr/bin/env python3
"""
make_officers.py — write data/officers.json: the elected/appointed officers of ACM
SIGMETRICS by term. Static transcribed data; the website overlays it onto sigmetrics.json
by matching author NAMES (same exact+fuzzy matcher used for awards/chairs), so it marks
officers in the author dashboard with no DBLP refetch.

Sources:
  1971–2023 archive: https://sigmetrics.org/history_officers.shtml
  current term:       https://sigmetrics.org/index.shtml
"""
import json, os, time

# Each term: label, [(role, [names...]), ...]. Roles kept verbatim per the source.
TERMS = [
    ("Current", True, [
        ("Chair", ["Mor Harchol-Balter"]),
        ("Vice-Chair", ["Niklas Carlsson"]),
        ("Secretary/Treasurer", ["Anshul Gandhi"]),
        ("Board of Directors", ["Giulia Fanti", "Y.C. Tay", "Devavrat Shah", "Benny van Houdt"]),
        ("PER Editor", ["Bo Ji"]),
        ("Bulletin Board Editor", ["William Cheng"]),
        ("Webmaster", ["Mohammad Hajiesmaili"]),
        ("Social Media Master", ["Feng Yan", "Zhixuan Fang"]),
        ("Mailing List Manager", ["Marco Paolieri"]),
        ("Conference Advisory Committee", ["Mor Harchol-Balter", "Niklas Carlsson", "Adam Wierman", "Evgenia Smirni"]),
        ("Statistics Czar", ["Niklas Carlsson"]),
        ("Corporate Funding Czar", ["Anshul Gandhi"]),
        ("Awards Coordinator", ["Y.C. Tay"]),
        ("Ethics/Violation/Harassment Czar", ["Giulia Fanti"]),
    ]),
    ("2021-2023", False, [
        ("Chair", ["Giuliano Casale"]),
        ("Vice-Chair", ["Augustin Chaintreau"]),
        ("Secretary/Treasurer", ["Niklas Carlsson"]),
        ("Past Chair", ["Vishal Misra"]),
        ("Board of Directors", ["Sara Alouf", "Devavrat Shah", "R. Srikant", "Adam Wierman"]),
        ("PER Editor", ["Zhenhua Liu"]),
        ("Bulletin Board Editor", ["Bill Cheng"]),
        ("Webmaster", ["Daniela Hurtado-Lange"]),
    ]),
    ("2019-2021", False, [
        ("Chair", ["Giuliano Casale"]),
        ("Vice-Chair", ["Augustin Chaintreau"]),
        ("Secretary/Treasurer", ["Niklas Carlsson"]),
        ("Past Chair", ["Vishal Misra"]),
        ("Board of Directors", ["Sara Alouf", "Devavrat Shah", "R. Srikant", "Adam Wierman"]),
        ("PER Editor", ["Zhenhua Liu"]),
        ("Bulletin Board Editor", ["Bill Cheng"]),
        ("Webmaster", ["Daniela Hurtado-Lange"]),
    ]),
    ("2017-2019", False, [
        ("Chair", ["Vishal Misra"]),
        ("Vice-Chair", ["Adam Wierman"]),
        ("Secretary/Treasurer", ["Niklas Carlsson"]),
        ("Past Chair", ["John C.S. Lui"]),
        ("Board of Directors", ["Giuliano Casale", "Augustin Chaintreau", "Nick Duffield", "Cathy H. Xia"]),
        ("PER Editor", ["Nidhi Hegde"]),
        ("Bulletin Board Editor", ["Bill Cheng"]),
        ("Webmaster", ["Kevin Yang"]),
    ]),
    ("2015-2017", False, [
        ("Chair", ["Vishal Misra"]),
        ("Vice-Chair", ["Adam Wierman"]),
        ("Secretary/Treasurer", ["Niklas Carlsson"]),
        ("Past Chair", ["John C.S. Lui"]),
        ("Board of Directors", ["Giuliano Casale", "Augustin Chaintreau", "Nick Duffield", "Cathy H. Xia"]),
        ("PER Editor", ["Nidhi Hegde"]),
        ("Bulletin Board Editor", ["Bill Cheng"]),
        ("Webmaster", ["Kevin Yang"]),
    ]),
    ("2013-2015", False, [
        ("Chair", ["John C.S. Lui"]),
        ("Vice-Chair", ["Vishal Misra"]),
        ("Secretary/Treasurer", ["John R. Douceur"]),
        ("Past Chair", ["Carey Williamson"]),
        ("N/L Editor", ["Giuliano Casale"]),
        ("Board of Directors", ["Thomas Bonald", "Erich Nahum", "Evgenia Smirni", "Adam Wierman"]),
    ]),
    ("2011-2013", False, [
        ("Chair", ["John C.S. Lui"]),
        ("Vice-Chair", ["Vishal Misra"]),
        ("Secretary/Treasurer", ["John R. Douceur"]),
        ("Past Chair", ["Carey Williamson"]),
        ("N/L Editor", ["Giuliano Casale"]),
        ("Board of Directors", ["Thomas Bonald", "Erich Nahum", "Evgenia Smirni", "Adam Wierman"]),
    ]),
    ("2009-2011", False, [
        ("Chair", ["Carey Williamson"]),
        ("Vice-Chair", ["John C.S. Lui"]),
        ("Secretary/Treasurer", ["Arif Merchant"]),
        ("Past Chair", ["Albert Greenberg"]),
        ("N/L Editor", ["Leana Golubchik"]),
        ("Board of Directors", ["Philippe Nain", "Christoph Lindemann", "Vishal Misra", "Mark Squillante"]),
    ]),
    ("2007-2009", False, [
        ("Chair", ["Carey Williamson"]),
        ("Vice-Chair", ["John C.S. Lui"]),
        ("Secretary/Treasurer", ["Arif Merchant"]),
        ("Past Chair", ["Albert Greenberg"]),
        ("N/L Editor", ["Evgenia Smirni"]),
        ("Board of Directors", ["Philippe Nain", "Christoph Lindemann", "Vishal Misra", "Mark Squillante"]),
    ]),
    ("2005-2007", False, [
        ("Chair", ["Albert Greenberg"]),
        ("Vice-Chair", ["Philip Heidelberger"]),
        ("Secretary/Treasurer", ["Mor Harchol-Balter"]),
        ("Past Chair", ["Leana Golubchik"]),
        ("N/L Editor", ["Evgenia Smirni"]),
        ("Board of Directors", ["John C.S. Lui", "William H. Sanders", "Robert F. Berry", "Leana Golubchik"]),
    ]),
    ("2003-2005", False, [
        ("Chair", ["Leana Golubchik"]),
        ("Vice-Chair", ["Philip Heidelberger"]),
        ("Secretary/Treasurer", ["Robert F. Berry"]),
        ("Past Chair", ["Derek L. Eager"]),
        ("N/L Editor", ["Evgenia Smirni"]),
        ("Board of Directors", ["Sem Borst", "Margaret R. Martonosi", "Edmundo de Souza e Silva", "Jennifer Rexford"]),
    ]),
    ("2001-2003", False, [
        ("Chair", ["Derek L. Eager"]),
        ("Vice-Chair", ["Leana Golubchik"]),
        ("Secretary/Treasurer", ["Robert F. Berry"]),
        ("Past Chair", ["Mary Vernon"]),
        ("N/L Editor", ["Sanjeev Setia"]),
        ("Board of Directors", ["Philip Heidelberger", "William H. Sanders", "Edmundo de Souza e Silva", "Margaret R. Martonosi"]),
    ]),
    ("1999-2001", False, [
        ("Chair", ["Mary Vernon"]),
        ("Vice-Chair", ["Albert Greenberg"]),
        ("Secretary/Treasurer", ["Carey Williamson"]),
        ("Past Chair", ["Murray Woodside"]),
        ("N/L Editor", ["Scott Leutenegger"]),
        ("Board of Directors", ["Leana Golubchik", "Murray Woodside", "Richard R. Muntz", "Garth A. Gibson"]),
    ]),
    ("1997-1999", False, [
        ("Chair", ["Murray Woodside"]),
        ("Vice-Chair", ["Mary Vernon"]),
        ("Secretary/Treasurer", ["Carey Williamson"]),
        ("Past Chair", ["Lawrence W. Dowdy"]),
        ("N/L Editor", ["Scott Leutenegger"]),
        ("Board of Directors", ["Richard R. Muntz", "Albert Greenberg", "Lawrence W. Dowdy", "Mark S. Squillante"]),
    ]),
    ("1995-1997", False, [
        ("Chair", ["Lawrence W. Dowdy"]),
        ("Vice-Chair", ["Murray Woodside"]),
        ("Secretary/Treasurer", ["Scott Leutenegger"]),
        ("Past Chair", ["Linda S. Wright"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Richard Muntz", "Donald Towsley", "Mary Vernon", "Linda S. Wright"]),
    ]),
    ("1993-1995", False, [
        ("Chair", ["Linda S. Wright"]),
        ("Vice-Chair", ["Donald Towsley"]),
        ("Secretary/Treasurer", ["Daniel A. Reed"]),
        ("Past Chair", ["Michael K. Molloy"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Domenico Ferrari", "Michael K. Molloy", "Richard Muntz", "Randolph Nelson"]),
    ]),
    ("1991-1993", False, [
        ("Chair", ["Michael K. Molloy"]),
        ("Vice-Chair", ["Connie U. Smith"]),
        ("Secretary/Treasurer", ["Blaine D. Gaither"]),
        ("Past Chair", ["Tom W. Keller"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Linda S. Wright", "Derek L. Eager", "Richard Muntz", "Daniel A. Reed"]),
    ]),
    ("1989-1991", False, [
        ("Chair", ["Tom W. Keller"]),
        ("Vice-Chair", ["John Zahorjan"]),
        ("Secretary/Treasurer", ["Derek L. Eager"]),
        ("Past Chair", ["Edward Lazowska"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Edward Lazowska", "Connie U. Smith", "Mary Vernon", "Donald Towsley"]),
    ]),
    ("1987-1989", False, [
        ("Chair", ["Edward Lazowska"]),
        ("Vice-Chair", ["Tom W. Keller"]),
        ("Secretary/Treasurer", ["Edward Lazowska"]),
        ("Past Chair", ["Herb Schwetman"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Domenico Ferrari", "Alan Jay Smith", "Mary Vernon", "John Zahorjan"]),
    ]),
    ("1985-1987", False, [
        ("Chair", ["Edward Lazowska"]),
        ("Vice-Chair", ["Connie U. Smith"]),
        ("Secretary/Treasurer", ["Tom W. Keller"]),
        ("Past Chair", ["Herb Schwetman"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Domenico Ferrari", "Herb Schwetman", "Kenneth C. Sevcik", "Alan Jay Smith"]),
    ]),
    ("1983-1985", False, [
        ("Chair", ["Herb Schwetman"]),
        ("Vice-Chair", ["Connie U. Smith"]),
        ("Secretary/Treasurer", ["Tom W. Keller"]),
        ("Past Chair", ["Gary J. Nutt"]),
        ("N/L Editor", ["Blaine D. Gaither"]),
        ("Board of Directors", ["Jeffrey P. Buzen", "Robert L. Morrison", "Charles H. Sauer", "Kenneth C. Sevcik"]),
    ]),
    ("1981-1983", False, [
        ("Chair", ["Herb Schwetman"]),
        ("Vice-Chair", ["James P. Bouhana"]),
        ("Secretary/Treasurer", ["Robert L. Morrison"]),
        ("Past Chair", ["Gary J. Nutt"]),
        ("N/L Editor", ["Harold Joseph Highland"]),
        ("Board of Directors", ["Thomas E. Bell", "Jeffrey Buzen", "Jo Ann Lockett", "Charles H. Sauer"]),
    ]),
    ("1979-1981", False, [
        ("Chair", ["Gary J. Nutt"]),
        ("Vice-Chair", ["Dennis M. Conti"]),
        ("Secretary/Treasurer", ["Robert L. Morrison"]),
        ("Past Chair", ["Warren J. Erikson"]),
        ("N/L Editor", ["Harold Joseph Highland"]),
        ("Board of Directors", ["Thomas E. Bell", "Philip J. Kiviat", "Stephen R. Kimbleton", "Harold Joseph Highland"]),
    ]),
    ("1977-1979", False, [
        ("Chair", ["Warren J. Erikson"]),
        ("Vice-Chair", ["Thomas Giammo"]),
        ("Secretary/Treasurer", ["Mark Allen Franklin"]),
        ("Past Chair", ["Philip J. Kiviat"]),
        ("N/L Editor", ["Harold Joseph Highland"]),
        ("Board of Directors", ["Thomas E. Bell", "Philip J. Kiviat", "Jeffrey Buzen", "C. Dudley Warner"]),
    ]),
    ("1975-1977", False, [
        ("Chair", ["Philip J. Kiviat"]),
        ("Vice-Chair", ["Forest Baskett III"]),
        ("Secretary/Treasurer", ["Thomas E. Bell"]),
        ("Past Chair", ["Stephen Kimbleton"]),
        ("N/L Editor", ["Michael F. Morris"]),
        ("Board of Directors", ["Barry W. Boehm", "Stephen Kimbleton", "Kenneth Kolence", "Michael F. Morris"]),
    ]),
    ("1973-1975", False, [
        ("Chair", ["Philip J. Kiviat"]),
        ("Vice-Chair", ["Tad Pinkerton"]),
        ("Secretary/Treasurer", ["Thomas E. Bell"]),
        ("Past Chair", ["Stephen Kimbleton"]),
        ("N/L Editor", ["J.C. Browne"]),
        ("Board of Directors", ["Gary Carlson", "Stephen Kimbleton", "Kenneth Kolence", "Michael F. Morris"]),
    ]),
    ("1971-1973", False, [
        ("Chair", ["Stephen Kimbleton"]),
        ("Secretary/Treasurer", ["C.V. Apter (Viki)"]),
        ("N/L Editor", ["Henry C. Lucas, Jr."]),
        ("Board of Directors", ["Robert R. Johnson", "J.D. Madden", "Richard Muntz", "Tad Pinkerton"]),
    ]),
]

out = {
    "generatedAt": int(time.time() * 1000),
    "source": "https://sigmetrics.org/history_officers.shtml (+ current officers from index.shtml)",
    "terms": [
        {"term": label, "current": cur,
         "roles": [{"role": role, "people": people} for (role, people) in roles]}
        for (label, cur, roles) in TERMS
    ],
}
os.makedirs("data", exist_ok=True)
with open("data/officers.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
names = {n for _, _, roles in TERMS for _, ppl in roles for n in ppl}
print(f"Wrote data/officers.json: {len(TERMS)} terms ({TERMS[-1][0]}–current), {len(names)} distinct officers")
