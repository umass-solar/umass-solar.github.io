export type Officer = { role: string; name: string; href?: string };

export const officers: Officer[] = [
  { role: "SIG Chair", name: "Mor Harchol-Balter", href: "https://www.cs.cmu.edu/" },
  { role: "SIG Vice Chair", name: "Niklas Carlsson", href: "https://www.ida.liu.se/" },
  { role: "SIG Secretary/Treasurer", name: "Anshul Gandhi", href: "https://www3.cs.stonybrook.edu/" },
  { role: "PER Editor", name: "Bo Ji", href: "https://people.cs.vt.edu/" },
  { role: "Bulletin Board Editor", name: "William Cheng", href: "https://merlot.usc.edu/" },
  { role: "SIG Webmaster", name: "Mohammad Hajiesmaili", href: "https://groups.cs.umass.edu/" }
];

export const committees = {
  boardOfDirectors: [
    { name: "Giulia Fanti", href: "https://gfanti.github.io/" },
    { name: "Y.C. Tay", href: "https://www.comp.nus.edu.sg/" },
    { name: "Devavrat Shah", href: "https://devavrat.mit.edu/" },
    { name: "Benny van Houdt", href: "https://win.uantwerpen.be/" }
  ],
  executiveCommitteeNote:
    "This is the steering committee of ACM SIGMETRICS as per its bylaws.",
  executiveCommitteeMembers: [
    "Niklas Carlsson",
    "Giulia Fanti",
    "Anshul Gandhi",
    "Mor Harchol-Balter",
    "Athina Markopoulou",
    "Devavrat Shah",
    "Benny van Houdt"
  ]
};
