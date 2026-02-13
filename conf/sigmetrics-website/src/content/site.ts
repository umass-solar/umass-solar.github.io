export type NavItem = { label: string; href: string };

export const site = {
  title: "ACM SIGMETRICS",
  tagline: "Special Interest Group on Performance Evaluation",
  description:
    "ACM SIGMETRICS is the ACM Special Interest Group (SIG) for the computer performance evaluation community.",
  contact: {
    email: "webmaster@sigmetrics.org"
  },
  social: {
    x: "https://twitter.com/ACMSigmetrics"
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

export const externalLinks = {
  sigmetricsConference: "https://www.sigmetrics.org/",
  pomacs: "https://dl.acm.org/journal/pomacs",
  joinSigmetrics: "https://campus.acm.org/public/quickjoin/sigs.cfm",
  joinAcm: "https://campus.acm.org/public/quickjoin/assoc.cfm",
  acmStore: "https://store.acm.org/"
};
