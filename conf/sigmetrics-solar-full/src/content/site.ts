export type NavItem = { label: string; href: string };

export const site = {
  title: "ACM SIGMETRICS",
  tagline: "Special Interest Group on Performance Evaluation",
  description:
    "SIGMETRICS is the ACM Special Interest Group (SIG) for the computer performance evaluation community.",
  contact: {
    email: "webmaster@sigmetrics.org"
  },
  social: {
    x: "https://twitter.com/ACMSigmetrics"
  },
  originals: {
    home: "https://www.sigmetrics.org/",
    awards: "https://www.sigmetrics.org/awards.shtml",
    frequentAuthors: "https://sigmetrics.org/frequent-authors.shtml",
    history: "https://www.sigmetrics.org/history.shtml",
    mailingList: "https://www.sigmetrics.org/mailinglist.shtml",
    newsletter: "https://www.sigmetrics.org/per.shtml",
    procedures: "https://www.sigmetrics.org/procedures.shtml",
    studentActivities: "https://sigmetrics.org/students.shtml",
    acmFellows: "https://www.sigmetrics.org/acm-fellows.shtml",
    acmOpenTOC: "https://www.sigmetrics.org/opentoc.shtml",
    dei: "https://www.sigmetrics.org/DEI.shtml",
    volunteering: "https://www.sigmetrics.org/volunteers.shtml"
  }
};

export const nav: NavItem[] = [
  { label: "Home", href: "/" },
  { label: "Awards", href: "/awards" },
  { label: "Frequent Authors", href: "/frequent-authors" },
  { label: "History", href: "/history" },
  { label: "Mailing List", href: "/mailing-list" },
  { label: "Newsletter", href: "/newsletter" },
  { label: "Procedures", href: "/procedures" },
  { label: "Student Activities", href: "/student-activities" },
  { label: "ACM Fellows", href: "/acm-fellows" },
  { label: "ACM OpenTOC", href: "/acm-opentoc" },
  { label: "DEI", href: "/dei" },
  { label: "Volunteering", href: "/volunteering" }
];

export const links = {
  pomacs: "https://dl.acm.org/journal/pomacs",
  acm: "https://www.acm.org",
  joinSigmetrics: "https://campus.acm.org/public/quickjoin/sigs.cfm",
  joinAcm: "https://campus.acm.org/public/quickjoin/assoc.cfm",
  acmStore: "https://store.acm.org/",
  sigmetricsConference: "https://www.sigmetrics.org/"
};
